# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Board1(models.Model):
    num = models.IntegerField(primary_key=True)
    writer = models.CharField(max_length=30, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=20, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.CharField(max_length=2000, blank=True, null=True)
    file1 = models.CharField(max_length=200, blank=True, null=True)
    boardid = models.CharField(max_length=2, blank=True, null=True)
    regdate = models.DateTimeField(blank=True, null=True)
    readcnt = models.IntegerField(blank=True, null=True)
    grp = models.IntegerField(blank=True, null=True)
    grplevel = models.IntegerField(blank=True, null=True)
    grpstep = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'board1'

