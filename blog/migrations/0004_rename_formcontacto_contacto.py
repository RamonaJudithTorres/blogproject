# Generated by Django 4.0.4 on 2022-06-12 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_formcontacto_alter_article_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FormContacto',
            new_name='Contacto',
        ),
    ]
