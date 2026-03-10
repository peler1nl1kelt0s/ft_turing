import sys
import json
from parse import import_json, parse
from ft_turing import run
def main():

	if len(sys.argv) != 3:
		print("Usage: python main.py <json_file> <input>")
		sys.exit(1)
	try:
		file = open(sys.argv[1])
		json_arg = json.loads(file.read())
	except:
		print("Error: when reading json file. Please give valid json")
		exit(1)
	machine = import_json(json_arg=json_arg, input_string=sys.argv[2])
	if parse(machine=machine) == 0:
		return 0
	run(machine=machine)

if __name__ == "__main__":
	main()