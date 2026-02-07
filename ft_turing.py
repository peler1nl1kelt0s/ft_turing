import json

class TuringMachine:
	def __init__(self, jsonfile, input):
		self.name = jsonfile["name"]
		self.alphabet = jsonfile["alphabet"]
		self.blank = jsonfile["blank"]
		self.states = jsonfile["states"]
		self.initial_state = jsonfile["initial"]
		self.finals_state = jsonfile["finals"]
		self.transitions = jsonfile["transitions"]
		self.state = self.initial_state
		self.input = input


	

def	read_json(jsonfile):
	return json.loads(jsonfile)

