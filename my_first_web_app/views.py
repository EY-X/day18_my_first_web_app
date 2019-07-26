from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from random import randint

def home_page(request):
    context = {'name': 'Betty Maker'}
    response = render(request, 'index.html', context)
    return HttpResponse(response)
    
def root(request): 
    return HttpResponseRedirect('home')

def gallery(request):
    image_urls = []
    for i in range(5):
        random_number = randint(0,100)
        image_urls.append("https://picsum.photos/400/600/?image={}".format(random_number))
    context = {'gallery_image': image_urls}
    response = render(request, 'gallery.html', context)
    return HttpResponse(response)
    

def about_me(request):
    my_dict = {
        'skills': ['Guitar player', 'Developer', 'Athlete'],
        'interests': ['music', 'basketball', 'computers']
    }
    response = render(request, 'about_me.html', my_dict)
    return HttpResponse(response)


def favourites(request):
    context = {'fave_links': ['https://www.peteranswers.com']}
    response = render(request, 'favourite_links.html', context)
    return HttpResponse(response)

def gallery_red(request):
    return HttpResponseRedirect('portfolio')