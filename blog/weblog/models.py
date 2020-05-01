from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
        
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()
    date = models.DateTimeField()
    is_published = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    username = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.username
