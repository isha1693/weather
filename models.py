from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(150)])
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=100)

def __str__(self):
        return self.name

class Address(models.Model):
    person = models.ForeignKey(Person,  related_name='addresses', on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)

def __str__(self):
        return f"{self.street}, {self.state} {self.zipcode} "
