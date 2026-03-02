from dataclass import TuringMachine

def run(machine : TuringMachine):
	
	def get_transition(state : str, read_char : str) -> dict:
		transition = machine.transitions.get(state, [])
		return next(filter(lambda t: t["read"] == read_char, transition), None)

	def loop(current_state : str, tape : list, head : int):
		if current_state in machine.finals:
			print(f"Halted! Final tape: {''.join(tape)}")
			return tape
		
		read_char = tape[head] if 0 <= head < len(tape) else machine.blank
		transition = get_transition(state=current_state, read_char=read_char)
		new_tape = tape.copy()
		new_tape[head] = transition.get("write")
		new_head = head -1 if transition.get("action") == "LEFT" else head + 1
		print(tape, f"({current_state}, {transition.get("read")}) -> ({transition.get("to_state")}, {transition.get("write")}, {transition.get("action")})")
		return loop(current_state=transition.get("to_state"),tape=new_tape, head=new_head)

	loop(current_state=machine.initial, tape=machine.tape,head=0)

	