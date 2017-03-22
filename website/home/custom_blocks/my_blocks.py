from django.db import models

from wagtail.wagtailcore.fields import StreamField, RichTextField
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, \
							InlinePanel, PageChooserPanel, StreamFieldPanel


class ThreeColumnHighlightBlock(blocks.StructBlock):
	left_column = blocks.StreamBlock([
		('heading', blocks.CharBlock(classname="full title")),
		('paragraph', blocks.RichTextBlock()),
		], icon='arrow-left', label='Left column content')

	center_column = blocks.StreamBlock([
		('heading', blocks.CharBlock(classname="full title")),
		('paragraph', blocks.RichTextBlock()),
		], icon='arrow-down', label='Right column content')

	right_column = blocks.StreamBlock([
		('heading', blocks.CharBlock(classname="full title")),
		('paragraph', blocks.RichTextBlock()),
		], icon='arrow-right', label='Right column content')

	class Meta:
		template = 'home/blocks/three_column_highlight_block.html'
		icon = 'pick'
		label = 'Three Column Highlight'


class SingleImageHeader(blocks.StructBlock):
	header = blocks.StreamBlock([
		('header_image', ImageChooserBlock(required=True)),
	    ('header_top_text', blocks.CharBlock(required=True)),
	    ('header_sub_text', blocks.CharBlock()),
	    ('header_info_text', blocks.CharBlock()),
	    ('header_cta', blocks.CharBlock(required=True)),
	    ('header_target_link', blocks.PageChooserBlock(required=True)),
		], icon = "image", label = "Single Image Header")

	class Meta:
		template = 'home/blocks/single_image_header.html'
		icon = 'image'
		label = 'Single Image Header'


# class RotatingImageHeader(blocks.StructBlock):
# 	pass