"""
@email:guishoushi126@126.com
@project:XMmarket
@author:张建行
@file:urls.PY
@ide:PyCharm
@time:2022-08-17 14:18:03
"""
from django.contrib import admin
from django.urls import path, include
from market import views

app_name = 'market'
urlpatterns = [
    path('', views.Index.as_view(), name='market'),
    path('verificationCode', views.Verification.as_view(), name='verificationCode')

]
