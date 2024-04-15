from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='', blank=True, null=True)
    technologies = models.CharField(max_length=200)

    def __str__(self):
        return self.title
