from random import randint
from django.core.mail import send_mail
from .models import EmailOTP
from django.conf import settings

def send_otp(user):
    otp = str(randint(100000,999999)) # 6 digit otp
    EmailOTP.objects.update_or_create(user=user,defaults={'otp':otp, 'is_verified':False})

    try:
        send_mail(
            'Your OTP verification code',
            f'hello {user.username}, your OTP is {otp}',
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False
        )
        print(f"✅ OTP sent to {user.email}: {otp}")
    except Exception as e:
        print(f"❌ OTP send failed: {e}")

