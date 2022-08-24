from argparse import Namespace
from django.contrib import admin
from django.urls import path,include
from enroll import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()
router.register('studentapi',views.StudentModelViewSet,basename='student')
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    # path('gettoken/',obtain_auth_token),
    path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('verifytoken/',TokenVerifyView.as_view(),name='token_verify'),
]
