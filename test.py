from propresenter_lib.slide import Slide, Slide_Color
from propresenter_lib.presentation import Presentation
from propresenter_lib.transition import Transition, Slide_Transition
from propresenter_lib.control_next import ControlNext
from propresenter_lib.media_cue import MediaCue
from propresenter_lib.shared import Shared
import calendar
import time

def make_quick_slide(label, media_url, **kwargs):
	transition = Transition(transition_duration=2, transition_type=Slide_Transition.dissolve)

	slide = Slide(
		label = label,
		transition = transition
	)

	media = MediaCue(
		source = media_url,
		transition = transition
	)

	slide.add_media(media)

	return slide

presentation = Presentation()

presentation.add_slide(make_quick_slide("Logo", "/Users/erick/Documents/The Cove/Cove Kids/Series/2015-02-21 Big Questions/2015-03-01/2015-03-01 - Big Questions - Logo.png"))
presentation.add_slide(make_quick_slide("Bottom Line", "/Users/erick/Documents/The Cove/Cove Kids/Series/2015-02-21 Big Questions/2015-03-01/2015-03-01 - Big Questions - Bottom Line Week 1.png"))
presentation.add_slide(make_quick_slide("Verse", "/Users/erick/Documents/The Cove/Cove Kids/Series/2015-02-21 Big Questions/2015-03-01/2015-03-01 - Big Questions - Preschool Verse.png"))

Shared.write_to_file(None, '/Users/erick/Desktop/protest_{}.pro5'.format(calendar.timegm(time.gmtime())), presentation.xml_string())
print(presentation.xml_string())