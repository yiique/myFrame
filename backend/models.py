from __future__ import unicode_literals

from django.db import models

# Create your models here.


class MySideBar(models.Model):
    id = models.AutoField(primary_key=True)
    entry_name = models.CharField(max_length=200)


class MyTags(models.Model):
    id = models.AutoField(primary_key=True)
    first_level = models.CharField(max_length=200)
    second_level = models.CharField(max_length=200, null=True)  # separated with first level with "|"


class MyPapers(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.CharField(max_length=100, default="0000-00-00")
    name = models.CharField(max_length=500)
    authors = models.CharField(max_length=200)
    institutions = models.CharField(max_length=200)
    abstract = models.TextField()
    notes = models.TextField()
    state = models.IntegerField(default=2)          # 0 already known; 1 to be reread; 2 to be implemented
    tag = models.TextField(default=None, null=True)


class MyNotes(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.CharField(max_length=100)
    name = models.CharField(max_length=500)
    type = models.IntegerField(default=0)           # 0 book;   1 note
    content = models.TextField()
    state = models.IntegerField(default=2)          # 0 already done; 1 to be modified; 2 to be rewrite
    tag = models.TextField(default=2)
