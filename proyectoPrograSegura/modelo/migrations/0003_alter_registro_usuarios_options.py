# Generated by Django 3.2.12 on 2022-06-01 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0002_auto_20220531_0324'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registro_usuarios',
            options={'ordering': ['-id']},
        ),
    ]
