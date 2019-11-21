from django.db import models
from django.contrib.auth.models import User

class Comments(models.Model):
    text = models.TextField()
    comment_name = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'comments_name')
    comment_email = models.EmailField(default='')
    url = models.URLField(blank=True)
    article = models.ForeignKey('entries.Entry', verbose_name='文章', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}: {}'.format(self.comment_name, self.text[:20])

