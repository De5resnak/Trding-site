from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import MemberUser
from django.core.mail import send_mail
from .models import Response

User = get_user_model()

@receiver(post_save, sender=User)
def create_member_user(sender, instance, created, **kwargs):
    if created:
        MemberUser.objects.create(anyUser=instance)

@receiver(post_save, sender=User)
def save_member_user(sender, instance, **kwargs):
    instance.memberuser.save()

@receiver(post_save, sender=Response)
def send_response_notification(sender, instance, created, **kwargs):
    if created:
        post_owner_email = instance.post.member.email  # Получаем email владельца поста
        subject = 'Новый отклик на ваш пост'
        message = f'Здравствуйте!\n\nНа ваш пост поступил новый отклик. Проверьте его на сайте.'
        send_mail(subject, message, None, [post_owner_email])

@receiver(post_save, sender=Response)
def send_response_notification(sender, instance, created, **kwargs):
    if not created and instance.confirmation:
        response_owner_email = instance.sender.email
        subject = 'Ваш отклик принят'
        message = 'Здравствуйте!\n\nВаш отклик был принят.'
        send_mail(subject, message, None, [response_owner_email])