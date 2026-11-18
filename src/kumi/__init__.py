import sys
from importlib.metadata import version


def main() -> None:
    if sys.argv[1:] in (["--version"], ["-V"]):
        print(f"kumi {version('kumi')}")
        return
    print("kumi: assemble projects from versioned blocks. Early development.")
