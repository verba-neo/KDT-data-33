from django.db import models


# 클래스 생성 => ORM => 테이블 생성

# 클래스 명 => 테이블 명
class Patient(models.Model):
    # 필드명 = 필드 타입
    name =   models.CharField(max_length=30)
    age =    models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    mbti =   models.CharField(max_length=4)

'''
1. 테이블에 대응하는 모델 클래스 생성
2. 컬럼에 대응하는 필드 클래스 변수 생성
3. python manage.py makemigrations <app_name>
4. python manage.py migrate <app_name>

'''