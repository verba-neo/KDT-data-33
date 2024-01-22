from django.db import models

# Create your models here.
class KakaoRestaurant(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    score = models.FloatField(default=0)
    score_count = models.IntegerField(default=0)
    review_count = models.IntegerField(default=0)
    address = models.CharField(max_length=200)
    detail_url = models.URLField()

    class Meta:
        db_table = 'kakao_restaurants'
        db_table_comment = '카카오 맵 selenium 스크래핑으로 저장한 데이터'
        # ordering 지정시) restaurants = KakaoRestaurant.objects.all()  => ORDER BY score desc, score_count desc
        ordering = ['-score', '-score_count']  
