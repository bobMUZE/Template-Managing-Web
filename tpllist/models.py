from django.db import models
from django.urls import reverse
from tpllist.modules import og_tag

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
        return reverse("tpl_manage:customer_main", args=(self.customer_id, ))

    def get_info_url(self):
        return reverse("tpl_manage:customer_info", args=(self.customer_id, ))
    
    def get_site_url(self):
        return reverse("tpl_manage:customer_site", args=(self.customer_id, ))
    
    def get_user_url(self):
        return reverse("tpl_manage:customer_user", args=(self.customer_id, ))
    


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
    site_url = models.CharField(unique=True, max_length=400, blank=True, null=True)
    server_env = models.CharField(max_length=45, blank=True, null=True)
    framework = models.CharField(max_length=45, blank=True, null=True)
    is_root = models.IntegerField()



    class Meta:
        managed = False
        db_table = 'sites'

    def __str__(self):
        return self.site_url
    

    def get_tpl_url(self):
        return reverse("tpl_manage:customer_site_detail", args=(self.customer_id, self.site_id, ))
    
    def get_tpl_add_url(self):
        return reverse("tpl_manage:customer_tpl_add", args=(self.customer_id, self.site_id, ))

    def get_og_image(self):
        url = self.site_url
        print(url)
        img_path = og_tag.find_og_img(url)
        print(img_path)
        return img_path
        


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

    class Meta:
        managed = False
        db_table = 'users'

