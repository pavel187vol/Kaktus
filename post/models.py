from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Tag(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['slug',]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
            return reverse('post:tag_detail',
                            args=[self.slug])

class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts',
                               on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, related_name='posts')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    body = models.TextField()
    image = models.ImageField(upload_to='products/%Y/%m/%D',
                              blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
            return reverse('post:post_detail',
                            args=[self.id, self.slug])
