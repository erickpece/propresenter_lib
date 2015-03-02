from enum import Enum
from .shared import Shared
from lxml import etree, objectify
from .propresenter_object import ProPresenterObject


class Slide_Color(Enum):
	black = 1
	blue = 2
	brown = 3
	cyan = 4
	green = 5
	magenta = 6
	orange = 7
	purple = 8
	red = 9
	yellow = 10
	white = 11


class Slide_Transition(Enum):
	default = 1
	dissolve = 2
	iris = 3
	ripple = 4
	mod = 5
	flip = 6
	swap = 7
	cube = 8
	door = 9


class Slide(ProPresenterObject):
	def __init__(self, **kwargs):
		self.label = kwargs.get("label", "")
		self.slide_color = kwargs.get("slide_color", "")
		self.transition = kwargs.get("transition", "")
		self.enabled = kwargs.get("enabled", True)
		self.notes = kwargs.get("notes", "")
		self.index = kwargs.get("index", 0)

	def xml(self):
		slide = objectify.Element("RVDisplaySlide")
		slide.attrib['UUID'] = Shared.get_uuid(self)
		slide.attrib['backgroundColor'] = "0 0 0 1"
		slide.attrib['chordChartPath'] = ""
		slide.attrib['drawingBackgroundColor'] = "0"
		slide.attrib['enabled'] = str(int(self.enabled))
		
		if self.slide_color:
			if self.slide_color == Slide_Color.black:
				slide.attrib['highlightColor'] = Shared.rgb_hex_to_propresenter_color(self, 0, 0, 0)
			if self.slide_color == Slide_Color.blue:
				slide.attrib['highlightColor'] = Shared.rgb_hex_to_propresenter_color(self, 0, 0, 255)
			if self.slide_color == Slide_Color.brown:
				slide.attrib['highlightColor'] = Shared.rgb_hex_to_propresenter_color(self, 153, 102, 51)
			if self.slide_color == Slide_Color.cyan:
				slide.attrib['highlightColor'] = Shared.rgb_hex_to_propresenter_color(self, 0, 255, 255)
			if self.slide_color == Slide_Color.green:
				slide.attrib['highlightColor'] = Shared.rgb_hex_to_propresenter_color(self, 0, 255, 0)
			if self.slide_color == Slide_Color.magenta:
				slide.attrib['highlightColor'] = Shared.rgb_hex_to_propresenter_color(self, 255, 0, 255)
			if self.slide_color == Slide_Color.orange:
				slide.attrib['highlightColor'] = Shared.rgb_hex_to_propresenter_color(self, 255, 127, 0)
			if self.slide_color == Slide_Color.purple:
				slide.attrib['highlightColor'] = Shared.rgb_hex_to_propresenter_color(self, 127, 0, 127)
			if self.slide_color == Slide_Color.red:
				slide.attrib['highlightColor'] = Shared.rgb_hex_to_propresenter_color(self, 255, 0, 0)
			if self.slide_color == Slide_Color.yellow:
				slide.attrib['highlightColor'] = Shared.rgb_hex_to_propresenter_color(self, 255, 255, 0)
			if self.slide_color == Slide_Color.white:
				slide.attrib['highlightColor'] = Shared.rgb_hex_to_propresenter_color(self, 255, 255, 255)


		slide.attrib['hotKey'] = ""
		slide.attrib['label'] = self.label
		slide.attrib['notes'] = ""
		slide.attrib['serialization-array-index'] = str(self.index)
		slide.attrib['slideType'] = "1"
		slide.attrib['sort_index'] = str(self.index)

		cues = objectify.SubElement(slide, "cues")
		cues.attrib['containerClass'] = "NSMutableArray"

		display_elements = objectify.SubElement(slide, "displayElements")
		display_elements.attrib['containerClass'] = "NSMutableArray"

		# transition_object = objectify.SubElement(slide, "_-RVProTransitionObject-_transitionObject")
		# transition_object.attrib['motionDuration'] = "20"
		# transition_object.attrib['motionEnabled'] = "0"
		# transition_object.attrib['motionSpeed'] = "100"
		# transition_object.attrib['transitionDuration'] = "1"
		# transition_object.attrib['transitionType'] = "-1"

		objectify.deannotate(slide, pytype=True, xsi=True, xsi_nil=True, cleanup_namespaces=True)

		return slide