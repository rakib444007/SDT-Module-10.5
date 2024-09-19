
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.home),
    path('first_project/',include('first_project.urls')),

]
