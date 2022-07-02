from django.shortcuts import render
from .models import Review
# Create your views here.

# def ReviewView(request):
#     print("here")
#     return render(request, 'Review.html')



def ApppintmentReviews(request):
    return render(request, 'ApppintmentReviews.html')