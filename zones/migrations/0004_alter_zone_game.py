# Generated by Django 3.2.9 on 2021-12-08 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
        ('zones', '0003_alter_zone_zones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zone',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='games.game'),
        ),
    ]