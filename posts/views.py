from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm
import datetime
from django.db.models import Q

# 주요 소식을 불러오는 함수
def home(request):
    
    posts = Post.objects.all() # '주요'소식으로 수정 필요 (model에 '주요'라는 field를 추가하여...)
    # posts = Post.objects.filter().order_by('-end_date') # 내림차순
    return render(request, 'index.html', {'posts':posts})

def search_list(request):
    # page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    search_posts = Post.objects.all()

    if kw:
        search_posts = search_posts.filter(
            Q(title__icontains=kw) |  # 제목 검색
            Q(body__icontains=kw)   # 내용 검색
            # Q(loc1__icontains=kw) |  # 지역1 검색
        ).distinct()
    # paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    # page_obj = paginator.get_page(page)
    # context = {'question_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'search_list.html', {'kw':kw, 'search_posts':search_posts})

def list_all(request):
    posts = Post.objects.all() # 모든 소식
    return render(request, 'list_all.html', {'posts':posts})

def list_support(request):
    posts = Post.objects.filter(category='지원 정책')
    return render(request, 'list_support.html', {'posts':posts})

def list_product(request):
    posts = Post.objects.filter(category='금융 상품')
    return render(request, 'list_product.html', {'posts':posts})

def list_weekly(request):
    posts = Post.objects.filter(category='주간 소식')
    return render(request, 'list_weekly.html', {'posts':posts})

def search_detail(request):
    posts = Post.objects.all()
    return render(request, 'search_detail.html', {'posts':posts})

# post_id 번째 글을 DB에서 가져와서 detail.html에 띄워주는 함수
def get_post_detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    posts = Post.objects.all()
    return render(request, 'post_detail.html', {'post_detail':post_detail, 'posts':posts})