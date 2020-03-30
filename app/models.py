from django.db import models
from django.db.models import CharField,DateField,ForeignKey,IntegerField
from django.contrib.auth.models import User

# Create your models here.
BALANCE_TYPE = ((u'收入',u'收入'),(u'支出',u'支出'))

class Category(models.Model):
    category = CharField(max_length=20)
    user     = ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        # 在後台管理介面時，將各個目錄名稱直接顯示出來
        return self.category
        

class Record(models.Model):
    date         = DateField()
    description  = CharField(max_length=300)
    category     = ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    cash         = IntegerField()
    balance_type = CharField(max_length=2, choices=BALANCE_TYPE)
    user         = ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        # 在後台管理介面時，以 description 作為每筆 Record 的名稱
        return self.description