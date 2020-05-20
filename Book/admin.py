from django.contrib import admin

# Register your models here.
from Book.models import BookInfo


class BookInfoAdmin(admin.ModelAdmin):
    """自定义管理页面"""
    list_display = ['id', 'book_title', 'book_date']

# 必须要放在一起注册，因为BookInfoAdmin类中没有模型，不符合Django模型注册规则
admin.site.register(BookInfo, BookInfoAdmin) 