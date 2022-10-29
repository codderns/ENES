from django.apps import AppConfig

#appss.py uygulamamızın ismini gösteren (article) bir dosyamızdır.
class ArticleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'article'
