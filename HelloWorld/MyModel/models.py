# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


class DLight(models.Model):
    c_id = models.IntegerField(db_column='C_ID', primary_key=True)  # Field name made lowercase.
    c_house_id = models.IntegerField(db_column='C_HOUSE_ID')  # Field name made lowercase.
    c_device_id = models.IntegerField(db_column='C_DEVICE_ID')  # Field name made lowercase.
    c_switch = models.IntegerField(db_column='C_SWITCH', blank=True, null=True)  # Field name made lowercase.
    c_create_time = models.DateTimeField(db_column='C_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'd_light'


class TDevice(models.Model):
    c_id = models.AutoField(db_column='C_ID', primary_key=True)  # Field name made lowercase.
    c_code = models.CharField(db_column='C_CODE', max_length=20)  # Field name made lowercase.
    c_name = models.CharField(db_column='C_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_house_id = models.IntegerField(db_column='C_HOUSE_ID')  # Field name made lowercase.
    c_terminal_id = models.IntegerField(db_column='C_TERMINAL_ID')  # Field name made lowercase.
    c_problem = models.IntegerField(db_column='C_PROBLEM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_device'


class TDeviceAttr(models.Model):
    c_id = models.AutoField(db_column='C_ID', primary_key=True)  # Field name made lowercase.
    c_code = models.CharField(db_column='C_CODE', max_length=20)  # Field name made lowercase.
    c_name = models.CharField(db_column='C_NAME', max_length=50)  # Field name made lowercase.
    c_house_id = models.IntegerField(db_column='C_HOUSE_ID')  # Field name made lowercase.
    c_terminal_id = models.IntegerField(db_column='C_TERMINAL_ID')  # Field name made lowercase.
    c_device_id = models.IntegerField(db_column='C_DEVICE_ID')  # Field name made lowercase.
    c_use = models.IntegerField(db_column='C_USE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_device_attr'


class THouse(models.Model):
    c_id = models.IntegerField(db_column='C_ID', primary_key=True)  # Field name made lowercase.
    c_name = models.CharField(db_column='C_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_location = models.CharField(db_column='C_LOCATION', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_house'


class TLog(models.Model):
    c_id = models.AutoField(db_column='C_ID', primary_key=True)  # Field name made lowercase.
    c_log = models.TextField(db_column='C_LOG', blank=True, null=True)  # Field name made lowercase.
    c_create_time = models.DateTimeField(db_column='C_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_log'


class TTerminal(models.Model):
    c_id = models.AutoField(db_column='C_ID', primary_key=True)  # Field name made lowercase.
    c_code = models.CharField(db_column='C_CODE', max_length=20)  # Field name made lowercase.
    c_house_id = models.IntegerField(db_column='C_HOUSE_ID')  # Field name made lowercase.
    c_online = models.IntegerField(db_column='C_ONLINE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_terminal'


class TUser(models.Model):
    c_id = models.AutoField(db_column='C_ID', primary_key=True)  # Field name made lowercase.
    c_account = models.CharField(db_column='C_ACCOUNT', max_length=20)  # Field name made lowercase.
    c_password = models.CharField(db_column='C_PASSWORD', max_length=20)  # Field name made lowercase.
    c_name = models.CharField(db_column='C_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    c_create_time = models.DateTimeField(db_column='C_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_user'


class TUserHouse(models.Model):
    c_id = models.AutoField(db_column='C_ID', primary_key=True)  # Field name made lowercase.
    c_user_id = models.IntegerField(db_column='C_USER_ID')  # Field name made lowercase.
    c_house_id = models.IntegerField(db_column='C_HOUSE_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_user_house'
