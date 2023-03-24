from django.shortcuts import render
import random
def home(request):
    return render(request, 'generator/home.html')
def password(request):

    thepassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    
    if request.GET.get('uppercase'):
        upperChars = list()
        for x in range(len(characters)):
            upperChars.append(characters[x].upper()) 
        characters += upperChars
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    length = int(request.GET.get('length', 12))
    
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')