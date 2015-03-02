from lxml import etree, objectify


class ProPresenterObject():
	def xml_string(self):
		return etree.tostring(self.xml())

	def __str__(self):
		description = "=" * 80
		description += "\nObject: {}\n".format(self.__class__.__name__)
		description += "=" * 80

		for attr in vars(self):
			description += "\n{}: {}".format(attr, getattr(self, attr))

		description += "\n"

		return description