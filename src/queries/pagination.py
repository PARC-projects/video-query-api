from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'previousPage': self.page.previous_page_number(),
            'currentPage': self.page.number,
            'nextPage': self.page.next_page_number(),
            'count': self.page.paginator.count,
            'lastPage': self.page.paginator.count,
            'results': data
        })
