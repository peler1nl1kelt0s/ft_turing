from dataclass import TuringMachine

def parse_json(json_arg: dict, input_string : str) -> TuringMachine:
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