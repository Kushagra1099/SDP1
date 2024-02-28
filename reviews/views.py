from django.shortcuts import render

def review_list(request):
    if request.method =='GET':
        reviews = TouristReview.objects.all()
        return render(request, 'reviewpage.html' )
