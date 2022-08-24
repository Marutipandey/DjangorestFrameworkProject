from rest_framework.pagination import PageNumberPagination
class myPageNumberPagination(PageNumberPagination):
    page_size = 3
    # page_query_param = 'p'
    # page_size_query_param = 'records'
    # max_page_size = 3
    last_page_strings = 'end'