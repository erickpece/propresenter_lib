from .shared import Shared
from lxml import etree, objectify
from .control_cue import ControlCue


class GotoNext(ControlCue):
	def __init__(self, index = 0, timer = 0, loop_to_beginning = False):
		self.index = index
		self.display_name = "Go to Next"
		self.ns_number_list = {
			"Timer": timer,
			"LoopToBeginning": str(int(loop_to_beginning))
		}


class ClearAll(ControlCue):
	def __init__(self, index = 0):
		self.index = index
		self.display_name = "Clear All"
		self.ns_number_list = {
			"Action": 0
		}


class ClearBackground(ControlCue):
	def __init__(self, index = 0):
		self.index = index
		self.display_name = "Clear Background"
		self.ns_number_list = {
			"Action": 1
		}


class ClearAudio(ControlCue):
	def __init__(self, index = 0):
		self.index = index
		self.display_name = "Clear Audio"
		self.ns_number_list = {
			"Action": 2
		}


class ClearProps(ControlCue):
	def __init__(self, index = 0):
		self.index = index
		self.display_name = "Clear Props"
		self.ns_number_list = {
			"Action": 3
		}


class ClearLiveVideo(ControlCue):
	def __init__(self, index = 0):
		self.index = index
		self.display_name = "Clear Live Video"
		self.ns_number_list = {
			"Action": 5
		}