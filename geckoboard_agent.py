from flask import Flask
from os import listdir
import imp
import inspect
import pdb
from geckoboard_types import types
import json

#there has to be a better way
def load_widgets():
	usable_widgets = {}
	alleged_widgets = [filename for filename in listdir("widgets") if filename.endswith(".py")]
	for filename in alleged_widgets:
		try:
			widget = imp.load_source(filename.split(".")[0],"widgets/"+filename)
			for name,obj in inspect.getmembers(widget):
				if inspect.isfunction(obj):
					usable_widgets[name] = obj
		except:
			pass

	return usable_widgets

def json_wrapper(user_defined_widget):
	original_call = lambda: json.dumps(user_defined_widget(types))
	return original_call

def run():
	widget_objects = load_widgets()
	app = Flask(__name__)
	
	for widget in widget_objects.keys():
		#dont want to force the user to json dump their widgets. not very clean.
		#TODO: is there a way to decorate this in flask?
		request = json_wrapper(widget_objects[widget])
		request.methods = ['GET']
		request.provide_automatic_options = False
		app.add_url_rule("/"+widget,widget,request)

	#change this if you dont like it.
	app.run("0.0.0.0",5000)

if __name__ == "__main__":
	run()