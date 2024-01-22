from django.contrib import admin
from .models import KakaoRestaurant


class KakaoRestaurantAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'score', 'category',]
    list_display_links = ['id', 'name']


admin.site.register(KakaoRestaurant, KakaoRestaurantAdmin)


# 추가 어드민 등록
# class AnotherClassAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(AnotherClass, AnotherClassAdmin)
    

