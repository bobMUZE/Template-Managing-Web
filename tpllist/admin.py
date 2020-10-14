from django.contrib import admin
from tpllist.models import Customer, LicenseTable, Sites, Templates, Users


# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'customer_name')

@admin.register(LicenseTable)
class LicenseTableAdmin(admin.ModelAdmin):
    list_display = ('license_id', 'subscript_period', 'customer_ids')


@admin.register(Sites)
class SitesAdmin(admin.ModelAdmin):
    list_display = ('site_id', 'customer_id', 'site_url')

@admin.register(Templates)
class TemplatesAdmin(admin.ModelAdmin):
    list_display = ('tpl_id', 'customer_id', 'site_id', 'tpl_url', 'tpl_path')

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'customer_id', 'site_id', 'u_name', 'u_passwd', 'permission_lvl')



