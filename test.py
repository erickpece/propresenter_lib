from propresenter_lib.slide import Slide, Slide_Color
from propresenter_lib.presentation import Presentation
from propresenter_lib.transition import Transition, Slide_Transition
from propresenter_lib.control_next import ControlNext
from propresenter_lib.media_cue import MediaCue
from propresenter_lib.shared import Shared
import calendar
import time

transition = Transition(transition_duration=2, transition_type=Slide_Transition.dissolve)

first = Slide(label="Logo", transition=transition)
media = MediaCue(transition=transition, source = "/Users/erick/Documents/The Cove/Cove Kids/Series/2015-02-21 Big Questions/2015-03-01/2015-03-01 - Big Questions - Logo.png")
first.add_media(media)

second = Slide(label="Bottom Line", transition=transition)
media2 = MediaCue(transition=transition, source = "/Users/erick/Documents/The Cove/Cove Kids/Series/2015-02-21 Big Questions/2015-03-01/2015-03-01 - Big Questions - Bottom Line Week 1.png")
second.add_media(media2)

third = Slide(label="Verse", transition=transition)
media3 = MediaCue(transition=transition, source = "/Users/erick/Documents/The Cove/Cove Kids/Series/2015-02-21 Big Questions/2015-03-01/2015-03-01 - Big Questions - Preschool Verse.png")
third.add_media(media3)


presentation = Presentation()
presentation.add_slide(first)
presentation.add_slide(second)
presentation.add_slide(third)
presentation.xml_string()

Shared.write_to_file(None, '/Users/erick/Desktop/protest_{}.pro5'.format(calendar.timegm(time.gmtime())), presentation.xml_string())
print(presentation.xml_string())