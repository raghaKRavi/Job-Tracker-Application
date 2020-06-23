# Generated by Django 3.0.7 on 2020-06-18 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sourceCode', '0003_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(blank=True, choices=[('pending', 'Pending'), ('success', 'Success'), ('failure', 'Failure')], max_length=8, null=True),
        ),
    ]
