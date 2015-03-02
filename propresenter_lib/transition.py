from enum import Enum
from .shared import Shared
from lxml import etree, objectify
from .propresenter_object import ProPresenterObject


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


class Transition(ProPresenterObject):

	def __init__(self, **kwargs):
		self.motion_duration = kwargs.get("motion_duration", 20)
		self.motion_enabled = kwargs.get("motion_enabled", False)
		self.motion_speed = kwargs.get("motion_speed", 100)
		self.transition_duration = kwargs.get("transition_duration", 1)
		self.transition_type = kwargs.get("transition_type", Slide_Transition.default)

	def xml(self):
		transition = objectify.Element("_-RVProTransitionObject-_transitionObject")
		transition.attrib['motionDuration'] = str(self.motion_duration)
		transition.attrib['motionEnabled'] = str(int(self.motion_enabled))
		transition.attrib['motionSpeed'] = str(self.motion_speed)
		transition.attrib['transitionDuration'] = str(self.transition_duration)
		
		if self.transition_type == Slide_Transition.default:
			transition.attrib['transitionType'] = "-1"
		if self.transition_type == Slide_Transition.dissolve:
			transition.attrib['transitionType'] = "0"

		objectify.deannotate(transition, pytype=True, xsi=True, xsi_nil=True, cleanup_namespaces=True)

		return transition