from dataclass import TuringMachine
from parse import get_state
from print import print_tape, print_initial_values

def run(machine : TuringMachine):
	def get_transition(state : str, read_char : str) -> dict:
		transition = get_state(machine=machine, state=state)
		return next(filter(lambda t: t["read"] == read_char, transition), None)

	def loop(current_state : str, tape : list, head : int):
		try:
			if current_state in machine.finals:
				return tape
			
			read_char = tape[head] if 0 <= head < len(tape) else machine.blank
			transition = get_transition(state=current_state, read_char=read_char)
			new_tape = tape.copy()
			new_tape[head] = transition.get("write")
			new_head = head + 1 if transition.get("action") == "RIGHT" else head - 1
			print_tape(tape=tape, current_state=current_state, read=transition.get("read"), to_state=transition.get("to_state"),write=transition.get("write"), action=transition.get("action"), head=head)
			return loop(current_state=transition.get("to_state"),tape=new_tape, head=new_head)
		except Exception as e:
			print(e)
			exit(1)

	print_initial_values(machine=machine)
	loop(current_state=machine.initial, tape=machine.tape,head=0)