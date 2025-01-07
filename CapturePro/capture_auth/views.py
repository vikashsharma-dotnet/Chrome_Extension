from django.shortcuts import render, redirect
import requests
from django.conf import settings
from django.http import JsonResponse
from .api_views import VideoRecordingView

def signIn(request):
    if request.method == "POST":
        # Get the username and password from the form
        username = request.POST.get('username')
        password = request.POST.get('password')

        # API URL for sign-in
        api_url = "http://127.0.0.1:8000/api/signin/"  # The API endpoint for login

        # Send a POST request to the API
        response = requests.post(
            api_url,
            json={"username": username, "password": password},  # Send the credentials as JSON
        )

        if response.status_code == 200:
            # Parse the response JSON to get the tokens
            response_data = response.json()
            access_token = response_data.get("access")
            refresh_token = response_data.get("refresh")

            # Store the tokens in the session
            request.session['access_token'] = access_token
            request.session['refresh_token'] = refresh_token

            # Redirect to the home page after successful login
            return redirect('/home/')
        else:
            # If credentials are invalid, render the login page with an error message
            return render(request, "capture_auth/sign-in.html", {"error": "Invalid credentials."})

    # For GET requests, just render the sign-in page
    return render(request, "capture_auth/sign-in.html")

def signUp(request):
    return render(request, "capture_auth/sign-up.html")

def adminDashboard(request):
    return render(request, "admin_agency/admin-dashboard.html")

def userCrud(request):
    return render(request, "admin_agency/crud-user.html")

def home(request):
    if request.method == 'POST':
        # Call the VideoRecordingView's post method to handle the upload
        video_view = VideoRecordingView.as_view()
        return video_view(request)

    return render(request, "employee/employee-dashboard.html")

def subscription(request):
    return render(request, "admin_agency/subscription.html")

def some_view(request):
    access_token = request.session.get('access_token')
    if access_token:
        # Use the token for authenticated requests
        # For example, you can include it in headers for another API call
        headers = {
            'Authorization': f'Bearer {access_token}',
        }
        # Make an API call using the token
        response = requests.get('http://127.0.0.1:8000/api/protected/', headers=headers)
        # Handle the response as needed
    else:
        # Handle the case where the token is not available
        return redirect('/login/')  # Redirect to login if not authenticated
