from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url


urlpatterns = [
    path('packingList/', include('packingList.urls')),
    path('tripPlanner/', include('tripPlanner.urls')),
    path('homePage/', include('homePage.urls')),
    path('admin/', admin.site.urls),
]
