from django.shortcuts import render

def frontpage(request):
    return render(request, 'coming_soon/frontpage.html')