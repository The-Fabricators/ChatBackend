# Generated by Django 5.1.3 on 2024-11-29 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_payment_issuer_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payer_email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
