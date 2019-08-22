from django.db import models

# Create your models here.

# 1. python manage.py makemigrations => django한테 model작성했음을 알림
# 2. python manage.py migrate => django한테 실제 DB에 작성하라고 명령

class Article(models.Model):
    # id(pk)는 기본적으로 처음 테이블 생성시 자동으로 만들어진다.
    # id = models.AutoField(primary_key=True)

    # 모든 필드는 기본적으로 NOT NULL ==> 비어있으면 안된다.

    # CharField 에서는 max_length가 필수 인자
    title = models.CharField(max_length=20)
    content = models.TextField() # 클래스 변수 (DB의 필드)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번 글 - {self.title} : {self.content}'
