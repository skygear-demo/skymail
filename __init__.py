# Copyright 2017 Oursky Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from .util.skymail import Mailer
import requests
import skygear
from . import settings

def verify_grecaptcha(captcha_value):
    verify_url = "https://www.google.com/recaptcha/api/siteverify"
    r = requests.post(verify_url, data= {
        'secret': settings.config["grecaptcha_secret"],
        'response': captcha_value
        }
      )
    result = r.json()
    print(result['success'])
    return result['success']

@skygear.op('send_invitation_email')
def send_invitation_email(to_email, subject="", custom_message="", grecaptcha=None):

    # Check grecaptcha before sending email
    if settings.config["enable_grecaptcha"]:
        verified = verify_grecaptcha(grecaptcha)
        if not verified:
          return {
            'result': 'Fail',
            'msg': 'captcha incorrect'
          }

    print("Prepare to send")
    sender = settings.config["default_sender"]
    reply_to = settings.config["default_reply_to"]

    subject = subject
    text = custom_message
    html = '<p>'+custom_message+'</p>'

    mailer = Mailer(
      smtp_host=settings.smtp_settings["smtp_host"],
      smtp_port=settings.smtp_settings["smtp_port"],
      smtp_mode=settings.smtp_settings["smtp_mode"],
      smtp_login=settings.smtp_settings["smtp_login"],
      smtp_password=settings.smtp_settings["smtp_password"]
    )
    mailer.send_mail(sender, to_email, subject, text, html=html, reply_to=reply_to)
    print("Email sent")
    return {
      'result': 'OK',
    }
