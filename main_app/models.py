# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DAddress(models.Model):
    address_id = models.CharField(primary_key=True, max_length=20)
    user = models.ForeignKey('DUser', models.DO_NOTHING, blank=True, null=True)
    address_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'd_address'


class DUser(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20)
    username = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'd_user'
