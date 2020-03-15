from django.contrib import admin
from .models import Question

admin.site.register(Question)  # 告诉管理员为这个 Question 对象创建一个管理界面
