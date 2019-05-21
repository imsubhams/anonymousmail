from django.db import models


class sendEmailModel(models.Model):
    to = models.CharField(max_length=50, null=True)
    subject = models.CharField(max_length = 100, null=True)
    message = models.CharField(max_length= 500, null = True)
    sent = models.BooleanField(default=False)

    # def __str__(self):
    #     return (self.to, self.subject)