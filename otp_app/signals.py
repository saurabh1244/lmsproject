from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from .models import OtpToken
from django.core.mail import send_mail
from django.utils import timezone


@receiver(post_save , sender=settings.AUTH_USER_MODEL)
def create_token(sender , instance , created , **kwargs):
    if created:
        if instance.is_superuser:
            pass

        else:
            OtpToken.objects.create(user=instance,otp_expires_at=timezone.now() + timezone.timedelta(minutes=5) )
            instance.is_active = False
            instance.save()

            otp = OtpToken.objects.filter(user=instance).last()
            print("----------------------------")
            print(f"otp === {otp}")



            subject = "Email Verification"

            message = f""" 

          Hii {instance.username},, here is your OTP {otp.otp_code}  and
          it expire in 5 mintunes
          http://127.0.0.1:8000/verify-email/{instance.username}
                       

                           """
            sender = "sstcdurg@gmail.com"
            receiver = [instance.email,]

            send_mail(
            subject,
            message,
            sender,
            receiver,
            fail_silently=False
                  )