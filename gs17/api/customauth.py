from rest_framework.permissions import BasePermission

class MyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method=="GET" or request.method=="POST":
            # Setting a permission to let this api only be used when method is get or post else not.
            return True
        return False