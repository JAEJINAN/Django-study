from django.db import models

# Create your models here.
class Post(models.Model): # 포스트 저장 모델
    title = models.CharField(max_length=30)
    content = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True) # 작성시 자동 시간 저장
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'[{self.pk}]{self.title}'
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    
    # author : 추후 작성 예정
    