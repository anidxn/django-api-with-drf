from django.db import models

import uuid

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key = True, editable = False, default = uuid.uuid4())
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