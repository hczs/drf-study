import django_filters

from snippets.models import Snippet


class SnippetFilter(django_filters.rest_framework.FilterSet):
    """
    Snippet过滤器，创建时间区间查询，title模糊查询
    """
    # 创建时间区间查询
    s_time = django_filters.DateTimeFilter(field_name='created', lookup_expr='gte')
    e_time = django_filters.DateTimeFilter(field_name='created', lookup_expr='lte')
    # title模糊查询
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Snippet
        fields = ['s_time', 'e_time', 'title']
