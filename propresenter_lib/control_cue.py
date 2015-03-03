from .shared import Shared
from lxml import etree, objectify
from .propresenter_object import ProPresenterObject


class ControlCue(ProPresenterObject):
	def __init__(self, **kwargs):
		self.display_name = kwargs.get("display_name")
		self.ns_number_list = kwargs.get("ns_number_list")
		self.index = kwargs.get("index", 0)

	def xml(self):
		control_cue = objectify.Element("RVControlCue")
		control_cue.attrib['UUID'] = Shared.get_uuid(self)
		control_cue.attrib['delayTime'] = "0"
		control_cue.attrib['displayName'] = self.display_name
		control_cue.attrib['enabled'] = "1"
		control_cue.attrib['filePath'] = ""
		control_cue.attrib['parentUUID'] = Shared.get_uuid(self)
		control_cue.attrib['serialization-array-index'] = str(self.index)
		control_cue.attrib['slideIndex'] = "-1"
		control_cue.attrib['slideUUID'] = ""
		control_cue.attrib['timestamp'] = "0"

		control_object = objectify.SubElement(control_cue, "controlObject")
		control_object.attrib['containerClass'] = "NSMutableDictionary"

		for ns_number in self.ns_number_list:
			key = ns_number
			value = self.ns_number_list[ns_number]
			
			ns_number_object = objectify.Element("NSNumber")
			ns_number_object.attrib['serialization-dictionary-key'] = str(key)
			ns_number_object.attrib['serialization-native-value'] = str(value)

			control_object.append(ns_number_object)

		objectify.deannotate(control_cue, pytype=True, xsi=True, xsi_nil=True, cleanup_namespaces=True)

		return control_cue