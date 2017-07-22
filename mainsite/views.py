from django.shortcuts import render

# Create your views here.

def base(request):
       return render(request, 'base.html')
       
def aboutus(request):
       return render(request, 'About_us.html')
       
def ourteam(request):
       return render(request, 'Our_team.html')