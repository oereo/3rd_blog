from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone

# Create your views here.
def home(request):
    blogs = Blog.objects #쿼리셋 = 모델을 오브젝트의 목록을 가져온다고 생각 , 메소드
    return render(request, 'home.html', {'blogs': blogs})
    #return redirect('google.com')

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'details': details})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title'] #ppt에 GET과 POST의 차이 적어두었어요!!!
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()#쿼리 메소드
    return redirect('home')

def edit(request, blog_id):
    blog= get_object_or_404(Blog, pk = blog_id)
    return render(request, 'edit.html', {'blog': blog })

def update(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    blog.title = request.GET['title'] #ppt에 GET과 POST의 차이 적어두었어요!!!
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()#쿼리 메소드
    return redirect('home')

def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    blog.delete() #쿼리 메소드
    return redirect('home')
    
# CRUD의 U인데 edit 수정할 게시글들을 가져오는 부분
# CRUD의 U 수정을 하구 다시 저장하는 부분
# # CRUD의 D 게시글을 삭제하는 부분
