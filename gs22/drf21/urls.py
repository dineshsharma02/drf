from unicodedata import name
from django.contrib import admin
from django.urls import path,include
# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('studentapi',views.StudentModelViewset,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework') ),
    path('gettoken/', TokenObtainPairView.as_view(),name="get_token"),
    path('refreshtoken/',TokenRefreshView.as_view(),name="refresh_token"),
    path('verifytoken/',TokenVerifyView.as_view(),name="verify_token"),
    
]
