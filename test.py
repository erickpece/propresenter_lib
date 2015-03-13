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
import yaml
import os


def make_quick_slide(label, media_url, **kwargs):
	transition = Transition(
		transition_duration = 1, 
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

def build_propresenter_from_yaml(path):
	config = yaml.load(open(path))
	
	# Capture global settings
	date = config['date']
	series = config['series']
	week = config['week']
	base_path = config['media_path']

	# Create playlist
	playlist_title = "{} - {} - Cove Kids".format(date, series)
	playlist = Playlist(name = playlist_title)

	for media in config['media']:
		# Create presentation
		presentation_name = "{} | {}".format(date, media)
		presentation = Presentation(presentation_name)

		for slide in config['media'][media]:
			media_path = os.path.join(base_path, slide['file'])
			base_name = os.path.basename(media_path)
			base_name = os.path.splitext(base_name)[0]
			base_name = base_name.split("-")
			base_name = base_name[len(base_name)-1]

			on_end = slide['onend']

			# Create slide
			new_slide = make_quick_slide(
				base_name, 
				media_path
			)

			presentation.add_slide(new_slide)

		playlist.add_presentation(presentation)

	playlist.write_file('/Users/erick/Desktop')

build_propresenter_from_yaml('definition.yaml')

