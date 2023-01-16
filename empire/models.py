from django.db import models
# IMPORTED 
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.
 
class CompanyProfile(models.Model):
    b_name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logo')
    big_logo = models.ImageField(upload_to='logo')
    banner = models.ImageField(upload_to='banner')
    ceo_pix = models.ImageField(upload_to='ceo_pix')
    ceo_name = models.CharField(max_length=50)
    phone_no = models.IntegerField()
    phone_no2 = models.IntegerField()
    favicon = models.ImageField(upload_to='favicon')
    about = models.TextField()
    copyright = models.CharField( max_length=50)

    def __str__(self):
        return self.b_name

    class Meta:
        db_table = 'companyprofile'
        managed = True
        verbose_name = 'CompanyProfile'
        verbose_name_plural = 'CompanyProfiles'

class Categories(models.Model):
    type = models.CharField( max_length=50)
    main = models.CharField( max_length=50, blank=True,null=True)

    def __str__(self):
        return self.type

    class Meta:
        db_table = 'categories'
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
 
   
class Content(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE )
    title = models.CharField(max_length=50, blank=True,null=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField( upload_to='image', blank=True,null=True)
    file = models.FileField(upload_to='file',blank=True,null=True)
    content = models.TextField(blank=True,null=True)
    updated = models.DateTimeField(auto_now=True)
    liked = models.ManyToManyField(User, default=None,blank =True,related_name='liked')

    def __str__(self) :
        return self.content

    class Meta:
        db_table = 'content'
        managed = True
        verbose_name = 'Content'
        verbose_name_plural = 'Content'

    def save(self,*arg,**kwargs):
        self.slug = slugify(self.title)
        super(Content,self).save(arg,kwargs)
    
    def num_likes(self):
        return self.liked.all().count()
    
LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike'),
)

class Like(models.Model):
    user = models.ForeignKey(User,on_delete =models.CASCADE)
    post = models.ForeignKey(Content,on_delete = models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like',max_length = 10)

    def __str__(self):
        return str(self.post)

class Comment(models.Model):
    commenter = models.ForeignKey(User,on_delete = models.CASCADE, related_name = 'comments')
    post = models.ForeignKey(Content, on_delete = models.CASCADE,related_name = 'comments')
    body = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.commenter.username



class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField()
    sent = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
    
    class Meta:
        db_table = 'contact'
        managed = True
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'
