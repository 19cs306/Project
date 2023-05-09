from django.shortcuts import render

from django.http import HttpResponse

def main(request):
    title = 'My Projects'
    proj1 = '/media/word.png'
    proj2 = '/media/Covid.png'
    proj3 = '/media/NewsSelect.png'
    return render(request, "main.html", {'title':title,'proj1': proj1,'proj2': proj2,'proj3': proj3})