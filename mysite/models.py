# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class LocationCode(models.Model):
    loc_code = models.CharField(primary_key=True, max_length=5)
    location = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location_code'


class Realestate(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    price = models.CharField(max_length=20, blank=True, null=True)
    fnd_year = models.CharField(max_length=20, blank=True, null=True)
    sold_date = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=20, blank=True, null=True)
    loc_num = models.CharField(max_length=20, blank=True, null=True)
    loc_cd = models.CharField(max_length=20, blank=True, null=True)
    floor = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'realestate'


class RealestateIconPath(models.Model):
    estate_type = models.IntegerField(blank=True, null=True)
    img_path = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'realestate_icon_path'


class Realnews(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    newspaper_tit = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'realnews'


class SmallHouseRealestate(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=20, blank=True, null=True)
    price_deposit = models.CharField(max_length=20, blank=True, null=True)
    price_monthly = models.CharField(max_length=20, blank=True, null=True)
    fnd_year = models.CharField(max_length=20, blank=True, null=True)
    sold_date = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=20, blank=True, null=True)
    loc_num = models.CharField(max_length=20, blank=True, null=True)
    loc_cd = models.CharField(max_length=20, blank=True, null=True)
    floor = models.CharField(max_length=20, blank=True, null=True)
    area_average = models.CharField(max_length=20, blank=True, null=True)
    buy_type = models.CharField(max_length=20, blank=True, null=True)
    bldg_type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'small_house_realestate'


class SmallHouseRealnews(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    newspaper = models.CharField(max_length=20, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    wr_date = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'small_house_realnews'


class TransIconPath(models.Model):
    trans_type = models.IntegerField(blank=True, null=True)
    img_path = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trans_icon_path'
