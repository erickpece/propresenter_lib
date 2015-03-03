import os
import urllib.parse
from enum import Enum
from .shared import Shared
from lxml import etree, objectify
from .propresenter_object import ProPresenterObject


class MediaCue(ProPresenterObject):
	def __init__(self, **kwargs):
		self.source = kwargs.get("source")
		self.foreground = kwargs.get("foreground", True)
		self.transition = kwargs.get("transition", None)
		self.index = kwargs.get("index", 0)

	def xml(self):
		# Process filename
		head, tail = os.path.split(self.source)
		self.display_name = tail
		filename = "file://localhost{}".format(self.source).replace(" ", "%20")

		mediacue = objectify.Element("RVMediaCue")
		mediacue.attrib['UUID'] = Shared.get_uuid(self)
		mediacue.attrib['alignment'] = "4"

		# Foreground (True) or background (False)?
		if self.foreground:
			mediacue.attrib['behavior'] = "2"
		else:
			mediacue.attrib['behavior'] = "1"

		mediacue.attrib['delayTime'] = "0"
		mediacue.attrib['displayName'] = self.display_name
		mediacue.attrib['elementClassName'] = "RVImageElement"
		mediacue.attrib['enabled'] = "1"
		mediacue.attrib['parentUUID'] = Shared.get_uuid(self)
		mediacue.attrib['serialization-array-index'] = str(self.index)
		mediacue.attrib['timeStamp'] = "0"

		element = objectify.SubElement(mediacue, "element")
		element.attrib['displayName'] = self.display_name
		element.attrib['format'] = ""
		element.attrib['scaleBehavior'] = "3"
		element.attrib['scaleFactor'] = "1"
		element.attrib['source'] = filename
		element.attrib['typeID'] = "0"

		# Transition object, if any
		if self.transition is not None:
			mediacue.append(self.transition.xml())

		objectify.deannotate(mediacue, pytype=True, xsi=True, xsi_nil=True, cleanup_namespaces=True)

		return mediacue