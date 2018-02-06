from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        previous_page = None;
        if self.page.has_previous():
            previous_page = self.page.previous_page_number()

        nextPage = None;
        if self.page.has_next():
            nextPage = self.page.next_page_number()

        return Response({
            'pagination': {
                'count': self.page.paginator.count,
                'previousPage': previous_page,
                'currentPage': self.page.number,
                'nextPage': nextPage,
                'lastPage': self.page.paginator.num_pages
            },
            'results': data
        })
