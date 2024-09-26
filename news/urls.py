from django.urls import path
from django.views.decorators.cache import cache_page

from .views import PostList, PostDetail, create_post, PostUpdate, PostDelete, CategoryListView, subscribe

urlpatterns = [
    path('', cache_page(60)(PostList.as_view())),
    path('post/<int:pk>', cache_page(60 * 5)(PostDetail.as_view())),
    path('post/search/', PostList.as_view(), name='post_search'),
    path('news/create/', create_post, name='news_create'),
    path('articles/create/', create_post, name='articles_create'),
    path('news/<int:pk>/edit/', PostUpdate.as_view(), name='news_edit'),
    path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='articles_edit'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='articles_delete'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
]
