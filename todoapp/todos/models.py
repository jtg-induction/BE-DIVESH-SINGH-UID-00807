from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import smart_str as smart_unicode
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.utils import timezone


class Todo(models.Model):
    """
    Needed fields
    - user (fk to User Model - Use AUTH_USER_MODEL from django.conf.settings)
    - name (max_length=1000)
    - done (boolean with default been false)
    - date_created (with default of creation time)
    - date_completed (set it when done is marked true)

    Add string representation for this model with todos name.
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    done = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
    date_completed = models.DateTimeField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if self.pk:
            current_instance = type(self).objects.get(pk=self.pk)
            if self.done and not current_instance.done:
                self.date_completed = timezone.now()
            elif not self.done:
                self.date_completed = None

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    