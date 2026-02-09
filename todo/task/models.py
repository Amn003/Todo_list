from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    TASK_TYPE =[
        ("once","Once"),
        ("daily","Daily"),
        ("weekly","Weekly"),
        ("monthly","Monthly"),
        ("yearly","Yearly"),
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True,null=True)
    task_type=models.CharField(max_length=100,choices=TASK_TYPE)

    created_at=models.DateTimeField( auto_now=False, auto_now_add=False)
    is_active=models.BooleanField(default=True)
    is_deleted=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}-{self.title}"



class TaskComp(models.Model):
    task=models.ForeignKey(Task,on_delete=models.CASCADE)
    complete_on=models.DateField()

    class Meta:
        unique_together=("task","complete_on")
        
    def __str__(self):
        return f"{self.task.title}--{self.complete_on} "