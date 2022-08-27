from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/single_pages/{self.pk}/'

class Comment(models.Model):
    question = models.CharField(null=True, max_length=50)
    content=models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.question},{self.content}'

    def get_absolute_url(self):
        return f'/list/#comment-{self.pk}'


class Information(models.Model):
    name = models.CharField(null=True, max_length=10)
    email = models.EmailField(null=True, max_length=30)
    instagram = models.URLField(null=True)
    mbti = models.CharField(null=True, max_length=7)

    def __str__(self):
        return f'[Update{self.pk}] Information'
