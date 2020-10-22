from django.contrib import admin
from tpllist.models import Customer, License, Site, Template, User


# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'customer_name')

@admin.register(License)
class LicenseTableAdmin(admin.ModelAdmin):
    list_display = ('license_id', 'subscript_date', 'max_sites')


@admin.register(Site)
class SitesAdmin(admin.ModelAdmin):
    list_display = ('site_id', 'customer_id', 'site_url')

@admin.register(Template)
class TemplatesAdmin(admin.ModelAdmin):
    list_display = ('tpl_id', 'customer_id', 'site_id', 'tpl_path')

@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'customer_id', 'site_id', 'u_name', 'u_passwd', 'permission_lvl')



