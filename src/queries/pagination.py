from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        previousPage = 0;
        if self.page.has_previous():
            previousPage = self.page.previous_page_number()

        return Response({
            'pagination': {
                'count': self.page.paginator.count,
                'previousPage': previousPage,
                'currentPage': self.page.number,
                'nextPage': self.page.next_page_number(),
                'lastPage': self.page.paginator.num_pages
            },
            'results': data
        })
