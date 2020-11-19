from django.shortcuts import render,HttpResponse
from blog.models import Blog
import math


# Create your views here.
def home(request):
    return render(request,"index.html")
def blog(request):
    no_of_posts = 3
    page = request.GET.get('page')
    if page is None:
        page=1
    else:
        page=int(page)
    print(page)
    blogs= Blog.objects.all()
    length=len(blogs)
    blogs=blogs[(page-1)*no_of_posts:page*no_of_posts]
    if page>1:
        prev=page-1
    else:
        prev=None
    if page<math.ceil(length/no_of_posts):
        nxt=page+1
    else:
        nxt=None
    print(prev,nxt)
    context={'blogs':blogs,'prev':prev,'nxt':nxt}
    return render(request,"bloghome.html",context)
def contact(request):
    return render(request,"contact.html")
def blogpost(request,slug):
    return HttpResponse(f"you are viewing {slug}")
def search(request):
    return render(request,"search.html")
