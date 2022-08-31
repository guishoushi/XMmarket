from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField('姓名', max_length=10)
    phoneNumber = models.CharField('手机号码', max_length=11)
    grade = models.CharField('所属年级', max_length=10)
    add_date = models.DateTimeField('添加时间', auto_now_add=True)

    class Meta:
        verbose_name = '市场信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class VerificationCode(models.Model):
    code = models.CharField('验证码', max_length=6)
    phone_number = models.CharField(verbose_name='所属号码', max_length=11)
    add_date = models.DateTimeField('添加时间', auto_now_add=True)

    class Meta:
        verbose_name = '验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
