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

from .custom_blocks.my_blocks import OneColumnHighlightBlock, TwoColumnHighlightBlock, ThreeColumnHighlightBlock,\
                                     SingleImageHeader, RotatingImageBlock, CenterImageWell, \
                                     MutedHighlightWithYellowIconsBlock, YellowStatBlock, HighlightWithStatBars, \
                                     TiledServiceBlock


class HomePage(Page):
    header = StreamField([
        ('single_image_header', SingleImageHeader()),
        ('rotating_image_header', RotatingImageBlock()),
    ], null=True, blank=True)
    body = StreamField([
        ('one_column_highlight', OneColumnHighlightBlock()),
        ('two_column_highlight', TwoColumnHighlightBlock()),
        ('three_column_highlight', ThreeColumnHighlightBlock()),
        ('center_image_well', CenterImageWell()),
        ('tiled_service_block', TiledServiceBlock()),
        ('muted_highlight_with_yellow_icons', MutedHighlightWithYellowIconsBlock()),
        ('yellow_stat_bar', YellowStatBlock()),
        ('highlight_with_stat_bars', HighlightWithStatBars()),
        ('single_image_header', SingleImageHeader()),
        ('rotating_image_header', RotatingImageBlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('header'),
        StreamFieldPanel('body'),
    ]

