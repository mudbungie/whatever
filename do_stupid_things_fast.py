from random import choices, randint
from subprocess import run
from string import printable
from keyword import kwlist
from sys import argv


def build_program(lines: int, max_line_length: int = 10) -> str:
    program = ""

    while len(program) < lines:
        new_word_length = k = randint(1, max_line_length)
        new_word = " ".join(choices([*printable, *kwlist], k=new_word_length))
    
        if is_valid_python(program + new_word):
            program += new_word + " "

    return program

def is_valid_python(program: str) -> bool:
    print(program)
    attempt = run(["python3", "-c", program], capture_output=True)
    return attempt.returncode == 0


if __name__ == "__main__":
    print(build_program(int(argv[1])))
