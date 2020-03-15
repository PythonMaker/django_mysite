from django.db import models
from datetime import datetime
from django.utils import timezone

# 在我们的调查程序，我们将创建两个模块：需要投票问题与每个问题的选项。每个选项与问题相关联
# 一个问题有两个字段：问题文本和发布日期。一个选项有两个字段：选项的文本和选票数量。


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        verbose_name = verbose_name_plural = '问题'  # 用于将管理界面中被管理的类显示为中文


class Choice(models.Model):
    # 通过设置外键将每个 Choice 对象都关联到一个 Question 对象
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
