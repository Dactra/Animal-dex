from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Animal, Dog, Cat, Bird

# Create your views here.

def index(request):
    animals = Animal.objects.order_by('name')[:75]
    context = {'animals': animals, 'page_title': 'All Animals', 'type': 'all'}
    return render(request, 'animals/index.html', context)

def detail(request, animal):
    context = {'animal': animal, 'animal_dict': animal.display()}
    return render(request, 'animals/detail.html', context)

def cats(request):
    animals = Cat.objects.order_by('name')[:75]
    context = {'animals': animals, 'page_title': 'Cats', 'type': 'cats'}
    return render(request, 'animals/index.html', context)

def dogs(request):
    animals = Dog.objects.order_by('name')[:75]
    context = {'animals': animals, 'page_title': 'Dogs', 'type': 'dogs'}
    return render(request, 'animals/index.html', context)

def birds(request):
    animals = Bird.objects.order_by('name')[:75]
    context = {'animals': animals, 'page_title': 'Birds', 'type': 'birds'}
    return render(request, 'animals/index.html', context)

def cat_detail(request, slug):
    try:
        animal = Cat.objects.get(slug=slug)
    except Cat.DoesNotExist:
        return HttpResponseRedirect('/animals/') # Should probably be 404

    return detail(request, animal)

def dog_detail(request, slug):
    try:
        animal = Dog.objects.get(slug=slug)
    except Dog.DoesNotExist:
        return HttpResponseRedirect('/animals/') # Should probably be 404

    return detail(request, animal)

def bird_detail(request, slug):
    try:
        animal = Bird.objects.get(slug=slug)
    except Bird.DoesNotExist:
        return HttpResponseRedirect('/animals/') # Should probably be 404

    return detail(request, animal)

def search(request):
    search_term = request.GET['q']
    type = request.GET['type']

    if search_term == '':   #if no search term, redirect to animal index page
        return HttpResponseRedirect('/animals/' + type)
    else:   #if search term exists, show search results
        search_title = "Search " + type + " for '" + search_term + "'"
        page_title = type

        # search by animal type
        if type == 'all':
            animals = Animal.objects.filter(name__icontains=search_term).order_by('name')  #icontains=case-insensitive
        elif type == 'cats': 
            animals = Cat.objects.filter(name__icontains=search_term).order_by('name')
        elif type == 'dogs':
            animals = Dog.objects.filter(name__icontains=search_term).order_by('name')
        elif type == 'birds':
            animals = Bird.objects.filter(name__icontains=search_term).order_by('name')
        else:
            animals = None
        
        context = {'animals': animals, 'search_term': search_term, 'search_title': search_title, 'type': type}
        return render(request, 'animals/index.html', context)
