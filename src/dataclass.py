from dataclasses import dataclass

@dataclass(frozen=True)
class TuringMachine:
    name: str
    alphabet: list
    blank: str
    states: list
    initial: str
    finals: list
    transitions: dict
    tape : list
    head : int = 0
    
