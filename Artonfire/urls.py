
from django.contrib import admin
from django.urls import path,include
from art_gallery import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('art_gallery.urls'))
]
