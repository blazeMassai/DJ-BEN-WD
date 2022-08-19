# from reviews.admin import admin_site
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reviews.urls'))
]
