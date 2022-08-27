from django.db import models
import os

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    head_image = models.ImageField(upload_to='diary/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='diary/files/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/diary/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)
    
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]



class Guest(models.Model):
    author = models.CharField(null=True,max_length=20)
    content=models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)
    sticker=models.CharField(null=True, max_length=100)

    def __str__(self):
        return f'{self.author},{self.content}'

    def get_absolute_url(self):
        return f'/diary/guest_book/#guest-{self.pk}'
