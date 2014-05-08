from django.shortcuts import render

from .models import Entry
# Create your views here.

def home(request):
    data = {}
    data['varvalue'] = 25.33
    data['entries'] = Entry.objects.all()
    # templates are located in templates-folder
    return render(request, 'blog/index.djhtml', data)
