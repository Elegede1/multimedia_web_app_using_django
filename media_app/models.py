from django.db import models

class Media(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='media/')

    def __str__(self):
        return self.name

    @property
    def media_type(self):
        if self.file.name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            return 'image'
        elif self.file.name.lower().endswith(('.mp4', '.webm', 'ogg')):
            return 'video'
        return None
