from django.shortcuts import render, redirect
import requests
from django.conf import settings
from django.http import JsonResponse
import logging

def signIn(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        api_url = "http://127.0.0.1:8000/api/signin/"
        response = requests.post(
            api_url, json={"username": username, "password": password})

        if response.status_code == 200:
            data = response.json()
            request.session['access_token'] = data.get('access')
            return redirect('/home/')
        else:
            return render(request, "capture_auth/sign-in.html", {"error": "Invalid credentials."})

    return render(request, "capture_auth/sign-in.html")


def signUp(request):
    return render(request, "capture_auth/sign-up.html")


def adminDashboard(request):
    return render(request, "admin_agency/admin-dashboard.html")


def userCrud(request):
    return render(request, "admin_agency/crud-user.html")

# Logger setup
logger = logging.getLogger(__name__)

def home(request):
    videos = [] 
    if request.method == 'GET':
        api_url = "http://127.0.0.1:8000/api/getrecordings/"
        headers = {
            'Authorization': f'Bearer {request.session.get("access_token")}',
            'X-CSRFToken': request.META.get('CSRF_COOKIE'),
        }

        response = requests.get(api_url, headers=headers)

        logger.info(f"GET {api_url} - Status Code: {response.status_code}")
        if response.status_code == 200:
            videos = response.json() 
            logger.info(f"Videos retrieved: {videos}")
        else:
            logger.error(f"Failed to retrieve videos: {response.json()}")

    if request.method == 'POST':
        # Check if there are videos before allowing upload
        if not videos:  # If videos list is empty, do not allow upload
            return render(request, "employee/employee-dashboard.html", {"error": "No videos available to upload."})

        api_url = "http://127.0.0.1:8000/api/recordings/"
        title = request.POST.get('title')
        video_file = request.FILES.get('video')
        headers = {
            'Authorization': f'Bearer {request.session.get("access_token")}',
            'X-CSRFToken': request.META.get('CSRF_COOKIE'),
        }

        files = {'video': video_file}
        data = {'title': title}

        response = requests.post(api_url, headers=headers, data=data, files=files)

        if response.status_code == 201:
            logger.info("Video uploaded successfully.")
            # After successful upload, fetch the updated list of videos
            return render(request, "employee/employee-dashboard.html", {"success": "Video uploaded successfully!"})
        else:
            logger.error(f"Upload failed: {response.json()}")
            return render(request, "employee/employee-dashboard.html", {"error": response.json().get("error", "Upload failed.")})

    return render(request, "employee/employee-dashboard.html", {"videos": videos})


def subscription(request):
    return render(request, "admin_agency/subscription.html")
