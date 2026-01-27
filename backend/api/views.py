from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from design_plagiarism_core.core.compare import compare_images
from reports.models import Report
from designs.models import DesignImage
from rest_framework.permissions import AllowAny



class CompareAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        image_1 = request.FILES.get("image_1")
        image_2 = request.FILES.get("image_2")

        if not image_1 or not image_2:
            return Response(
                {"error": "Both image_1 and image_2 are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        img_obj_1 = DesignImage.objects.create(
            image=image_1,
            uploaded_by=request.user
        )

        img_obj_2 = DesignImage.objects.create(
            image=image_2,
            uploaded_by=request.user
        )

        # Run comparison
        result = compare_images(
            img_obj_1.image.path,
            img_obj_2.image.path,
        )

        # -------- DB reference comparison (READ-ONLY) --------

        # Exclude the two images just uploaded
        db_images = DesignImage.objects.exclude(
            id__in=[img_obj_1.id, img_obj_2.id]
        )

        best_db_score = 0.0
        best_match_id = None

        for db_img in db_images:
            # Compare image_1 with DB image
            res_1 = compare_images(
                img_obj_1.image.path,
                db_img.image.path
            )

            # Compare image_2 with DB image
            res_2 = compare_images(
                img_obj_2.image.path,
                db_img.image.path
            )

            score_1 = res_1["final_score"]
            score_2 = res_2["final_score"]

            current_best = max(score_1, score_2)

            if current_best > best_db_score:
                best_db_score = current_best
                best_match_id = db_img.id


        report = Report.objects.create(
            user=request.user if request.user.is_authenticated else None,
            image_1=img_obj_1.image,
            image_2=img_obj_2.image,
            scores=result["scores"],
            final_score=result["final_score"],
            verdict=result["verdict"],
            explanation=result["decision"]["reason"],
        )
        

        return Response(
            {
                "pairwise_result": result,
                "database_match": {
                    "best_match_id": best_match_id,
                    "best_score": round(best_db_score, 3),
                },
            },
            status=status.HTTP_200_OK,
            )
