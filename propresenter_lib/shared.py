import uuid


class Shared:
	def get_uuid(self):
		uuid_string = uuid.uuid4()
		return str(uuid_string).upper()

	def rgb_hex_to_propresenter_color(self, r, g, b):
		return "{} {} {} 1".format(r/255, g/255, b/255)