import datetime

from django.db import models
from django_mysql.models import ListCharField
from django.utils import timezone

# class User(models.Model):
#     name = models.CharField(max_length=16)
#     password = models.


class Hakidame(models.Model):
    title = models.CharField(max_length=60)
    detail = models.CharField(max_length=200, blank=True)
    todo = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    bookmark = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    # is_active = models.BooleanField(default=True)
    # deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)


class Tag(models.Model):
    name = models.CharField(max_length=10)
    pub_date = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class HakidameTag(models.Model):
    hakidame_id = models.ForeignKey(Hakidame, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    
