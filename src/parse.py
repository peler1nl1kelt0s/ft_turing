from dataclass import TuringMachine

def import_json(json_arg: dict, input_string : str) -> TuringMachine:
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
    
def get_state(machine : TuringMachine, state : str):
    try:
        return machine.transitions.get(state)
    except:
        raise ValueError("Error: states are invalid")

def parse_states(machine : TuringMachine):
    map(lambda s: get_state(s), machine.states)

def parse_alphabet(machine : TuringMachine):
    map(lambda )
    pass

def parse_halt():
    pass

def parse(machine : TuringMachine):
    try:
        parse_states(machine=machine)
        parse_alphabet()
    except ValueError as e:
        print(e)
        return 0