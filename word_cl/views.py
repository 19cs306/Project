from django.shortcuts import render, redirect
import os
from django.conf import settings
from .forms import MyModelForm

import sys
sys.path.insert(1, 'Programs')
from Proj_wc import word_c

def handle_uploaded_file(f):
    ext = os.path.splitext(f.name)[1]
    filename = 'file' + os.path.splitext(f.name)[1]  # get the original file extension
    with open(os.path.join(settings.MEDIA_ROOT, filename), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    if ext == '.docx':
        word_c.process_docx("media/file.docx")
    elif ext == '.txt':
        word_c.process_text("media/file.txt")
    return filename
    
def my_view(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST, request.FILES)
        fname = request.FILES['file']
        ext = os.path.splitext(fname.name)[1]
        if form.is_valid():
            uploaded_file = handle_uploaded_file(request.FILES['file'])
            my_model = form.save(commit=False)
            my_model.file = uploaded_file
            my_model.save()
            tag_title = "Wordcloud for the file" + str(fname) + " is:"
            img = "media/word.png"
            id = 'cloud'
            tag = "File "+ str(fname)+ " Uploaded"
            return render(request, 'cloud.html', {'tag': tag,"img" : img, 'id': id, "tag_title":tag_title})
        else:
            tag = "Invalid File Type !!!"
            return render(request, 'cloud.html', {'tag': tag})
    else:
        form = MyModelForm()
    title = 'WordCloud'
    return render(request, 'cloud.html', {'title':title,'form': form} )


