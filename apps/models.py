import uuid

from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, ForeignKey, CASCADE, IntegerField, DateTimeField, TextField, ImageField
from django.utils.translation import gettext_lazy as _

# class Tag(Model):
#     name = CharField(max_length=255)


# class Blog(Model):
#     title = CharField(max_length=255)
#     description = TextField()
#     created_at = DateTimeField(auto_now_add=True)
#     author = ForeignKey('auth.User', CASCADE)
#     tag = ManyToManyField('apps.Tag', blank=True)
#     photo = ImageField(upload_to='blog/')


# class Category(Model):
#     name = CharField(max_length=255, verbose_name=_("Name"))
#
#     class Meta:
#         verbose_name = _('category')
#         verbose_name_plural = _('categories')


#
#
# class User(AbstractUser):
#     image = ImageField(upload_to='user/')
#
#
# class Blog(Model):
#     first_name = CharField(max_length=255)
#     last_name = CharField(max_length=255)
#     category = ForeignKey('apps.Category', CASCADE)
#     user = ForeignKey('apps.User', CASCADE)
#     image = ImageField(upload_to='blog/')
#     title = CharField(max_length=255)
#     description = TextField()
#     created_at = DateTimeField(auto_now_add=True)
#     uuid = UUIDField(default=uuid.uuid4, primary_key=True)

#
# class Product(Model):
#     name = CharField(max_length=255, verbose_name=_("Name"))
#     image = ImageField(upload_to='product/', verbose_name=_("Image"))
#     price = IntegerField(verbose_name=_("Price"))
#     # category = ManyToManyField('apps.Category', blank=True)
#     description = TextField()
#     # user = ForeignKey('auth.User', CASCADE)
#     # type = ForeignKey('apps.Type', CASCADE)
#     # color = ForeignKey('apps.Color', CASCADE)
#     # brand = ForeignKey('apps.Brand', CASCADE)
#     created_at = DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
#
#     class Meta:
#         verbose_name = _('product')
#         verbose_name_plural = _('products')

# class Position(Model):
#     name = CharField(max_length=50)
#
#
# class Contact(Model):
#     name = CharField(max_length=50)
#     email = CharField(max_length=255)
#     position = ForeignKey('apps.Position', CASCADE)
#     project = IntegerField()

# class Job(Model):
#     name = CharField(max_length=255)
#
#
# class Country(Model):
#     name = CharField(max_length=255)
#
#
# class Company(Model):
#     name = CharField(max_length=255)
#
#
# class Category(Model):
#     name = CharField(max_length=255)
#
#
# class Candidate(Model):
#     name = CharField(max_length=255)
#     price = IntegerField()
#     job = ForeignKey('apps.Job', CASCADE)
#     country = ForeignKey('apps.Country', CASCADE)
#     company = ManyToManyField('apps.Company')
#     category = ManyToManyField('apps.Category')


# class Basemodel(Model):
#     updated_at = DateTimeField(auto_now=True)
#     created_at = DateTimeField(auto_now_add=True)
#
#     class Meta:
#         abstract = True
#
#
# class Category(Model):
#     name = CharField(max_length=255)
#
#
# class Product(Basemodel):
#     title = CharField(max_length=255)
#     description = TextField(null=True, blank=True)
#     price = DecimalField(max_digits=10, decimal_places=2)
#     category = ForeignKey('apps.Category')

# import uuid
#
# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.db.models import SET_NULL
# from django.utils.translation import gettext_lazy as _
# from django_ckeditor_5.fields import CKEditor5Field
#
#
# # Create your models here.
#
# class Blog(models.Model):
#     id = models.UUIDField(default=uuid.uuid4, primary_key=True)
#     name = models.CharField(max_length=200)
#     owner = models.CharField(max_length=200)
#     comment_count = models.IntegerField()
#     created_at = models.DateField(auto_now_add=True)
#     description = CKEditor5Field('Text', config_name='extends')
#     image = models.ImageField(upload_to='blog/images/')
#     category = models.ForeignKey('apps.Category', SET_NULL, null=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=200, null=True, blank=True)
#
#     class Meta:
#         verbose_name = 'Category'
#         verbose_name_plural = 'Categories'
#
#     def __str__(self):
#         return self.name
#
#
# # ------------------------------------ email verification --------------------------------------------
# class CustomUser(AbstractUser):
#     email_confirmed = models.BooleanField(default=False)
#     activation_link_used = models.BooleanField(default=False)
#
#
# # -----------------JSONFIELD------------------------------------
# class Product(models.Model):
#     name = models.CharField(max_length=200)
#     price = models.FloatField()
#     image = models.ImageField(upload_to='products/%Y/%m', null=True)
#     description = models.TextField(null=True, blank=True)
#     info = models.JSONField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True, editable=False)
#
#     class Meta:
#         verbose_name = _('product')
#         verbose_name_plural = _('products')


class Work(Model):
    name = CharField(max_length=255)


class Profile(Model):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    address = CharField(max_length=255)
    work = ForeignKey('apps.Work', CASCADE)



'''
django i18n

LANGUAGES(
    ()
    ()

)

LOCALE_PATHS = [BASE_DIR / 'locale']

verbose_name = _('products')
gettext_lazy as _
i18n_patterns (urls.py)
'''