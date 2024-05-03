from django.shortcuts import render, redirect
from Tribe.models import Notes, Resources


def tribe_village(request):
    stats = Resources.objects.all()
    return render(request, 'Tribe/tribe_village.html', {'stats': stats})


def story(request):
    stats = Resources.objects.all()
    return render(request, 'Tribe/story.html', {'stats': stats})


def workshops(request):
    stats = Resources.objects.all()
    return render(request, 'Tribe/workshops.html', {'stats': stats})

def jungle(request):
    stats = Resources.objects.all()
    return render(request, 'Tribe/jungle.html', {'stats': stats})

def my_notes(request):
    stats = Resources.objects.all()
    if request.method == 'POST':
        my_text = request.POST.get('item_text')
        entry = Notes()
        entry.text = my_text
        entry.save()
        return redirect(request.path)

    existing_notes = Notes.objects.all()
    return render(request, 'Tribe/my_notes.html', {'existing_notes': existing_notes, 'stats': stats})
