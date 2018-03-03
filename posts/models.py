from django.utils import timezone
from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=300, blank=False)
    content = models.TextField()
    publish = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    created_at = models.DateField(default=timezone.now())

    def __str__(self):
        return '{} | {}'.format(self.id, self.title)

    class Meta:
        verbose_name_plural = 'posts'
