# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 17:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('header', wagtail.wagtailcore.fields.StreamField((('single_image_header', wagtail.wagtailcore.blocks.StructBlock((('header', wagtail.wagtailcore.blocks.StreamBlock((('header_image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('header_top_text', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('header_sub_text', wagtail.wagtailcore.blocks.CharBlock()), ('header_info_text', wagtail.wagtailcore.blocks.CharBlock()), ('header_cta', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('header_target_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=True))), icon='image', label='Single Image Header')),))),))),
                ('body', wagtail.wagtailcore.fields.StreamField((('three_column_highlight', wagtail.wagtailcore.blocks.StructBlock((('left_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock())), icon='arrow-left', label='Left column content')), ('center_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock())), icon='arrow-down', label='Right column content')), ('right_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock())), icon='arrow-right', label='Right column content'))))),))),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.DeleteModel(
            name='HomePage',
        ),
    ]