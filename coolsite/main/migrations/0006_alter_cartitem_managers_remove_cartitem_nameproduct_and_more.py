# Generated by Django 4.2.7 on 2024-05-13 10:33

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_review_options_alter_review_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='cartitem',
            managers=[
                ('objectsCartItem', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='nameProduct',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='priceOnMoneyProduct',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.product'),
        ),
    ]