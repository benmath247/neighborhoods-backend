from django.db import models
from django.contrib.auth.models import Group
from ckeditor.fields import RichTextField
from PIL import Image

class Committee(models.Model):
    name = models.CharField(max_length=200)
    neighborhood = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class BoardMember(models.Model):
    neighborhood = models.ForeignKey(Group, on_delete=models.CASCADE)
    committee = models.ManyToManyField(Committee)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=300, null=True, blank=True)
    email = models.CharField(max_length=300, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

# Neighborhood associations all have board minutes that they often upload as a file.
# They could also make it just text/HTML
class BoardMinutes(models.Model):
    neighborhood = models.ForeignKey(Group, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    content = RichTextField()
    file = models.FileField(upload_to='board_minutes/', null=True, blank=True)

    def __str__(self):
        return self.neighborhood.name+"-"+str(self.date)
    
    class Meta:
        verbose_name_plural = "Board Minutes"
    
# Blogs 1 and 2 will each have categories. Each neighborhood has their own set of categories
class Blog1Category(models.Model):
    neighborhood = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Blog (Type 1) Categories"


class Blog2Category(models.Model):
    neighborhood = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Blog (Type 2) Categories"


# Every neighborhood can have their own 2 sets of blogs
class Blog1(models.Model):
    neighborhood = models.ForeignKey(Group, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=300, null=True, blank=True)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Blog1Category, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Blogs (Type 1)"

class Blog2(models.Model):
    neighborhood = models.ForeignKey(Group, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=300, null=True, blank=True)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Blog2Category, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Blogs (Type 2)"
    