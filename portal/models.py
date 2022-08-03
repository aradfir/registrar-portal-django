from django.db import models


# Create your models here.
class Course(models.Model):
    department = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    course_number = models.IntegerField()
    professor_name = models.CharField(max_length=150)
    start_time = models.TimeField()
    end_time = models.TimeField()
    group = models.IntegerField()
    DAYS_OF_WEEK = (
        (0, 'Saturday'),
        (1, 'Sunday'),
        (2, 'Monday'),
        (3, 'Tuesday'),
        (4, 'Wednesday'),
    )

    day_1 = models.IntegerField(choices=DAYS_OF_WEEK, null=False)
    day_2 = models.IntegerField(choices=DAYS_OF_WEEK, null=True)
