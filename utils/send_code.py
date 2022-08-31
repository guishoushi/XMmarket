"""
@email:guishoushi126@126.com
@project:XMmarket
@author:张建行
@file:send_code.PY
@ide:PyCharm
@time:2022-08-18 14:20:06
"""

from unisdk.sms import UniSMS
from unisdk.exception import UniException

# 初始化
client = UniSMS("n6FdddCKrbUiwk4ym9mNmKaoZFFfdHcBFfwf5J5Em5LMNu322",
                'bgQEoYH4HPmdUKZjnCKxP5kMddFGWC')  # 若使用简易验签模式仅传入第一个参数即可


def send_verificationcode(phone,code):


    try:
        # 发送短信
        res = client.send({
            "to": str(phone),
            "signature": "学码科技",
            "templateId": "pub_verif_basic",
            "templateData": {
                "code": code
            }
        })
    except UniException as e:
        print(e)
        return e

