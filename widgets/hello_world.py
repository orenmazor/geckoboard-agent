#the name of this function becomes the request path.
#
#geckoboard_types is a dictionary of available widget types as defined by geckoboard. see README.

def hello_world(geckoboard_types):
	my_widget = geckoboard_types["number_and_secondary_stat"]
	my_widget["item"][0]["value"] = 5
	my_widget["item"][1]["value"] = 1

	return my_widget