from matplotlib import pyplot as plt
from dataclass import TuringMachine

def input_generator(machine : TuringMachine):
	steps = list(range(1,101))
	generators = {
        "unary_add": lambda n: "1" * n + "+" + "1" * n + "=",
        "palindrome": lambda n: "1" * n + "0" * n + "1" * n,
        "0n1n": lambda n: "0" * n + "1" * n,
        "02n": lambda n: "0" * (2 * n),
        "utm_unary_add": lambda n: "q1_1_1_R_q1#" + "1"*n + "+" + "1"*n + "="
    }
	func = generators.get(machine.name, lambda n: "1" * n)
	inputs = tuple(map(func, steps))
	return inputs, steps

def complexity(machine : TuringMachine):
	pass

def visualize(n : int = 100):
	plt.plot()
	plt.xlabel("Elements")
	plt.ylabel("Operations")
	plt.legend()
	plt.show()