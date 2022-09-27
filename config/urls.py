from django.contrib import admin
from django.urls import path, include
from posts import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('search-list/', views.search_list, name="search-list"),
    path('list-all/', views.list_all, name='list-all'),
    path('list-support/', views.list_support, name='list-support'),
    path('list-product/', views.list_product, name='list-product'),
    path('list-weekly/', views.list_weekly, name='list-weekly'),

    path('search-detail/', views.search_detail, name='search-detail'),
    path('post-detail/<int:post_id>', views.get_post_detail, name='post-detail'),

    path('accounts/', include('accounts.urls')),
]

# 미디어 파일 접근 url
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)