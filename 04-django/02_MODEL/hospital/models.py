from django.db import models


# models.py의 존재 이유 => 클래스 생성 => ORM => 테이블 생성

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


# 아래 코드는 예시 코드를 기록으로 남겨놓은것.

# 현재의 파일(02_MODEL/hospital/models.py)이 
# 직접 실행($ python models.py)된 경우에만 아래 조건문 블럭
if __name__ == '__main__':
    # DB patient 테이블 조작

# Create (생성)
    # 레코드 한줄 만들기
    p1 = Patient()
    # 컬럼 채우기
    p1.name = '김환자'
    p1.age = 20
    p1.weight = 67.3
    p1.height = 175.2
    p1.mbti = 'ISTJ'
    # 실제 DB에 반영
    p1.save()

    p2 = Patient(name='이환자', age=23, weight=52.3, height=162.0, mbti='ESTP')
    p2.save()

    p3 = Patient.objects.create(name='박환자', age=29, weight=68.0, height=171.4, mbti='INFP')

    p4 = Patient()
    p4.name = '유환자'
    p4.age = 32
    p4.weight = 57.2
    p4.height = 163.1
    p4.mbti = 'ISTJ'
    p4.save()


# Read 전체 조회
    Patient.objects.all()
    # 전체 환자의 나이 => 몸무게만 print 해보려면?
    for patient in Patient.objects.all():
        print(patient.age, patient.weight)

# Read 단일 조회
    p2 = Patient.objects.get(name='이환자')
    print(p2.name, p2.age, p2.weight, p2.height)
    
    p3 = Patient.objects.get(id=3)
    p3 = Patient.objects.get(pk=3)

# # Read 조건 조회 (무시)
    # # 나이가 25 이상인 사람들 (Greater Than or Equal)
    # Patient.objects.filter(age__gte=25)
    # # 키가 170보다 작은 사람들 (Less Than)
    # Patient.objects.filter(height__lt=170)

    
# Update 수정
    # 한명을 고르고
    p1 = Patient.objects.get(pk=1)
    # 수정하고
    p1.age = 40
    p1.weight += 10
    # 저장한다
    p1.save()

# Delete 삭제
    # 한명을 고르고
    p4 = Patient.objects.get(pk=4)
    # 삭제한다 (save 없이 바로 반영)
    p4.delete()


# C => R => U => D
    Patient.objects.create(name='최환자', age=45, weight=68.0, height=171.4, mbti='INFP')
    
    patients = Patient.objects.all()
    p5 = Patient.objects.get(pk=5)

    # p5 = Patient.objects.get(pk=5)
    p5.age += 1
    p5.mbti = 'ISTJ'
    p5.weight += 3
    p5.save()

    # p5 = Patient.objects.get(pk=5)
    p5.delete()


    for i in range(10):
        import random
        mbtis = ['ISTP', 'ENFJ', 'INTP', 'ESTJ']
        age = random.choice(range(10, 100))
        weight = random.choice(range(30, 100))
        height = random.choice(range(150, 200))
        mbti = random.choice(mbtis)
        Patient.objects.create(name='샘플환자', age=age, weight=weight, height=height, mbti=mbti)



