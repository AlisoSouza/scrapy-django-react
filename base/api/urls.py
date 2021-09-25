from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('quotes', views.QuoteViewSet, basename='quotes')
router.register('tags', views.TagViewSet, basename='tags')
router.register('authors', views.AuthorViewSet, basename='authors')

urlpatterns = [
    path('', include(router.urls))
    # path('articles', views.ArticleList.as_view(), name='articles'),
    # path('articles/<int:pk>', views.ArticleDetail.as_view(), name='article_details')
]
