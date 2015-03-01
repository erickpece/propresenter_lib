from enum import Enum


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

class Slide:
	def __init__(self, **kwargs):
		self.label = kwargs.get("label")
		self.color = kwargs.get("color")
		self.transition = kwargs.get("transition")

	def __str__(self):
		description = "=" * 80
		description += "\nSlide: {}\n".format(self.label)
		description += "=" * 80
		description += "\nColor: {}".format(self.color)
		description += "\nTransition: {}".format(self.transition)

		return description

	def xml(self):
		return "Stub for ProPresenter slide XML"