from django.db import models


class List(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)


class Item(models.Model):
    ACTIVE = 1
    DONE = 2
    DELETED = 3
    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (DONE, 'Done'),
        (DELETED, 'Deleted')
    )

    list = models.ForeignKey(List)
    name = models.CharField(max_length=255)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=ACTIVE)
    created = models.DateTimeField(auto_now_add=True)
