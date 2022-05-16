from dataclasses import dataclass


@dataclass
class IllegalCharacter:
    character: str
    row: int
    column: int

    def __str__(self) -> str:
        error_msg: str = (
            f"line {self.row}:{self.column} : Illegal character '{self.character}'"
        )
        return error_msg
