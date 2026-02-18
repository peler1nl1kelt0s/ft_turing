import sys
import json
from parse import parse_json, parse_arg

def main():

	if len(sys.argv) != 3:
		print("Usage: python main.py <json_file> <input>")
		sys.exit(1)

	input_str=sys.argv[2]
	try:
		file = open(sys.argv[1])
		json_arg = json.loads(file.read())
	except:
		print("Error: when reading json file. Please give valid json")
		file.close()
		exit(1)
	machine = parse_json(json_arg=json_arg)
	tape = parse_arg(machine=machine, input_str=input_str)
	

if __name__ == "__main__":
	main()