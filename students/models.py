from django.db import models

# Create your models here.


class Student(models.Model):
    section_choice = (
        ('A', 'SectionA'),
        ('B', 'SectionB'),
    )
    roll_no = models.IntegerField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    full_name = models.CharField(max_length=200)
    course = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    section = models.CharField(choices=section_choice, max_length=1)

    # in admin panel will use full_name field to display Student objects
    def __str__(self):
        return self.full_name
