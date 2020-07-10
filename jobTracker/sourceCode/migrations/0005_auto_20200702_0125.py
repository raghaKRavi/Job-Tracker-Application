# Generated by Django 3.0.7 on 2020-07-02 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sourceCode', '0004_auto_20200618_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(blank=True, choices=[('pending', 'Pending'), ('success', 'Success'), ('failure', 'Failure')], default='', max_length=8, null=True, verbose_name='status'),
        ),
    ]
