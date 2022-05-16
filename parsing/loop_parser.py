from typing import Dict


class LoopParser:
    @staticmethod
    def get_loop_mappings(code: str) -> Dict[int, int]:
        result: Dict[int, int] = {}
        stack = []
        for index, command in enumerate(code):
            if command == "[":
                stack.append(index)
            elif command == "]":
                last = stack.pop()
                result[last] = index
                result[index] = last
        return result
