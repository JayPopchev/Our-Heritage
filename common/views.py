from django.shortcuts import render

from artifacts.models import Artifact


# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def dashboard(request):
    artifacts = Artifact.objects.all()

