from django.db import models
from django.urls import reverse

# Create your models here.
class Customer(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=45)
    customer_name = models.CharField(max_length=45)
    license_id = models.IntegerField()
    join_date = models.DateField(blank=True, null=True)
    site_name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'Customer'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("tpl_manage:customer_detail", args=(self.customer_id, ))


class LicenseTable(models.Model):
    license_id = models.IntegerField(primary_key=True)
    subscript_period = models.IntegerField(blank=True, null=True)
    customer_ids = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'license_table'

class Sites(models.Model):
    site_id = models.AutoField(primary_key=True)
    customer_id = models.CharField(max_length=45, blank=True, null=True)
    root_url = models.CharField(db_column='root_URL', max_length=45, blank=True, null=True)  # Field name made lowercase.
    server_env = models.CharField(max_length=45, blank=True, null=True)
    framework = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sites'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("tpl_manage:customer_tpl_detail", args=(self.customer_id, self.site_id))


class Templates(models.Model):
    tpl_id = models.AutoField(primary_key=True)
    customer_id = models.CharField(max_length=45, blank=True, null=True)
    site_id = models.IntegerField(blank=True, null=True)
    permissions = models.CharField(max_length=45, blank=True, null=True)
    module_id = models.CharField(max_length=45, blank=True, null=True)
    tpl_url = models.CharField(db_column='tpl_URL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tpl_path = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        verbose_name = 'tpl'
        verbose_name_plural = 'tpls'
        managed = False
        db_table = 'templates'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    customer_id = models.CharField(max_length=45, blank=True, null=True)
    site_id = models.IntegerField(blank=True, null=True)
    u_name = models.CharField(max_length=45, blank=True, null=True)
    u_passwd = models.CharField(max_length=45, blank=True, null=True)
    permission_lvl = models.IntegerField(blank=True, null=True)

