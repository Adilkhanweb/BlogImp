# Generated by Django 4.1.1 on 2022-09-20 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamblocks', '0002_codeblock'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='title',
            field=models.CharField(default='Test', max_length=128),
        ),
    ]
