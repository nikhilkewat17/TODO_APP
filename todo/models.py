from django.db import models

class Todo(models.Model):
    title=models.CharField(max_length=80)
    complete=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title