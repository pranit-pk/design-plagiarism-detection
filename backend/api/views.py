from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

from reports.models import Report
from design_plagiarism_core.core.compare import compare_images


class CompareAPIView(APIView):
    def post(self, request):
        image_1 = request.FILES.get("image_1")
        image_2 = request.FILES.get("image_2")

        if not image_1 or not image_2:
            return Response(
                {"error": "Both image_1 and image_2 are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Save images temporarily via Report model
        dummy_user = User.objects.first()  # auth comes later

        report = Report.objects.create(
            user=dummy_user,
            image_1=image_1,
            image_2=image_2,
            scores={},
            final_score=0.0,
            verdict="",
            explanation="",
        )

        # Run comparison
        result = compare_images(
            report.image_1.path,
            report.image_2.path,
        )

        # Update report
        report.scores = result["scores"]
        report.final_score = result["final_score"]
        report.verdict = result["verdict"]
        report.explanation = result["explanation"]
        report.save()

        return Response(result, status=status.HTTP_200_OK)
