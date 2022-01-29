from email.policy import default
from rest_framework.pagination import CursorPagination

class MyPaginationPage(CursorPagination):
    
    page_size = 3
    ordering  = 'roll'
    cursor_query_param = "cursor"