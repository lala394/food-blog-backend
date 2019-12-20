from django.contrib.auth.models import User
from django.db import models
from djrichtextfield.models import RichTextField

# Create your models here.

class AboutPage (models.Model):
    title = models.CharField(max_length=255, blank=False, null=True)
    description = models.TextField(blank=False, null=True)
    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

class NavLinks(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    url = models.CharField(max_length=20, blank=True)
    active = models.BooleanField(default=True)
    
     # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    subject = models.CharField(max_length=60, blank=False, null=False)
    message = models.TextField(blank=False, null=False)

    #logs
    sent_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

class Story(models.Model):
    title = models.CharField(max_length=50, blank=False, null=True)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='stories', blank=False, null=True)
    description = models.TextField(blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='stories', null=True)

    # logs
    updated_at = models.DateField(auto_now = True)

    def __sts__(self):
        return self.title

    class Meta:
        ordering=('created_at',)
        verbose_name='Story'
        verbose_name_plural='Stories'
        
class Category(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(upload_to='categories', blank=False)

    #logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=('created_at',)
        verbose_name='Category'
        verbose_name_plural='Categories'

class Recipe(models.Model):
    title = models.CharField(max_length=50, blank=False, null=True)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='recipes', blank=False, null=True)
    description = models.TextField(blank=False)
    long_description = RichTextField('Long description')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='recipes', null=True)

    # logs
    updated_at = models.DateField(auto_now = True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=('created_at',)
        verbose_name='Recipe'
        verbose_name_plural='Recipes'

class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField('Comments',)
    recipe = models.ForeignKey(Recipe, related_name='comments', on_delete=models.CASCADE, null=True, blank=True)
    story = models.ForeignKey (Story, related_name='comments', on_delete=models.CASCADE, null=True, blank=True)
    reply_comment = models.ForeignKey('self', related_name = 'reply_comments', on_delete=models.CASCADE, null=True, blank=True)
    #logs
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.user.first_name}  {self.user.last_name}"

    def get_user_full_name(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)
    
    class Meta:
        ordering=('created_at',)
        verbose_name='Comment'
        verbose_name_plural='Comments'
