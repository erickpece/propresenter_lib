from propresenter_lib.slide import Slide, Slide_Color
from propresenter_lib.presentation import Presentation
from propresenter_lib.transition import Transition, Slide_Transition
from propresenter_lib.control_next import ControlNext
from propresenter_lib.shared import Shared
import calendar
import time


presentation = Presentation()
presentation.add_slide(
	Slide(
		label="Test Start",
		goto_next=
			ControlNext(
				timer=4
			)
	)
)
presentation.add_slide(
	Slide(
		label="Test Trans Color", 
		slide_color=Slide_Color.red,
		transition=
			Transition(
				transition_type=Slide_Transition.default, 
				transition_duration=4
			),
		goto_next=
			ControlNext(
				timer=8,
				loop_to_beginning=True
		)
	)
)
presentation.add_slide(Slide(label="Test No Trans"))

Shared.write_to_file(None, '/Users/erick/Desktop/protest_{}.pro5'.format(calendar.timegm(time.gmtime())), presentation.xml_string())
print(presentation.xml_string())