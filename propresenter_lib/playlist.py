import os
from enum import Enum
from .shared import Shared
from lxml import etree, objectify
import tempfile
from zipfile import ZipFile
import shutil
from .propresenter_object import ProPresenterObject


class Playlist(ProPresenterObject):
	
	def __init__(self, **kwargs):
		self.name = kwargs.get("name", "")
		self.temp_files = []

		# Create our slide list
		self.presentations = []

	def add_presentation(self, presentation):
		self.presentations.append(presentation)

	def zipdir(self, path, zip):
		for root, dirs, files in os.walk(path):
			for file in files:
				file_path = os.path.join(root, file)
				zip.write(file_path, "{}.pro5plx/".format(self.name) + os.path.basename(file_path))

	def write_file(self, target):
		project_dir = tempfile.mkdtemp()

		media_files = []

		# First, let's write the individual presentations, and also log the individual media files inside
		for presentation in self.presentations:
			presentation_file_path = "{}/{}.pro5".format(project_dir, presentation.title)
			presentation_file = open(presentation_file_path, "wb")
			presentation_file.write(presentation.xml_string())
			presentation_file.close()
			self.temp_files.append(presentation_file_path)

			for slides in presentation.slides:
				for cue in slides.cues:
					try:
						media_files.append(cue.source)
					except:
						pass


		## Then, let's write the playlist file
		playlist_file = open("{}/data.pro5pl".format(project_dir), "wb")
		playlist_file.write(self.xml_string())
		playlist_file.close()

		# Create zip file
		zip_file = ZipFile('{}/{}.pro5plx'.format(target, self.name), 'w')
		
		# Zip up the data files
		self.zipdir(project_dir, zip_file)

		# Zip up the media files in each presentation
		media_files = list(set(media_files))

		for media in media_files:
			zip_file.write(media, "{}.pro5plx/{}".format(self.name, media))

		# We're done - close it!
		zip_file.close()

		# Let's clean up by removing the temp folder
		shutil.rmtree(project_dir)


	def xml(self):
		playlist = objectify.Element("RVPlaylistDocument")
		playlist.attrib['creatorCode'] = ""
		playlist.attrib['playlistType'] = "0"
		playlist.attrib['versionNumber'] = "500"
		playlist.attrib['CCLILicenseNumber'] = ""

		playlists = objectify.SubElement(playlist, "playlists")
		playlists.attrib['containerClass'] = "NSMutableArray"

		dictionary = objectify.SubElement(playlists, "NSMutableDictionary")
		dictionary.attrib['containerClass'] = "NSMutableDictionary"
		dictionary.attrib['serialization-array-index'] = "0"

		playlist_details = objectify.SubElement(dictionary, "NSMutableString")
		playlist_details.attrib['serialization-dictionary-key'] = "playlistName"
		playlist_details.attrib['serialization-native-value'] = self.name

		playlist_children = objectify.SubElement(dictionary, "NSMutableArray")
		playlist_children.attrib['containerClass'] = "NSMutableArray"
		playlist_children.attrib['serialization-dictionary-key'] = "playlistChildren"
		playlist_children.attrib['key'] = "playlistChildren"

		# Loop through presentations and add to this playlist
		index_value = 0
		for presentation in self.presentations:
			presentation_child = objectify.SubElement(playlist_children, "RVDocumentCue")
			presentation_child.attrib['UUID'] = Shared.get_uuid(self)
			presentation_child.attrib['delayTime'] = "0"
			presentation_child.attrib['displayName'] = presentation.title
			presentation_child.attrib['enabled'] = "1"
			presentation_child.attrib['filePath'] = self.temp_files[index_value]
			presentation_child.attrib['parentUUID'] = Shared.get_uuid(self)
			presentation_child.attrib['selectedArrangementID'] = ""
			presentation_child.attrib['serialization-array-index'] = str(index_value)
			presentation_child.attrib['timeStamp'] = "0"

			index_value += 1

		playlist_children.attrib['key'] = "value"
		playlist_children.attrib['key'] = "value"

		objectify.deannotate(playlist, pytype=True, xsi=True, xsi_nil=True, cleanup_namespaces=True)

		return playlist