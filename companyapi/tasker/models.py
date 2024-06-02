from django.db import models

import uuid

class BaseModel(models.Model):
    # UUID is used to create unique ids of records. It is used in place of sequential numbers (AutoField), which makes it safer and prevents direct object access attack
    
    uid = models.UUIDField(primary_key = True, editable = False, default = uuid.uuid4())
    # task_id = models.AutoField(primary_key=True) 

    created_at = models.DateField(auto_now_add = True) # will set the timezone.now() only when the instance is created.
    updated_at = models.DateField(auto_now = True)  # will update the field every time the save method is called.

    class Meta:
        abstract = True # make it an abstract base class


class Task(BaseModel):
    task_title = models.CharField(max_length = 100)
    task_desc =  models.CharField(max_length = 400)
    is_done = models.BooleanField(default = False)

    def __str__(self):
        return self.task_title


class TimingTask(BaseModel):
    task = models.ForeignKey(Task, on_delete = models.CASCADE)
    timing = models.DateField()


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name