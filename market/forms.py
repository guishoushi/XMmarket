"""
@email:guishoushi126@126.com
@project:XMmarket
@author:张建行
@file:forms.PY
@ide:PyCharm
@time:2022-08-18 22:55:50
"""
from django.forms import ModelForm
from market.models import *


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('id', 'name', 'phoneNumber', 'grade')
