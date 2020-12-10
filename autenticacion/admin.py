from django.contrib import admin
from pages.models import Categoria, Post
# from cv_crud.models import CV

# Register your models here.
admin.site.register([Categoria, Post])
