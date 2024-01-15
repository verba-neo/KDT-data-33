from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    country = models.CharField(max_length=50)
    # Product (N) 을 부르고 싶다면?
    # product_set 을 통해 조회. [N]_set


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    # company_id = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


if __name__ == '__main__':
    Company.objects.create(
        name='삼성전자',
        year=1969,
        country='KR'
    )
    Company.objects.create(
        name='LG전자',
        year=1958,
        country='KR'
    )

    c1 = Company.objects.get(pk=1)
    c2 = Company.objects.get(pk=2)

    p1 = Product()
    p1.name = 'Galaxy z flip 5'
    p1.price = 1263000
    # FK 정수를 직접 입력 => 가능은 하지만 권장하지 않음
    p1.company_id = 1
    p1.save()

    p2 = Product()
    p2.name = 'Gram Pro 360'
    p2.price = 2222700
    # 1:N 관계의 객체를 할당
    p2.company = c2
    p2.save()

    Product.objects.create(
        name='시그니처 OLED M',
        price=45800000,
        company=c2
    )
    Product.objects.create(
        name='디오스 오브제컬렉션',
        price=5380000,
        company=c2
    )
    Product.objects.create(
        name='갤럭시 북4 울트라',
        price=3210000,
        company=c1
    )
    Product.objects.create(
        name='Neo QLED 8K',
        price=49900000,
        company=c1
    )

# 1:N 에서 1이 소유한 N들을 부르는 방법
    c1 = Company.obects.get(pk=1)
    c1.product_set.all()
    for p in c1.product_set.all():
        print(p.name, p.price)
    
# 1:N 에서 N이 소속된 1을 부르는 방법
    p1 = Product.objects.get(pk=1)
    p1.company

    # p1의 제조사의 창립년도는?
    p1.company.year

    # '디오스 오브제컬렉션'의 제조사의 국적은?
    p = Product.objects.get(name='디오스 오브제컬렉션')
    p.company.country


    # Gram Pro 360 을 만든 회사의 제품을 모두 가져오려면?
    Product.objects.get(name='Gram Pro 360').company.product_set.all()


    # Neo QLED 8K 제품을 만든 회사의 국적과 같은 국적을 가진 회사를 모두 찾아달라
    p = Product.objects.get(name='Neo QLED 8K')
    Company.objects.filter(country=p.company.country)

    

