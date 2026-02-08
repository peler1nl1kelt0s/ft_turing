import json
import sys

class Tape:
	# !!! ALAN GENISLETMELERI KONTROLUNU YAPMAYI UNUTMA
	def __init__(self, input_str, blank_char):
		self.tape = list(input_str) if input_str else blank_char
		self.blank_char = blank_char
		self.head = 0
	
	def read(self):
		if 0 <= self.head <= len(self.tape):
			return self.tape[self.head]
		return self.blank_char

	def write(self, char):
		if 0 <= self.head <= len(self.tape):
			self.tape[self.head] = char
	
	def action(self,action_str):
		if action_str == "RIGHT":
			self.head += 1
		elif action_str == "LEFT":
			self.head -= 1

class TuringMachine:
	def __init__(self, jsonfile, input):
		self.name = jsonfile["name"]
		self.alphabet = list(jsonfile["alphabet"])
		self.blank = jsonfile["blank"]
		self.states = list(jsonfile["states"])
		self.initial_state = jsonfile["initial"]
		self.finals_state = jsonfile["finals"]
		self.transitions = jsonfile["transitions"]
		self.current_state = self.initial_state
		self.input = input
		self.tape = Tape(self.input, self.blank)
		self.file = open("results.txt", "w")

	def print_states(self):
		count = 39 - int(len(self.name) / 2)
		is_count_odd = count % 2 == 1
		print("is_count_odd: ", is_count_odd)
		self.file.write("*" * 80 + "\n")
		self.file.write("*" + " " * 78 + "*\n")
		self.file.write("*" + (count - 1 if is_count_odd==True else count) * " " + self.name + count * " " + "*\n")
		self.file.write("*" + " " * 78 + "*\n")
		self.file.write("*" * 80 + "\n")
		self.file.write("Alphabet: [ " + ", ".join(self.alphabet) + " ]\n")
		self.file.write("States: [ " + ", ".join(self.states) + " ]\n")
		self.file.write("Initial: " + self.initial_state + "\n")
		self.file.write("Finals: [ " + ", ".join(self.finals_state) + " ]\n")
		for state, rules in self.transitions.items():
			for r in rules:
				self.file.write(
					f"({state}, {r['read']}) -> "
					f"({r['to_state']}, {r['write']}, {r['action']})\n"
				)
		self.file.write("*" * 80)

	def step(self):
		if self.current_state in self.finals_state:
			print("Program finale geldi")
			self.file.close()
			return 1 
		
		# !!!!!!! HATA DURUMLARI KONTROLLERINI DAHA SONRASINDA PARSE KISMINDA 
		# YAP KI DAHA SONRASINDA TEK TEK KONTROL ETME !!!!!!!!!!

		current_char = self.tape.read()
		if self.current_state not in self.transitions:
			print("state, transitions icerisinde bulunamadi")
			return 0

		for t in self.transitions[self.current_state]:
			if current_char == t["read"]:
				self.tape.write(t["write"])
				self.tape.action(t["action"])
				self.current_state = t["to_state"]
				return 2
		return 0

	def run(self, max_steps=10_000):
		steps = 0

		while steps < max_steps:
			code = self.step()
			steps += 1
			if code == 2:
				continue
			elif code == 1:
				print("HALT: işlem başarıyla tamamlandı")
				print(self.tape.tape)
				return 1
			else:
				print("ERROR: geçersiz durum")
				return 0

		print("ERROR: sonsuz döngü tespit edildi")
		return 0
	

def	read_json(jsonfile):
	try:
		with open(jsonfile, 'r') as file:
			data = json.load(file)
		return data
	except:
		print("Please give valid json file!!")
		sys.exit(1)
