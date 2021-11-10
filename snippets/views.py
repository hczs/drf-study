from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import permissions

from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # 添加permission_classes，做权限控制
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # create()我们的序列化程序的方法现在将传递一个额外的'owner'字段，以及来自请求的验证数据
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # 添加permission_classes，做权限控制，定制化权限，仅允许snippet的owner进行编辑操作(IsOwnerOrReadOnly)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
