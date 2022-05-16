import sys
from pathlib import Path
from typing import List

from interpretator import Interpretator
from model.turing_machine import TuringMachine
from parsing.analysis import BrainfkAnalysis
from utils.reader import Reader

if len(sys.argv) != 2:
    raise IndexError("Usage: python brainfk.py <FILE_PATH>")

file_name: str = sys.argv[1]
if not Path(file_name).is_file():
    raise FileNotFoundError(f"{file_name} does not exist or is not a file")

if not file_name.endswith(".bf"):
    raise IOError("File does not have .bf extension")

turing_machine: TuringMachine = TuringMachine()

code: List[str] = Reader.read(file_name)
BrainfkAnalysis.code_check(code)

interpretator: Interpretator = Interpretator(code, turing_machine=turing_machine)
interpretator.start()
