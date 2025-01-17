from django.db import models

# Create your models here.


class LightStatus(models.Model):
    status = models.BooleanField(default=False)  # True para encendido
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Light is {'on' if self.status else 'off'}"
