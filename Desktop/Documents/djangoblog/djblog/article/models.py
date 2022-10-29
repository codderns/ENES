from django.db import models

# Create your models here.
# uyglamamıza has tabloları models içinde yazmak lazım. modelleri admin panelinde göstermek istiyorsak bu modelleri register yani kayıt etmek gereklidir.

class Article(models.Model): #article'ı models klasından türetmeliyiz.
    author = models.ForeignKey("auth.User", on_delete = models.CASCADE, verbose_name = "Yazar") # auth.user tablosuna atıfta, işarette bulunduk. zaten fonksiyon adı foreignKey yani başka bir tablodaki şeyi al.
    # o user silinince o user'a ait bilgiler, tablolar da silinecek "on_delete" parametresi iş görür.
       #verbose_name admin panelinde author yerine yazar şeklinde göreceğiz giriş kayıt için
    title = models.CharField(max_length = 80, verbose_name = "Başlık")
    content = models.TextField(verbose_name = "İçerik")
    created_Date = models.DateTimeField(auto_now_add = True)

# bu article'ı admin panele göstermek için kayıt etmek lazım. admin kısmında ya