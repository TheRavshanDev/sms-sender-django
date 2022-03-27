from django.db import models
from django.contrib.auth.models import User
from twilio.rest import Client

class User(models.Model):
    name = models.CharField(max_length=100)
    phone = models.PositiveIntegerField()
    address = models.CharField(max_length=150)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.phone is not None:
            account_sid = '#'
            auth_token = '#'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                                        body=f'Hello {self.name}! You are successfully registered in (Your site name)! Go to https://www.ravshanenergy.uz/',
                                        from_='#',
                                        to='#'
                                    )

            print(message.sid)
        return super().save(*args, **kwargs)


