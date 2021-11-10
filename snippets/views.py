from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework import viewsets

from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    这个视图集自动提供了查询所有和查询一个的方法
    一个UserViewSet就做了之前users和userDetail两个类的活了
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    """
    这个类自动提供list、create、retrieve、update、destroy方法
    Additionally we also provide an extra `highlight` action.
    此外，还会提供额外的highlight操作
    这一个类，做了之前SnippetHighlight、SnippetList、SnippetDetail三个类做的活了
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    # 添加permission_classes，做权限控制，定制化权限，仅允许snippet的owner进行编辑操作(IsOwnerOrReadOnly)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    # 请注意，我们还使用@action装饰器创建了一个名为 的自定义操作highlight。这个装饰可以用来添加不符合标准的任何自定义端点create/ update/delete风格。
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    # create()我们的序列化程序的方法现在将传递一个额外的'owner'字段，以及来自请求的验证数据
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
