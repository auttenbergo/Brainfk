import sys
from typing import List

from model.illegal_character_model import IllegalCharacter


class BrainfkAnalysis:
    @staticmethod
    def allowed_commands() -> List[str]:
        allowed_commands: List[str] = ["+", "-", ">", "<", "[", "]", ".", ",", " "]
        return allowed_commands

    @staticmethod
    def _error_non_existing_commands(
            non_existing_commands: List[IllegalCharacter],
    ) -> None:
        for non_existing_command in non_existing_commands:
            print(non_existing_command)
        sys.exit(-1)

    @staticmethod
    def _check_for_allowed_commands(code: List[str]) -> None:
        allowed_commands: List[str] = BrainfkAnalysis.allowed_commands()
        non_existing_commands: List[IllegalCharacter] = []

        for row, line in enumerate(code):
            for column, character in enumerate(line):
                if character not in allowed_commands:
                    illegal_character: IllegalCharacter = IllegalCharacter(
                        character, row + 1, column + 1
                    )
                    non_existing_commands.append(illegal_character)

        if non_existing_commands:
            BrainfkAnalysis._error_non_existing_commands(non_existing_commands)

    @staticmethod
    def _check_for_loop_validity(code: List[str]) -> None:
        stack: List[str] = []
        for row, line in enumerate(code):
            for column, character in enumerate(line):
                if character == "[":
                    stack.append(f"{row + 1}:{column + 1}")
                elif character == "]":
                    if not stack:
                        print(f"Illegal loop ending at {row + 1}:{column + 1}")
                        sys.exit(-1)
                    stack.pop()
        if stack:
            print(f"Illegal loop opening at {stack.pop()}")
            sys.exit(-1)

    @staticmethod
    def code_check(code: List[str]) -> None:
        BrainfkAnalysis._check_for_allowed_commands(code)
        BrainfkAnalysis._check_for_loop_validity(code)
