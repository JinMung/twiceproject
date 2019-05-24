from django.db import models

class Twice(models.Model):
    Nationality_Choice=(
        ('KR','한국'),
        ('JP','일본'),
        ('TW','대만'),
    )

    name = models.CharField(max_length=20,default='홍길동')
    age = models.IntegerField()
    birth = models.DateTimeField('date published') 
    nationality = models.CharField(max_length=200, choices=Nationality_Choice)
    position = models.TextField(max_length=20)

    def __str__(self):
        return self.name
# Create your models here.
