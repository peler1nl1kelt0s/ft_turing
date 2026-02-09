import json
import sys

class Tape:
    def __init__(self, input_str, blank_char):
        self.blank = blank_char
        self.tape = list(input_str) if input_str else [blank_char]
        self.head = 0
        self.bound = 20

    def index_control(self):
        if self.head < 0:
            self.tape.insert(0, self.blank)
            self.head = 0
        elif self.head >= len(self.tape):
            self.tape.append(self.blank)

    def read(self):
        self.index_control()
        return self.tape[self.head]

    def write(self, char):
        self.index_control()
        self.tape[self.head] = char

    def action(self, action):
        if action == "RIGHT":
            self.head += 1
        elif action == "LEFT":
            self.head -= 1
        else:
            raise ValueError(f"Invalid action: {action}")

    def tape_view(self):
        b = self.bound
        h = self.head
        t = self.tape
        s = max(0, h - b // 2)
        e = s + b

        w = (t[s:e] + [self.blank] * b)[:b]
        i = h - s

        w[i] = f"<{w[i]}>"
        return "[" + "".join(w) + "]"


class TuringMachine:
    CONTINUE = 2
    HALT = 1
    ERROR = 0

    def __init__(self, jsonfile, input_str):
        self.name = jsonfile["name"]
        self.alphabet = jsonfile["alphabet"]
        self.blank = jsonfile["blank"]
        self.states = jsonfile["states"]
        self.initial_state = jsonfile["initial"]
        self.final_states = jsonfile["finals"]
        self.transitions = jsonfile["transitions"]

        self.current_state = self.initial_state
        self.tape = Tape(input_str, self.blank)

        self.file = open("results.txt", "w")

    def print_states(self):
        line_sep = "*" * 80
        empty = "*" + " " * 78 + "*"
        name_line = "*" + self.name.center(78) + "*"

        self.file.write(line_sep + "\n")
        self.file.write(empty + "\n")
        self.file.write(name_line + "\n")
        self.file.write(empty + "\n")
        self.file.write(line_sep + "\n")

        self.file.write("Alphabet: [ " + ", ".join(self.alphabet) + " ]\n")
        self.file.write("States: [ " + ", ".join(self.states) + " ]\n")
        self.file.write("Initial: " + self.initial_state + "\n")
        self.file.write("Finals: [ " + ", ".join(self.final_states) + " ]\n")

        for state, rules in self.transitions.items():
            for r in rules:
                self.file.write(
                    f"({state}, {r['read']}) -> "
                    f"({r['to_state']}, {r['write']}, {r['action']})\n"
                )

        self.file.write(line_sep + "\n")

    def print_step(self, read, write, action, next_state):
        self.file.write(
            f"{self.tape.tape_view()} "
            f"({self.current_state}, {read}) -> "
            f"({next_state}, {write}, {action})\n"
        )

    def step(self):
        if self.current_state in self.final_states:
            return self.HALT

        read_char = self.tape.read()

        for t in self.transitions[self.current_state]:
            if t["read"] == read_char:
                self.print_step(
                    read_char,
                    t["write"],
                    t["action"],
                    t["to_state"]
                )

                self.tape.write(t["write"])
                self.tape.action(t["action"])
                self.current_state = t["to_state"]
                return self.CONTINUE

        return self.ERROR

    def run(self, max_steps=10_000):
        self.print_states()

        steps = 0

        while steps < max_steps:
            result = self.step()
            steps += 1

            if result == self.CONTINUE:
                continue
            elif result == self.HALT:
                self.file.close()
                return 1
            else:
                self.file.close()
                return 0

        self.file.close()
        return 0
    def parse(self): 
        if self.initial_state not in self.transitions:
            raise ValueError(f"Invalid initial state: {self.current_state}")
        # alphabet transitions icerisinde hepsi dogru mu farkli var mi + blank
        # actionlar sadece left ve right mi
        # states ve transitions stateleri ayni mi
        # finals kismindakiler dogru state mi

def read_json(jsonfile):
    try:
        with open(jsonfile, "r") as f:
            return json.load(f)
    except Exception as e:
        print("JSON okunamadı:", e)
        sys.exit(1)
