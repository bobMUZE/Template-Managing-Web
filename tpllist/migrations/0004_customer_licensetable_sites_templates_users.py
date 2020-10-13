# Generated by Django 3.1.2 on 2020-10-07 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpllist', '0003_auto_20201007_0044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=45)),
                ('license_id', models.IntegerField()),
                ('join_date', models.DateField(blank=True, null=True)),
                ('site_name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LicenseTable',
            fields=[
                ('license_id', models.IntegerField(primary_key=True, serialize=False)),
                ('subscript_period', models.IntegerField(blank=True, null=True)),
                ('customer_ids', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'license_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('site_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_id', models.CharField(blank=True, max_length=45, null=True)),
                ('root_url', models.CharField(blank=True, db_column='root_URL', max_length=45, null=True)),
                ('server_env', models.CharField(blank=True, max_length=45, null=True)),
                ('framework', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'sites',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Templates',
            fields=[
                ('tpl_id', models.IntegerField(primary_key=True, serialize=False)),
                ('customer_id', models.IntegerField(blank=True, null=True)),
                ('site_id', models.IntegerField(blank=True, null=True)),
                ('permissions', models.CharField(blank=True, max_length=45, null=True)),
                ('module_id', models.CharField(blank=True, max_length=45, null=True)),
                ('tpl_url', models.CharField(blank=True, db_column='tpl_URL', max_length=200, null=True)),
                ('tpl_path', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'templates',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_id', models.CharField(blank=True, max_length=45, null=True)),
                ('site_id', models.IntegerField(blank=True, null=True)),
                ('u_name', models.CharField(blank=True, max_length=45, null=True)),
                ('u_passwd', models.CharField(blank=True, max_length=45, null=True)),
                ('permission_lvl', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
