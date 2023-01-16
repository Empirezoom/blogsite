# Generated by Django 4.1.5 on 2023-01-11 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='logo')),
                ('big_logo', models.ImageField(upload_to='logo')),
                ('banner', models.ImageField(upload_to='banner')),
                ('ceo_pix', models.ImageField(upload_to='ceo_pix')),
                ('ceo_name', models.CharField(max_length=50)),
                ('phone_no', models.IntegerField()),
                ('phone_no2', models.IntegerField()),
                ('favicon', models.ImageField(upload_to='favicon')),
                ('about', models.TextField()),
                ('copyright', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'CompanyProfile',
                'verbose_name_plural': 'CompanyProfiles',
                'db_table': 'companyprofile',
                'managed': True,
            },
        ),
    ]