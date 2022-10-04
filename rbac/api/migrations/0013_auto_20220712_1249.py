# Generated by Django 2.2.28 on 2022-07-12 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0012_auto_20220331_1924"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tenant",
            name="account_id",
            field=models.CharField(default=None, max_length=36, null=True),
        ),
        migrations.AlterField(
            model_name="tenant",
            name="org_id",
            field=models.CharField(db_index=True, default=None, max_length=36, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="tenant",
            name="tenant_name",
            field=models.CharField(max_length=63),
        ),
    ]