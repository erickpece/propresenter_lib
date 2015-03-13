from propresenter_lib.slide import Slide, Slide_Color
from propresenter_lib.presentation import Presentation
from propresenter_lib.playlist import Playlist
from propresenter_lib.transition import Transition, Slide_Transition
from propresenter_lib.control_next import ControlNext
from propresenter_lib.media_cue import MediaCue
from propresenter_lib.shared import Shared
from propresenter_lib.control_cue import ControlCue
from propresenter_lib.controls import GotoNext, ClearAll, ClearBackground, ClearAudio
import calendar
import time


def make_quick_slide(label, media_url, **kwargs):
	transition = Transition(
		transition_duration = 2, 
		transition_type = Slide_Transition.dissolve
	)

	slide = Slide(
		label = label,
		transition = transition
	)

	media = MediaCue(
		source = media_url,
		foreground = kwargs.get("foreground", True),
		transition = transition
	)

	slide.add_cue(media)

	if kwargs.get("go_to_next"):
		cue = GotoNext(kwargs.get("go_to_next"))
		slide.add_cue(cue)

	if kwargs.get("clear_audio"):
		cue = ClearAudio()
		slide.add_cue(cue)

	return slide

presentation = Presentation(title="2015-03-22 | Preschool")

presentation.add_slide(
	make_quick_slide(
		"Logo", 
		"/Users/erick/Desktop/2015-03-15/2015-03-15 - Big Questions - Logo.png",
		clear_audio=True
	)
)

presentation.add_slide(
	make_quick_slide(
		"Worship & Praise", 
		"/Users/erick/Desktop/2015-03-15/2015-03-15 - Big Questions - Worship and Praise.mp4", 
		foreground=True,
		go_to_next=True
	)
)

presentation.add_slide(
	make_quick_slide(
		"Path Straight", 
		"/Users/erick/Desktop/2015-03-15/2015-03-15 - Big Questions - Path Straight.mp4",
		foreground=True,
		go_to_next=True
	)
)

presentation.add_slide(
	make_quick_slide(
		"Logo", 
		"/Users/erick/Desktop/2015-03-15/2015-03-15 - Big Questions - Logo.png",
		clear_audio=True
	)
)

presentation.add_slide(
	make_quick_slide(
		"Trust in the Lord", 
		"/Users/erick/Desktop/2015-03-15/2015-03-15 - Big Questions - 2s Trust in the Lord.mp4",
		foreground=True,
		go_to_next=True
	)
)

# Shared.write_to_file(None, '/Users/erick/Desktop/pro5test_{}.pro5'.format(calendar.timegm(time.gmtime())), presentation.xml_string())

presentation2 = Presentation("2015-03-22 | Grade School")

presentation2.add_slide(
	make_quick_slide(
		"Logo", 
		"/Users/erick/Desktop/2015-03-15/2015-03-15 - Big Questions - Logo.png",
		clear_audio=True
	)
)

# Shared.write_to_file(None, '/Users/erick/Desktop/pro5test_{}-2.pro5'.format(calendar.timegm(time.gmtime())), presentation2.xml_string())


playlist = Playlist(name="2015-03-22 Cove Kids")
playlist.add_presentation(presentation)
playlist.add_presentation(presentation2)

# print(playlist.xml_string())
playlist.write_file('/Users/erick/Desktop')