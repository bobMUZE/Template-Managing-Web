from django.db import models
from django.urls import reverse
from tpllist.modules import og_tag



from django.db import models


class Customer(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=45)
    customer_name = models.CharField(max_length=45)
    license_id = models.IntegerField()
    join_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'customer'
    
    def __str__(self):
        return self.customer_name
    
    def get_absolute_url(self):
        return reverse("tpl_manage:customer_main", args=(self.customer_id, ))

    def get_info_url(self):
        return reverse("tpl_manage:customer_info", args=(self.customer_id, ))
    
    def get_init_url(self):
        return reverse("tpl_manage:customer_init", args=(self.customer_id, ))

    def get_site_url(self):
        return reverse("tpl_manage:customer_site", args=(self.customer_id, ))
    
    def get_user_url(self):
        return reverse("tpl_manage:customer_user", args=(self.customer_id, ))

    def get_add_url(self):
        return reverse("tpl_manage:customer_user", args=(self.customer_id, ))
    
    def get_report_url(self):
        return reverse("tpl_manage:customer_report", args=(self.customer_id, ))
    


class License(models.Model):
    license_id = models.AutoField(primary_key=True)
    subscript_date = models.IntegerField()
    max_sites = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'license'


class Site(models.Model):
    site_id = models.AutoField(primary_key=True)
    customer_id = models.CharField(max_length=45, blank=True, null=True)
    site_url = models.CharField(unique=True, max_length=300, blank=True, null=True)
    # server_env = models.CharField(max_length=45, blank=True, null=True)
    # framework = models.CharField(max_length=45, blank=True, null=True)
    parent_site = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'site'
    
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


class Template(models.Model):
    tpl_id = models.AutoField(primary_key=True)
    customer_id = models.CharField(max_length=45, blank=True, null=True)
    site_id = models.IntegerField(blank=True, null=True)
    permission = models.CharField(max_length=45, blank=True, null=True)
    module_id = models.IntegerField(blank=True, null=True)
    tpl_path = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'template'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    customer_id = models.CharField(max_length=45, blank=True, null=True)
    site_id = models.IntegerField(blank=True, null=True)
    u_name = models.CharField(max_length=45, blank=True, null=True)
    u_passwd = models.CharField(max_length=45, blank=True, null=True)
    permission_lvl = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
