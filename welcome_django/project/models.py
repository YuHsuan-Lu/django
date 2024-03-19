from django.db import models
from account.models import User
import uuid
# # Create your models here.

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)#not required
    created_by = models.ForeignKey(User,related_name = 'projects',on_delete=models.CASCADE)#pass in User object
    
    def __str__(self):
        return self.name