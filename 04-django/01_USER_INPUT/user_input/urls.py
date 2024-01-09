from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('var_routing/', include('var_routing.urls')),
    path('form/', include('form.urls')),
    path('utils/', include('utils.urls')),
]
