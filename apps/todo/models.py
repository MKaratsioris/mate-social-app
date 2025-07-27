from django.db import models
from django.contrib.auth.models import User

class TodoList(models.Model):
    id = models.AutoField(primary_key=True)
    manage = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task = models.CharField(max_length=50)
    is_done = models.BooleanField(default=False)
    
    class Meta:
        ordering=['id']

    def __str__(self) -> str:
        return f"{self.id}| {self.task}"