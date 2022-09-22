# Generated by Django 4.1.1 on 2022-09-22 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamblocks', '0003_page_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Quote',
            },
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=128),
        ),
    ]
