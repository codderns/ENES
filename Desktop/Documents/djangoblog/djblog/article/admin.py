from django.contrib import admin
from .models import Article #article'ı aldık. 
# Register your models here.
#app'i django'ya belirtmek lazım.

#admin paneline kayıt
admin.site.register(Article)