from dataclass import TuringMachine

FINAL = "FINAL"

def import_json(json_arg: dict, input_string: str) -> TuringMachine:
    try:
        return TuringMachine(
            name=json_arg.get("name"),
            blank=json_arg.get("blank"),
            initial=json_arg.get("initial"),
            alphabet=list(json_arg.get("alphabet")),
            states=list(json_arg.get("states")),
            finals=list(json_arg.get("finals")),
            transitions=dict(json_arg.get("transitions")),
            tape=list(input_string),
        )
    except Exception:
        raise ValueError("Error when parsing json file")


def get_state(machine: TuringMachine, state: str):
    try:
        if state in machine.finals:
            return FINAL
        elif machine.transitions.get(state):
            return machine.transitions.get(state)
    except Exception:
        raise ValueError("Error: states are invalid")


def parse_input(machine : TuringMachine):
	if not list(map(lambda alp: alp in machine.tape)):
		raise ValueError("Error: input is invalid")

def parse_states(machine: TuringMachine):
    return list(map(lambda s: get_state(machine, s), machine.states))


def parse_transition(machine: TuringMachine, state: str, read_char: str):
    if read_char not in machine.alphabet:
        raise ValueError(f"Error: read char '{read_char}' is not in alphabet {machine.alphabet}")
    
    transition = next(
        filter(
            lambda t: t["read"] == read_char,
            machine.transitions.get(state, [])
        ),
        None
    )
    
    if transition is None:
        raise ValueError(f"Error: no transition found for state '{state}' with read '{read_char}'")
    
    if transition["write"] not in machine.alphabet:
        raise ValueError(f"Error: write char '{transition['write']}' is not in alphabet {machine.alphabet}")
    
    if transition["to_state"] not in machine.states:
        raise ValueError(f"Error: to_state '{transition['to_state']}' is not in states {machine.states}")
    
    if transition["action"] not in ("LEFT", "RIGHT"):
        raise ValueError(f"Error: action '{transition['action']}' must be LEFT or RIGHT")
    
    return transition


def parse_halt(machine: TuringMachine):
    if not machine.finals:
        raise ValueError("Error: no final states defined")
    return list(filter(lambda s: s in machine.finals, machine.states))


def parse(machine: TuringMachine):
    try:
        parse_states(machine=machine)
        parse_halt(machine=machine)
        list(
            map(
                lambda state: list(
                    map(
                        lambda t: parse_transition(machine, state, t["read"]),
                        machine.transitions.get(state, [])
                    )
                ),
                machine.transitions.keys()
            )
        )
    except ValueError as e:
        print(e)
        return 0
    return 1