import uuid


class Shared:
	def get_uuid(self):
		uuid_string = uuid.uuid4()
		return str(uuid_string).upper()