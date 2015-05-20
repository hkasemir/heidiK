from django.db import models


class MainContent(models.Model):
    header = models.CharField(max_length = 200)
    content = models.TextField()
    page = models.CharField(max_length = 20, default="index")
    
    def __str__(self):
        return self.header
    
    
    