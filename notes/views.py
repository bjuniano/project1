from django.shortcuts import render
from .models import Note
from django.http import HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.
def note_list(request):
    allnotes = Note.objects.all()
    resptext = ""
    return render(request, 'notes/index.html', {'notes': allnotes})
    '''
    for note in allnotes:
        url = reverse('notes_details', args = str(note.id))
        resptext += "<a href=" +url + ">"
        resptext += note.title
        resptext += note.content
        
    return HttpResponse(resptext)
'''
def note_detail(request, note_id):
    note = Note.objects.get(id = note_id)
    resptext = ""
    resptext += note.first_name
    return HttpResponse(resptext)
    
def note(request, note_id):
    note = Note.objects.get(id=note_id)
    return render(request, 'notes/note.html', {'note':note})