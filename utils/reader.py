from typing import List


class Reader:
    @staticmethod
    def read(file_name: str) -> List[str]:
        code: List[str] = []
        with open(file_name, encoding="UTF-8") as f:
            code = f.readlines()
            for index, line in enumerate(code):
                code[index] = line.replace("\n", "")
        return code
