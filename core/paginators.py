from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

import math

DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = 6

class CategoryPaginator(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = DEFAULT_PAGE_SIZE
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'previous': self.get_previous_link(),
                'next': self.get_next_link()
            },
            'total_results': self.page.paginator.count,
            'total_pages': math.ceil(self.page.paginator.count / int(self.request.GET.get('page_size', self.page_size))),
            'current_page': int(self.request.GET.get('page', DEFAULT_PAGE)),
            'page_size': int(self.request.GET.get('page_size', self.page_size)),
            'results': data
        })