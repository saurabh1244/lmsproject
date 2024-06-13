from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings
import secrets
import datetime


# Define your choices as lists of tuples with string keys
framework_choices = [
    ('1', 'Django'),
    ('2', 'React'),
    ('3', 'Express'),
    ('4', 'Spring Boot'),
    ('5', 'Flask'),
    ('6', 'FastAPI'),
    ('7', 'Django REST framework'),
    ('8', 'Vue.js'),
    ('9', 'Angular'),
    ('10', 'Laravel')
]

programming_language_choices = [
    ('1', 'Python'),
    ('2', 'JavaScript'),
    ('3', 'Java'),
    ('4', 'C#'),
    ('5', 'Ruby'),
    ('6', 'PHP'),
    ('7', 'Go'),
    ('8', 'Swift'),
    ('9', 'Kotlin'),
    ('10', 'TypeScript')
]

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = ("email")
    REQUIRED_FIELDS = ["username"]

    # def __str__(self):
    #     return self.email
    

class OtpToken(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE,related_name="otps")
    otp_code = models.CharField(max_length=6 , default=secrets.token_hex(3))
    tp_created_At = models.DateTimeField(auto_now_add=True)
    otp_expires_at  = models.DateTimeField(blank=True , null=True)
    print("--------------------------")
    print(f"tp_created_At === {tp_created_At}")
    print(f"otp_expires_at === {otp_expires_at}")

    def __str__(self):
        return self.user.username
    




class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, default=0,decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=100 , blank=True , null=True , default='')
    image = models.ImageField(upload_to='uploads/product/')
    file = models.FileField(null=True)
    

   

    frameworks = models.CharField(max_length=50 ,choices=framework_choices)
    programming_language = models.CharField(max_length=50 ,choices=programming_language_choices)
    date_modified = models.DateTimeField(auto_now=True)

    course_content = models.TextField()
    requirements = models.TextField()
    screenshot1 = models.ImageField(upload_to='uploads/product/', null=True , blank=True)
    screenshot2 = models.ImageField(upload_to='uploads/product/',null=True, blank=True)
    screenshot3 = models.ImageField(upload_to='uploads/product/',null=True, blank=True)
    screenshot4 = models.ImageField(upload_to='uploads/product/',null=True, blank=True)

    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=6, default=0, decimal_places=2)

    def __str__(self):
        return self.name
    



class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(get_user_model() , on_delete=models.CASCADE)
    date = models.DateField(default=datetime.datetime.today)
    stats = models.BooleanField(default=False)







