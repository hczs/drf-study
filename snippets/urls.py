from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views


# Create a router and register our viewsets with it.
# 创建一个router（路由器），并把视图集注册进去
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# 这个API所有的URL由router自动确定
urlpatterns = [
    path('', include(router.urls)),
]
