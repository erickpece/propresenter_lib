from enum import Enum
from .shared import Shared
from lxml import etree, objectify
from .propresenter_object import ProPresenterObject


class Presentation(ProPresenterObject):
	
	def __init__(self, title, **kwargs):
		self.title = title
		self.artist = kwargs.get("artist", "")
		self.author = kwargs.get("author", "")
		self.publisher = kwargs.get("publisher", "")
		self.notes = kwargs.get("notes", "")
		self.size_x = kwargs.get("size_x", "1920")
		self.size_y = kwargs.get("size_y", "1080")

		# Create our slide list
		self.slides = []

	def add_slide(self, slide):
		self.slides.append(slide)

	def xml(self):
		presentation = objectify.Element("RVPresentationDocument")
		presentation.attrib['CCLIArtistCredits'] = ""
		presentation.attrib['CCLICopyrightInfo'] = ""
		presentation.attrib['CCLIDisplay'] = "0"
		presentation.attrib['CCLILicenseNumber'] = ""
		presentation.attrib['CCLIPublisher'] = ""
		presentation.attrib['CCLISongTitle'] = ""
		presentation.attrib['album'] = ""
		presentation.attrib['artist'] = self.artist
		presentation.attrib['author'] = ""
		presentation.attrib['backgroundColor'] = "0 0 0 1"
		presentation.attrib['category'] = "Presentation"
		presentation.attrib['chordChartPath'] = ""
		presentation.attrib['creatorCode'] = ""
		presentation.attrib['docType'] = "0"
		presentation.attrib['drawingBackgroundColor'] = "0"
		presentation.attrib['height'] = self.size_y
		presentation.attrib['lastDateUsed'] = "2015-03-01T19:31:33"
		presentation.attrib['notes'] = ""
		presentation.attrib['resourcesDirectory'] = ""
		presentation.attrib['usedCount'] = "0"
		presentation.attrib['versionNumber'] = "500"
		presentation.attrib['width'] = self.size_x

		groups = objectify.SubElement(presentation, "groups")
		groups.attrib['containerClass'] = "NSMutableArray"

		slide_grouping = objectify.SubElement(groups, "RVSlideGrouping")
		slide_grouping.attrib['color'] = "0 0 0 0"
		slide_grouping.attrib['name'] = ""
		slide_grouping.attrib['serialization-array-index'] = "0"
		slide_grouping.attrib['uuid'] = Shared.get_uuid(self)

		slides = objectify.SubElement(slide_grouping, "slides")
		slides.attrib['containerClass'] = "NSMutableArray"

		# Loop through slides and add to this presentation
		index_value = 0
		for slide in self.slides:
			slide.index = index_value
			slides.append(slide.xml())

			index_value += 1

		objectify.deannotate(presentation, pytype=True, xsi=True, xsi_nil=True, cleanup_namespaces=True)

		return presentation