from flask import Flask
from os import listdir
import imp
import inspect
import pdb

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

def run():
	widget_objects = load_widgets()
	pdb.set_trace()
	app = Flask(__name__)
	
	for widget in widget_objects.keys():
		request = widget_objects[widget]
		request.methods = ['GET']
		request.provide_automatic_options = False
		app.add_url_rule("/"+widget,widget,request)

	app.run()

if __name__ == "__main__":
	run()