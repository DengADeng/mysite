from django.db import models
from django.contrib.auth.models import User
from django.utils.html import strip_tags
from django.urls import reverse
from mdeditor.fields import MDTextField
import markdown


# Create your models here.
# Create table entry which contains four columns.

class Category(models.Model):
    name = models.CharField(max_length=50)

    # add class meta
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50,blank=True)

    # add class meta
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Entry(models.Model):
    entry_title = models.CharField(max_length=50)
    entry_text = MDTextField(default="")
    entry_date = models.DateTimeField(auto_now_add= True)
    entry_excerpt = models.CharField(max_length=200, blank=True)
    entry_author = models.ForeignKey(User, on_delete=models.CASCADE)
    ## one to one, many to many
    category = models.ForeignKey(Category, default="", on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, default="", blank=True)

    # add class meta
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.entry_title}'

    def get_absolute_url(self):
        return reverse('entries:entry_detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):

        # 首先实例化一个 Markdown 类，用于渲染 body 的文本。
        # 由于摘要并不需要生成文章目录，所以去掉了目录拓展。
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])

        # 先将 Markdown 文本渲染成 HTML 文本
        # strip_tags 去掉 HTML 文本的全部 HTML 标签
        # 从文本摘取前 54 个字符赋给 excerpt
        self.entry_excerpt = strip_tags(md.convert(self.entry_text))[:54]

        super().save(*args, **kwargs)
