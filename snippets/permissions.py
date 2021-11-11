from rest_framework import permissions
from rest_framework.permissions import DjangoModelPermissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    定制化权限管理，仅仅允许实例的owner字段所属user进行编辑操作
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user


# 重写权限码code，暂不使用
class MyDjangoModelPermissions(DjangoModelPermissions):
    perms_map = {
        'GET': [],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.添加%(model_name)s'],
        'PUT': ['%(app_label)s.修改%(model_name)s'],
        'PATCH': ['%(app_label)s.修改%(model_name)s'],
        'DELETE': ['%(app_label)s.删除%(model_name)s'],
    }
