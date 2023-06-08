from django.shortcuts import render
from .models import * 
from .forms import *

def index(request):
    ad = news.objects.order_by('-time_create')[:10]
    print(request.user)
    context = { 'ad' : ad }
    return render(request,'index.html', context = context)

def news_info(request,pk):
    news_search = news.objects.filter(pk = pk)
    context = { 'ad' : news_search }
    return render(request,"news.html", context = context)

def new(request):
    form = CreateNewNews()
    if request.method == 'POST':
        form = CreateNewNews(request.POST)
        if request.user.is_authenticated and form.is_valid:
            post = form.save(commit=False)
            post.author = request.user
            post.save()

    context = { 'form': form }
    return render(request,"add.html", context = context)