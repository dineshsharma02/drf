from rest_framework.pagination import PageNumberPagination

class MyPaginationPage(PageNumberPagination):
    # class names can be of your choice nothing is hardcoded/syntax
    page_size = 4 #this is syntax
    page_query_param = 'p' # changes in link
    page_size_query_param ='records' #user can change page size using records param in query
    max_page_size = 7 # defines max page size thar can be set by user
    last_page_strings = 'end' # domain/?page=end provides data of last page 

    #by default this prop is 'last'