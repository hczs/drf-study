from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework import viewsets

from snippets.filter import SnippetFilter
from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly, MyDjangoModelPermissions
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
    # 有这个model权限的人才可以操作
    permission_classes = [permissions.DjangoModelPermissions,
                          IsOwnerOrReadOnly]

    # 过滤器相关使用
    # 过滤器，简单的基于相等的过滤，在这里设置上哪个字段，哪个字段就会进行精确查询
    # filterset_fields = ['title', 'code']

    # 模糊查询搜索，在url后添加search参数，将会自动搜索title中符合条件的数据返回，模糊查询，但不是根据字段，而是根据search设置的字段
    # 按需注册到backends中，要想既提供搜索，又提供精确过滤/模糊过滤，就需要注册两个filter，
    # 这里的优先级最高，这里要是注册了filter_backends，就以这里的为准，setting中的就无效了
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['title']

    # 自定义一个过滤器类，指定过滤的逻辑
    filter_class = SnippetFilter

    # 请注意，我们还使用@action装饰器创建了一个名为 的自定义操作highlight。这个装饰可以用来添加不符合标准的任何自定义端点create/ update/delete风格。
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    # create()我们的序列化程序的方法现在将传递一个额外的'owner'字段，以及来自请求的验证数据
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
