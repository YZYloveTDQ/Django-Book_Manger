from django.db import models

# Create your models here.
class BookInfo(models.Model):
    """图书模型"""
    book_title = models.CharField(max_length=20) # 图书名
    book_date = models.DateField() # 图书出版日期
    #b_title = models.CharField(max_length=20, db_column='title') # 通过db_column指定bittle对应的表格中字段名称为title
    #b_pubDate = models.DateField() # 发布日期
    #b_read = models.IntegerField(default=0) # 阅读量，起始默认0
    #b_comment = models.IntegerField(default=0)# 评论量
    #is_delete = models.BooleanField(default=False) # 逻辑删除

    def __str__(self):
        return self.book_title

class People(models.Model):
    """人物模型"""
    name = models.CharField(max_length=20)
    age = models.IntegerField() # 整数类型

    # 设置BookInfo的一个外键字段，on_delete避免两个表里的数据不一致,django2.0之后都要写
    # cascade级联，一遍删除另一边也自动删除
    # related_name创建反向连接
    people_book = models.ForeignKey('BookInfo', on_delete=models.CASCADE, related_name='book_peoples')

    #p_gender = models.BooleanField(default=True) # 性别
    #is_delete = models.BooleanField(default=False) # 逻辑删除
    #p_comment = models.CharField(max_length=200, null=True, blank=False) # 人物评论对应数据库中的字段可以为空，但通过后台管理系统添加内容时，输入框不能空

    def __str__(self):
        return self.name


"""多对多模型"""
class TypeInfo(models.Model):
    type_name = models.CharField(max_length=20) # 新闻类别

class NewsInfo(models.Model):
    news_title = models.CharField(max_length=20) # 新闻标题
    news_content = models.TextField()# 新闻内容
    news_pubDate = models.DateField(auto_now_add=True) # 发布时间
    news_type = models.ManyToManyField("TypeInfo", related_name="news_type") # 一个新闻可以有很多类别

"""自关联的表结构"""
class AreaInfo(models.Model):
    area_title = models.CharField(max_length=30) # 名称
    area_parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE) # 关系