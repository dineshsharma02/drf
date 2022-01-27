from rest_framework.throttling import UserRateThrottle

class NewThrottle(UserRateThrottle):
    scope = "updated"   # this takes input from django settings.py rest_framework dict