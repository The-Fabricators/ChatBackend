# Generated by Django 5.1.3 on 2024-11-30 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genericAI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='geminigenericai',
            name='cover',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='geminigenericai',
            name='answer',
            field=models.CharField(blank=True, max_length=4000, null=True),
        ),
    ]
