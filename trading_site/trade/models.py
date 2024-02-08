from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class MemberUser(models.Model):
    anyUser= models.OneToOneField(User, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)
    email = models.CharField(max_length=70, default='')
    def confirm(self):
        self.confirmed = True
        self.save()
    def __str__(self):
        return self.email

class Post(models.Model):
    TANK = 'TK'
    HEAL = 'HL'
    DEALDAMAGE = 'DD'
    TRADER = 'TD'
    GUILDMASTER = 'GM'
    QUESTGIVER = 'QG'
    BLACKSMITH = 'BS'
    TANNER = 'TR'
    POTIONMAKER = 'PM'
    SPELLMASTER = 'SM'
    CATEGORY_OF_POST = [
        (TANK, 'Танки'),
        (HEAL, 'Хилы'),
        (DEALDAMAGE, 'ДД'),
        (TRADER, 'Торговцы'),
        (GUILDMASTER, 'Гилдмастер'),
        (QUESTGIVER, 'Квестгивер'),
        (BLACKSMITH, 'Кузнец'),
        (TANNER, 'Кожевники'),
        (POTIONMAKER, 'Зельевары'),
        (SPELLMASTER, 'Мастера заклинаний')
    ]
    title = models.CharField(max_length=60, default='Заголовок')
    category = models.CharField(max_length=2, choices=CATEGORY_OF_POST, default=TANK)
    content = RichTextField()
    likes = models.IntegerField(default=0)
    member = models.ForeignKey(MemberUser, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return (self.title)

class Response(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=600, default='None')
    confirmation = models.BooleanField(default=False)
    response_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return (self.content)
    def confirm (self):
        self.confirmation = True
        self.save()