# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 15:47
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20170327_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('three_column_highlight', wagtail.wagtailcore.blocks.StructBlock((('column', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock())), icon='arrow-left', label='Column Content')),))),)),
        ),
    ]
