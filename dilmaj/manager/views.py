from django.shortcuts import render, redirect
from .models import Word
from .forms import WordCreateForm
from django.contrib import messages
from django import forms


# access words database


# Create your views here.
def showHomePage(request):
    return render (request, 'managerHome.html')


# admin add vocabs to our projects
def addWords(request):
    
    if request.method == 'POST':
        print(request.POST)
        form = WordCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Word.objects.create(name = cd['name'], faTranslate = cd['faTranslate'], enTranslate = cd['enTranslate'], voice = cd['voice'], image = cd['image'])
            messages.success(request, cd['name'] + 'is registered' , 'success')
        return redirect ('homePage')
    else:
        form = WordCreateForm()
        return render (request, 'managerAddWords.html',{'form': form})

#admin can visits all words of database    
def showWords(request):
    all = Word.objects.all()

    return render (request, 'managerShowWords.html', {"words": all})

#admin can search a word in database    
def searchWords(request):
    return render (request, 'managerSearchWords.html')

#admin can visits details of a word in database 
def wordsDetail(request, WordId):
    word = Word.objects.get(id = WordId)
    return render (request, 'managerWordsDetails.html', {"word": word})