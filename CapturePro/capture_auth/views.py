from django.shortcuts import render

# Create your views here.
def signIn(request):
    return render(request, "Capture_auth/sign-in.html")

def signUp(request):
    return render(request, "Capture_auth/sign-up.html")