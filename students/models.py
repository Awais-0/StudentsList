from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField("Name", max_length=240)
    email = models.EmailField()
    document = models.CharField("Document", max_length=20)
    phone = models.CharField(max_length=11)
    registration_data = models.DateField("Resgitration Data", auto_now_add=True)

    def __str__(self):
        return self.name