class TuringMachine:
    def __init__(self) -> None:
        self.tape = [0]
        self.current_state_index = 0
        self.output_end = ""
        self.output_result = ""

    def finish(self):
        print(self.output_result)

    def set_output_end(self, end: str) -> None:
        self.output_end = end

    # Command ">"
    def go_to_right(self) -> None:
        self.current_state_index += 1
        if self.current_state_index == len(self.tape):
            self.tape.append(0)

    # Command "<"
    def go_to_left(self) -> None:
        self.current_state_index -= 1
        if self.current_state_index < 0:
            self.tape.insert(0, 0)

    # Command "+"
    def increment(self) -> None:
        self.tape[self.current_state_index] += 1

    # Command "-"
    def decrement(self) -> None:
        self.tape[self.current_state_index] -= 1

    # Command "."
    def output(self) -> None:
        character: str = chr(self.tape[self.current_state_index])
        self.output_result += character + self.output_end

    # Command ","
    def input_character(self):
        while True:
            character: str = input("Input a character: ")
            if len(character) != 1:
                print("Please, input a character!")
                continue

            self.tape[self.current_state_index] = ord(character)
            break

    def is_current_state_zero(self):
        return self.tape[self.current_state_index] == 0
