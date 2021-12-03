# Generated by Django 3.1.1 on 2020-09-14 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TPO_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(default='', max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phoneno', models.CharField(max_length=200)),
                ('college', models.CharField(max_length=20)),
                ('graduation', models.DecimalField(decimal_places=2, max_digits=5)),
                ('company', models.CharField(max_length=200)),
                ('profile', models.CharField(max_length=200)),
            ],
        ),
    ]
