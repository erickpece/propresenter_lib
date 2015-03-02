from enum import Enum
from .shared import Shared
from lxml import etree, objectify
from .propresenter_object import ProPresenterObject


class ControlNext(ProPresenterObject):
	def __init__(self, **kwargs):
		self.timer = kwargs.get("timer", 0)
		self.loop_to_beginning = kwargs.get("loop_to_beginning", False)

	def xml(self):
		control_cue = objectify.Element("RVControlCue")
		control_cue.attrib['UUID'] = Shared.get_uuid(self)
		control_cue.attrib['delayTime'] = "0"
		control_cue.attrib['displayName'] = "Go to Next"
		control_cue.attrib['enabled'] = "1"
		control_cue.attrib['filePath'] = ""
		control_cue.attrib['parentUUID'] = Shared.get_uuid(self)
		control_cue.attrib['serialization-array-index'] = "0"
		control_cue.attrib['slideIndex'] = "-1"
		control_cue.attrib['slideUUID'] = ""
		control_cue.attrib['timestamp'] = "0"

		control_object = objectify.SubElement(control_cue, "controlObject")
		control_object.attrib['containerClass'] = "NSMutableDictionary"

		number_timer = objectify.Element("NSNumber")
		number_timer.attrib['serialization-dictionary-key'] = "Timer"
		number_timer.attrib['serialization-native-value'] = str(self.timer)

		number_loop = objectify.Element("NSNumber")
		number_loop.attrib['serialization-dictionary-key'] = "LoopToBeginning"
		number_loop.attrib['serialization-native-value'] = str(int(self.loop_to_beginning))

		control_object.append(number_timer)
		control_object.append(number_loop)

		objectify.deannotate(control_cue, pytype=True, xsi=True, xsi_nil=True, cleanup_namespaces=True)

		return control_cue