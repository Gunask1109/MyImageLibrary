from django.http import HttpResponse
from django.shortcuts import render,redirect
from myapp.models import *
from django.contrib import messages

def show_about_page(request):
    name ="Gunasekar"
    phone = "9876543345"
    content ={'name':name, 'phone':phone}
    return render(request, 'about.html',content)
def show_home_page(request):
    cats = Category.objects.all()
    images = Image.objects.all()
    data ={'images': images,'cats': cats}
    return render(request, 'index.html', data)
def show_category_page(request, cid):
    cats = Category.objects.all()
    category = Category.objects.get(pk=cid)
    images = Image.objects.filter(cat=category)
    data ={'images': images,'cats': cats}
    return render(request, 'index.html', data)
def home(request):
    return redirect('/home')


def search(request):
    search_term = ''
    if 'query' in request.GET:
        search_term = request.GET['query']
        images1 = Image.objects.all().filter(title__icontains=search_term)
        images2 = Image.objects.all().filter(description__icontains=search_term)
        images = images1.union(images2)
    if images.count() == 0:
            messages.warning(request, 'No search result found, Please refine your query')

    cats = Category.objects.all()

    data = {'images': images, 'search_term': search_term, 'cats': cats}
    return render(request, 'search.html', data)
