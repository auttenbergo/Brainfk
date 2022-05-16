from dataclasses import dataclass, field
from typing import Dict, List

from model.turing_machine import TuringMachine
from parsing.loop_parser import LoopParser


@dataclass
class Interpretator:
    code: List[str]
    current_code_row: int = 0
    current_code_column: int = 0
    turing_machine: TuringMachine = field(default_factory=TuringMachine)

    def start(self) -> None:
        code: str = "".join([line for line in self.code])
        code = code.replace(" ", "")
        loop_mappings: Dict[int, int] = LoopParser.get_loop_mappings(code)
        current_command_index = 0

        while current_command_index < len(code):
            character: str = code[current_command_index]
            match character:
                case ">":
                    self.turing_machine.go_to_right()
                case "<":
                    self.turing_machine.go_to_left()
                case "+":
                    self.turing_machine.increment()
                case "-":
                    self.turing_machine.decrement()
                case ".":
                    self.turing_machine.output()
                case ",":
                    self.turing_machine.input_character()
                case "[":
                    current_command_index = (
                        current_command_index
                        if not self.turing_machine.is_current_state_zero()
                        else loop_mappings[current_command_index]
                    )
                case "]":
                    current_command_index = (
                        loop_mappings[current_command_index]
                        if not self.turing_machine.is_current_state_zero()
                        else current_command_index
                    )
            current_command_index += 1
        self.turing_machine.finish()
