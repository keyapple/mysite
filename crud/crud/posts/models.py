from django.db import models

# Create your models here.
# class 객체 지향 선언
# stirng 이라는 종류를 models----이런걸로 장고방식으로
    # 만들어진 시간 now add now 차이는 ? 확인하기
    # ex 계정 생성 시간수정 시간 등

    # primary key 고유 식별 ex 주민번호처럼! 
    
    # 설계한 포스트가 sqlite로
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    


    