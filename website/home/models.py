from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel, PageChooserPanel
from wagtail.wagtailimages.models import Image
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel

from .custom_blocks.my_blocks import ThreeColumnHighlightBlock, SingleImageHeader


class IndexPage(Page):
    header = StreamField([
        ('single_image_header', SingleImageHeader())
    ])
    body = StreamField([
        ('three_column_highlight', ThreeColumnHighlightBlock())
    ])
    # header_image = models.ForeignKey(
    #     'wagtailimages.Image',
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL,
    #     related_name='+'
    #     )   
    # header_top_text = models.CharField(max_length=255)
    # header_sub_text = models.CharField(max_length=255)
    # header_info_text = models.TextField()
    # header_cta = models.CharField(max_length=60)
    # header_target_link = models.ForeignKey(
    #     'wagtailcore.Page',
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL,
    #     related_name='+',
    # )

    content_panels = Page.content_panels + [
    	StreamFieldPanel('header'),
        StreamFieldPanel('body'),
    ]