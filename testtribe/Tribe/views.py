from django.shortcuts import render


def homepage(request):
    return render(request, 'Tribe/homepage.html')


def story(request):
    return render(request, 'Tribe/story.html')