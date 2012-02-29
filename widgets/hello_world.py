#the name of this function becomes the request path.
#
#geckoboard_types is a dictionary of available widget types as defined by geckoboard. see README.

def hello_world(geckoboard_types,cache):

	#get the response object to extend
	my_widget = geckoboard_types["number_and_secondary_stat"]

	#do whatever calculation you need
	my_new_value = 5

	#update the new value
	my_widget["item"][0]["value"] = my_new_value

	#get the old one if it exists
	if "hello_world_foobar" in cache.keys():
		my_widget["item"][1]["value"] = cache["hello_world_foobar"]
	else:
		my_widget["item"][1]["value"] = 0

	#save for next time
	cache["hello_world_foobar"] = my_new_value

	return my_widget