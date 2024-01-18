from django.db import models

# 두 테이블의 연결테이블이 오직 FK 두개만 가지고 있는 경우
class Lecture(models.Model):
    title = models.CharField(max_length=200)


class Student(models.Model):
    name = models.CharField(max_length=200)
    lectures = models.ManyToManyField(Lecture, related_name='students')
    

'''
# models.py에 변경이 있다 => 무조건 makemigrations

# related_name을 설정하지 않으면(default) 
l2.student_set

# related_name을 설정하면, 
l2.students

# s1 학생이 l1 수업을 수강한다.
s1.lectures.add(l1)

# l2 수업에 s3 학생이 들어왔다.
l2.students.add(s3)

# l3 수업을 듣는 모든 학생들을 보여줘
l3.students.all()

# s1 이 듣는 모든 수업을 보여줘
s1.lectures.all()

# l3 수강생들중 s4를 뺀다.
l3.students.remove(s4)

# s1 이 l2를 취소한다.
s1.lectures.remove(l2)

'''