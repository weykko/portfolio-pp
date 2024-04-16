# Generated by Django 5.0.4 on 2024-04-15 09:02

import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('rtfblock', wagtail.blocks.RichTextBlock()), ('imgblock', wagtail.images.blocks.ImageChooserBlock()), ('streamfieldblock', wagtail.embeds.blocks.EmbedBlock())], blank=True),
        ),
    ]
