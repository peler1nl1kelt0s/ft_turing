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
    bound: int = 20
    tape: list
    head : int = 0
    tape : list
    
    