from dataclass import TuringMachine


# TODO "IndexError: list assignment index out of range" hatasi aliyorum "111-111" inputu girdigim zaman. Sebebi de surekli olarak saga gitti icin indexi asiyor.
# TODO sonsuz dongu kontrolu eklenecek

FINAL = "FINAL"
BOUND = 20

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
            tape=list(input_string.ljust(BOUND, json_arg.get("blank"))),
        )
    except Exception:
        raise ValueError("Error when parsing json file")

def get_state(machine: TuringMachine, state: str):
    try:
        if state in machine.finals:
            return FINAL
        elif machine.transitions.get(state):
            return machine.transitions.get(state, [])
        else:
            raise ValueError("Error: states are invalid")
    except Exception:
        raise ValueError("Error: states are invalid")

def parse_input(machine : TuringMachine):
    error = list(filter(lambda tape: tape not in machine.alphabet, machine.tape))
    #TODO machine.tape null kontrolu yapilacak
	if error :
        raise ValueError(f"Error: input, {error} is invalid")

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

def parse_states_control(machine : TuringMachine):
    list(
        map(
            lambda state: list(
                map(
                    lambda t: parse_transition(machine, state, t["read"]),
                    get_state(machine=machine, state=state)
                )
            ),
            machine.transitions.keys()
        )
    )
        
def parse_halt(machine: TuringMachine):
    if not machine.finals:
        raise ValueError("Error: no final states defined")
    return list(filter(lambda s: s in machine.finals, machine.states))


def parse(machine: TuringMachine):
    try:
        get_state(machine=machine, state=machine.initial)
        parse_states(machine=machine)
        parse_states_control(machine=machine)
        parse_halt(machine=machine)
        parse_input(machine=machine)
    except Exception as e:
        print(e)
        return 0
    return 1