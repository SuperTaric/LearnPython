from django.contrib import admin

# Register your models here.
from myblog.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title",)

admin.site.register(Article, ArticleAdmin)