# Generated by Django 5.0.1 on 2024-01-29 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhoods_api', '0006_blog1_description_blog2_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardmember',
            name='position',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
