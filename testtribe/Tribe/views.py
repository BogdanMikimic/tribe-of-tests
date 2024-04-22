from django.shortcuts import render


def homepage(request):
    return render(request, 'Tribe/homepage.html')


def img_credits(request):
    return render(request, 'Tribe/credits.html')