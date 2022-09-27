from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.db.models import Q
from django.contrib import auth # 유저 확인
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


# 주요 소식을 불러오는 함수
def home(request):
    posts = Post.objects.all()
    if request.user.is_authenticated:
        user_kw1 = request.user.keyword1
        user_kw2 = request.user.keyword2
        print(user_kw1)
        print(user_kw2)
        posts = posts.filter(
                    Q(title__icontains=user_kw1) |
                    Q(body__icontains=user_kw1)  |
                    Q(subhead__icontains=user_kw1)|
                    Q(title__icontains=user_kw2) |
                    Q(body__icontains=user_kw2)  |
                    Q(subhead__icontains=user_kw2)
            ).distinct()
    # sort = request.GET.get('sort', '')
    # if sort == 'date':
    #     posts = Post.objects.filter().order_by('-end_date') # 내림차순
    # else:
    #     posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})

def search_list(request):

    # page = request.GET.get('page', '1')  # 페이지
    print("requests.GET.get : ", request.GET.get)
    kw = request.GET.get('kw', None)  # 검색어
    # kw_tag = request.GET.get('kw_tag', None)
    kw_age = request.GET.get('kw_age', None)
    kw_target = request.GET.get('kw_target', None)
    print("kw_target : ", kw_target)
    income = request.GET.get('income', None)
    categories = request.GET.get('categories', None)
    kw_loc = request.GET.get('kw_loc', None)
    kw_loc0 = request.GET.get('kw_loc0', None)
    print("kw_loc0 : ", kw_loc0)
    print("kw_loc : ", kw_loc)
    print("kw_target : ", kw_target)


    search_posts = Post.objects.filter().order_by('-count') # 조회순 정렬
    # age = request.GET.getlist('age', None)
    # loc = request.GET.getlist('loc', None)
    # category = request.GET.getlist('category', None)

    if kw_age:
        search_posts = search_posts.filter(
            Q(min_age__lte=kw_age) |
            Q(max_age__gte=kw_age)
        ).distinct()

    if kw_loc0 == "전체":
        pass
    else:
        if kw_loc == "전체":
            pass
        else:
            search_posts = search_posts.filter(
                    loc2=kw_loc
                )
    if kw:
        search_posts = search_posts.filter(
                Q(title__icontains=kw) |  # 제목 검색
                Q(body__icontains=kw)  |
                Q(subhead__icontains=kw)  # 내용 검색
        ).distinct()

    if income:
        search_posts = search_posts.filter(
            Q(income__icontains=income)
            # Q(income=None)
        ).distinct()

    print("카테고리 전 search_posts :", search_posts)
    if categories:
        categories = categories.replace("+", "").strip()
        print("categories : ", categories)
        search_posts = search_posts.filter(category=categories).distinct()

        print("카테고리 후 search_posts :", search_posts)

    if kw_target:
        print("target 전 : ", kw_target)
        search_posts = search_posts.filter(
            Q(target__icontains=kw_target)
        ).distinct()
    print(search_posts.query)
    print("target 후 search_posts : ", search_posts)
    if len(search_posts) > 0:
        exist_posts = True
    else:
        exist_posts = False

    context = {
        "kw":kw,
        "kw_age":kw_age,
        "exist_posts":exist_posts,
        "search_posts":search_posts
    }
    return render(request, 'search_list.html', context=context)

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
    posts = Post.objects.filter().order_by('body')
    return render(request, 'search_detail.html', {'posts':posts})

# post_id 번째 글을 DB에서 가져와서 detail.html에 띄워주는 함수
def get_post_detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    post_title = post_detail.title
    title_list = post_title.split()
    print("제목리스트 :", title_list)
    q = Q()
    for word in title_list:
        q.add(Q(title__icontains=word), q.OR)
        print(q)
    relevant_posts = Post.objects.all()
    # print("relevent_post 목록 : ", relevant_posts)
    relevant_posts = relevant_posts.filter(q)
    # print("relevent_post 목록2 : ", relevant_posts)
    return render(request, 'post_detail.html', {'post_detail':post_detail, 'relevant_posts':relevant_posts})