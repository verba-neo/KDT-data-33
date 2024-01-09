from django.urls import path
from . import views


urlpatterns = [
    # /utils/bmi_in/
    path('bmi_in/', views.bmi_in),
    # /utils/bmi_out/
    path('bmi_out/', views.bmi_out),

]
