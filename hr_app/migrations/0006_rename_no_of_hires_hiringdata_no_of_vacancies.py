# Generated by Django 4.2.5 on 2025-03-28 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0005_alter_hiringdata_date_req_received_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hiringdata',
            old_name='no_of_hires',
            new_name='no_of_vacancies',
        ),
    ]
