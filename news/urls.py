from django.urls import path
from .views import PostList, PostDetail, create_post, PostUpdate, PostDelete, CategoryListView, subscribe

urlpatterns = [
    path('', PostList.as_view()),
    path('post/<int:pk>', PostDetail.as_view()),
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