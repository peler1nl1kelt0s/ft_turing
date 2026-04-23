from dataclass import TuringMachine
import itertools
from config import WIDTH

def print_initial_values(machine):
    
    fmt_list = lambda lst: f"[ {', '.join(map(str, lst))} ]"
    
    box = [
        "*" * WIDTH,
        f"*{' ' * (WIDTH-2)}*",
        f"* {machine.name:^{WIDTH-4}} *",
        f"*{' ' * (WIDTH-2)}*",
        "*" * WIDTH
    ]
    list(map(print, box))

    print(f"Alphabet: {fmt_list(machine.alphabet)}")
    print(f"States  : {fmt_list(machine.states)}")
    print(f"Initial : {machine.initial}")
    print(f"Finals  : {fmt_list(machine.finals)}")

    all_transitions = itertools.chain.from_iterable(
        map(lambda state: 
            map(lambda t: {"state": state, **t}, machine.transitions[state]), 
            machine.transitions.keys()
        )
    )

    list(map(lambda t: print(
        f"({t['state']}, {t['read']}) -> ({t['to_state']}, {t['write']}, {t['action']})"
    ), all_transitions))

    print("*" * WIDTH)

def print_tape(tape, current_state, read, to_state, write, action, head):
    
    visual_tape = "".join(map(
        lambda x: f"<{x[1]}>" if x[0] == head else x[1], 
        enumerate(tape)
    ))
    print(f"[{visual_tape}] ({current_state}, {read}) -> ({to_state}, {write}, {action})")
