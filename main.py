import sys
from ft_turing import TuringMachine, read_json

def main():
	# JSON PARSE KONTROLU YAPILACAK
	if len(sys.argv) != 3:
		print("Usage: python main.py <json_file> <input>")
		sys.exit(1)

	json_arg = read_json(sys.argv[1])
	machine = TuringMachine(jsonfile=json_arg, input=sys.argv[2])
	machine.print_states()
	machine.run()
if __name__ == "__main__":
	main()