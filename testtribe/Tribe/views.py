from django.shortcuts import render, redirect
from Tribe.models import Notes


def tribe_village(request):
    return render(request, 'Tribe/tribe_village.html')


def story(request):
    return render(request, 'Tribe/story.html')


def workshops(request):
    return render(request, 'Tribe/workshops.html')

def jungle(request):
    return render(request, 'Tribe/jungle.html')

def my_notes(request):
    method='GET'
    if request.method == 'POST':
        my_text = request.POST.get('item_text')
        entry = Notes()
        entry.text = my_text
        entry.save()
        return redirect(request.path)

    existing_notes = Notes.objects.all()
    return render(request, 'Tribe/my_notes.html', {'existing_notes': existing_notes, 'method': method})
