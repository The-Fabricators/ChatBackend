# Generated by Django 5.1.3 on 2024-11-29 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_payment_instalments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='amount',
            new_name='transaction_amount',
        ),
        migrations.AddField(
            model_name='payment',
            name='date_expiration',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_id',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
