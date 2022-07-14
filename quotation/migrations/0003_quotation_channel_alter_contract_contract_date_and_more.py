# Generated by Django 4.0.5 on 2022-07-14 21:03

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sale_management', '0002_alter_province_deleted_at_alter_province_deleted_by_and_more'),
        ('quotation', '0002_alter_contract_contract_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='channel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sale_management.channel'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_date',
            field=models.DateField(default=datetime.date(2022, 7, 14), null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='delivery_time',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='status_date',
            field=models.DateField(default=datetime.date(2022, 7, 14), null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='valid_from_date',
            field=models.DateField(default=datetime.date(2022, 7, 14), null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='valid_to_date',
            field=models.DateField(default=datetime.date(2022, 7, 14), null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='quotation_date',
            field=models.DateField(default=datetime.date(2022, 7, 14), null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='status_date',
            field=models.DateField(default=datetime.date(2022, 7, 14), null=True),
        ),
    ]
