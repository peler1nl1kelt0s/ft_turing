import sys
import ft_turing


def main():
	try:
		json_arg = ft_turing.read_json(sys.argv[1])
	except:
		print("Error Accured when read json file!! Please give me json file")

if "__name__" == "__main__":
	main()