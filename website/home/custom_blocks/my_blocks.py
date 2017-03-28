from django.db import models

from wagtail.wagtailcore.fields import StreamField, RichTextField
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, \
							InlinePanel, PageChooserPanel, StreamFieldPanel



class ThreeColumnHighlightBlock(blocks.StructBlock):
	left_column = blocks.StructBlock([
		('heading', blocks.CharBlock(classname="full title")),
		('paragraph', blocks.RichTextBlock()),
		], icon='arrow-left', label='Left column content')

	center_column = blocks.StructBlock([
		('heading', blocks.CharBlock(classname="full title")),
		('paragraph', blocks.RichTextBlock()),
		], icon='arrow-down', label='Right column content')

	right_column = blocks.StructBlock([
		('heading', blocks.CharBlock(classname="full title")),
		('paragraph', blocks.RichTextBlock()),
		], icon='arrow-right', label='Right column content')

	class Meta:
		template = 'home/blocks/three_column_highlight_block.html'
		icon = 'pick'
		label = 'Three Column Highlight'


class TwoColumnHighlightBlock(blocks.StructBlock):
	left_column = blocks.StructBlock([
		('heading', blocks.CharBlock(classname="full title")),
		('paragraph', blocks.RichTextBlock()),
		], icon='arrow-left', label='Left column content')

	right_column = blocks.StructBlock([
		('heading', blocks.CharBlock(classname="full title")),
		('paragraph', blocks.RichTextBlock()),
		], icon='arrow-right', label='Right column content')

	class Meta:
		template = 'home/blocks/two_column_highlight_block.html'
		icon = 'pick'
		label = 'Two Column Highlight'


class OneColumnHighlightBlock(blocks.StructBlock):
	column = blocks.StructBlock([
		('heading', blocks.CharBlock(classname="full title")),
		('paragraph', blocks.RichTextBlock()),
		], icon='arrow-left', label='Left column content')

	class Meta:
		template = 'home/blocks/one_column_highlight_block.html'
		icon = 'pick'
		label = 'One Column Highlight'


class SingleImageHeader(blocks.StructBlock):
	header = blocks.StreamBlock([
		('header_image', ImageChooserBlock(default=0, required=True)),
		('header_top_text', blocks.CharBlock(default='Top Header Text', required=True)),
		('header_sub_text', blocks.CharBlock()),
		('header_info_text', blocks.CharBlock()),
		('header_cta', blocks.CharBlock(default='Call To Action', required=True)),
		('header_target_link', blocks.PageChooserBlock(default=0, required=True)),
		], icon = "image", label = "Single Image Header")

	class Meta:
		template = 'home/blocks/single_image_header.html'
		icon = 'image'
		label = 'Single Image Header'


class HeaderLinkBlock(blocks.StructBlock):
	cta = blocks.CharBlock(default='Call To Action', required=True)
	url_link = blocks.PageChooserBlock(default=0, required=True)
	
	class Meta:
		icon = "image"
		label = "Header Link Block"


class RotatingImageBlock(blocks.StructBlock):
	text = blocks.StructBlock([
		('header_top_text', blocks.CharBlock(default='Top Header Text', required=True)),
		('header_sub_text', blocks.CharBlock()),
		('header_info_text', blocks.CharBlock()),
		], icon = "image", label = "Rotating Image Banner")

	links = blocks.ListBlock(HeaderLinkBlock())

	images = blocks.ListBlock(ImageChooserBlock(default=0, required=True))

	class Meta:
		template = 'home/blocks/rotating_image_block.html'
		icon = 'image'
		label = 'Rotating Image Header'


class CenterImageWell(blocks.StructBlock):
	text = blocks.StructBlock([
		('header_top_text', blocks.CharBlock()),
		('header_info_text', blocks.CharBlock()),
		], icon = "doc-full", label = "Image Well Text")

	image = ImageChooserBlock(default=0, required=True)

	class Meta:
		template = 'home/blocks/center_image_well.html'
		icon = 'image'
		label = 'Center Image Well w-Text'


class HighlightWithIconBlock(blocks.StructBlock):
	service_icon = blocks.CharBlock(default='camera', required=True)
	service_title = blocks.CharBlock(required=True, default='service title')
	service_desc = blocks.CharBlock(default='service description')

	class Meta:
		icon = "tick-inverse"
		label = "Highlight Block w-Icon"


class MutedHighlightWithYellowIconsBlock(blocks.StructBlock):
	text = blocks.StructBlock([
		('services_cta', blocks.CharBlock(default='Services', required=True)),
		('services_info', blocks.CharBlock()),
		], icon = "doc-full", label = "Image Well Text")

	services = blocks.ListBlock(HighlightWithIconBlock())

	class Meta:
		template = 'home/blocks/muted_highlight_with_yellow_icons_block.html'
		icon = 'group'
		label = 'Gray Highlights w-Yellow Icons'


class TiledServiceBlock(blocks.StructBlock):
	services = blocks.ListBlock(HighlightWithIconBlock())

	class Meta:
		template = 'home/blocks/tiled_service_block.html'
		icon = 'group'
		label = 'Tiled Service Block'


class Stat(blocks.StructBlock):
	title = blocks.CharBlock(default='Stat')
	number = blocks.IntegerBlock(default=0, required=True)

	class Meta:
		icon = 'plus'
		label = 'Stat'


class YellowStatBlock(blocks.StructBlock):
	stats = blocks.ListBlock(Stat())

	class Meta:
		template = 'home/blocks/yellow_stat_block.html'
		icon = 'plus'
		label = 'Yellow Full-Width Stat Block'


class HighlightWithStatBars(blocks.StructBlock):
	text = blocks.StructBlock([
		('header_top_text', blocks.CharBlock()),
		('header_info_text', blocks.CharBlock()),
		], icon = "doc-full", label = "Text Blurb")

	stats = blocks.ListBlock(Stat())

	class Meta:
		template = 'home/blocks/highlight_with_stat_bars.html'
		icon = 'plus'
		label = 'Highlight Blurb w-Stats on Right'