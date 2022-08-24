from posixpath import basename
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from enroll import views
router = DefaultRouter()
router.register('studentapi',views.StudentModelViewSets,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
