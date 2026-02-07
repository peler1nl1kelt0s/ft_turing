import sys
from ft_turing import TuringMachine, read_json

def main():
	try:
		json_arg = read_json(sys.argv[1])
		machine = TuringMachine(jsonfile=json_arg, input=sys.argv[2])
		machine.run()
	except:
		print("Error Accured when read json file!! Please give me json file")

if __name__ == "__main__":
	main()