from email.policy import default
from rest_framework.pagination import LimitOffsetPagination

class MyPaginationPage(LimitOffsetPagination):
    # class names can be of your choice nothing is hardcoded/syntax
    default_limit = 4 #this is syntax
    limit_query_param = 'mylimit' # changes in link /limit=5 ==> /mylimit=5
    offset_query_param = 'myoffset' # changes in link /offset=5 ==> /myofset=5
    max_limit = 6 # defines max page size thar can be set by user