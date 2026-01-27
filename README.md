# Design Plagiarism Detection System (Backend)

A backend-focused system for detecting visual plagiarism between design images using multiple computer vision similarity metrics and a weighted decision layer.

This project focuses on algorithmic correctness, modular design, and scalable comparison logic, exposed via a REST API.

---

## Features

- Image preprocessing with aspect-ratio–preserving resizing
- Multiple similarity metrics:
  - Pixel-level similarity
  - Structural Similarity Index (SSIM)
  - ORB feature matching
  - Color histogram similarity
- Weighted scoring system to combine metrics
- Human-readable verdict generation (Low / Moderate / High similarity)
- Plagiarism decision layer with confidence levels
- REST API for image comparison
- Database-backed reference image storage for global comparison

---

## Core Logic Overview

1. Images are preprocessed and resized consistently
2. Each similarity metric independently computes a normalized score
3. Scores are combined using explicit weights
4. A decision layer classifies similarity and plagiarism confidence
5. Uploaded designs are compared against stored reference images

---

## Tech Stack

- Python
- Django
- Django REST Framework
- OpenCV
- NumPy
- SQLite (development)

---

## API Endpoint

### POST /api/compare/

**Request**
- multipart/form-data
- Fields:
  - image_1
  - image_2

**Response**
- Similarity scores per metric
- Final weighted score
- Verdict and plagiarism decision
- Best match from database (if any)

---

## Authentication Note

Authentication is optional.  
The system supports anonymous uploads to simplify plagiarism checks while remaining extensible for authenticated users.

---

## Project Status

Backend complete.  
Frontend intentionally kept minimal.  
The system is production-ready at the API level.

---

## Author

Pranit Khandelwal
