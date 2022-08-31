from django.shortcuts import render, HttpResponse
from django.views import View
from utils.send_code import send_verificationcode
from market.models import User, VerificationCode
from market.forms import UserForm
import random


# Create your views here.

class Index(View):
    def get(self, request):
        return render(request, template_name='market/index.html')


class Verification(View):
    def get(self, request):
        phonenum = request.GET.get('phoneNumber')
        code = ''.join([str(i) for i in random.choices(range(0, 10), k=6)])
        print(code, phonenum)
        send_verificationcode(phonenum, code)
        VerificationCode.objects.update_or_create(code=code, phone_number=phonenum)
        return HttpResponse('验证码已发送，请注意查收')

    def post(self, request):
        code = request.POST.get('code')
        phonenum = request.POST.get('phoneNumber')

        if not VerificationCode.objects.filter(phone_number=phonenum, code=code).first():
            return HttpResponse('验证码错误！')

        form = UserForm(data=request.POST)
        if form.is_valid():
            if not User.objects.filter(phoneNumber=form.cleaned_data['phoneNumber']).first():
                form.save()
                return HttpResponse('抢购成功！')

        return HttpResponse('抢购成功！')
