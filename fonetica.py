# %%
import argparse
import sys


def fonerica(frase):
    xx = {
        "dd": "d",
        "tt": "t",
        "ll": "l",
        "rr": "r",
        "nn": "n",
        "mm": "m",
        "ss": "s",
        "gn": "2",
        "cc": "c",
        "ff": "f",
        "gg": "g",
        "bb": "b",
        "pp": "p",
        "zz": "z",
        "vv": "v",
        "sce": "0",
        "sci": "0",
        "sca": "7",
        "sco": "7",
        "scu": "7",
        "qu": "7",
        "ch": "7",
        "gh": "7",
        "gi": "6",
        "ge": "6",
        "ci": "6",
        "ce": "6",
        "g": "7",
        "c": "7",
        "q": "7",
        "s": "0",
        "z": "0",
        "m": "3",
        "n": "2",
        "r": "4",
        "l": "5",
        "t": "1",
        "d": "1",
        "p": "9",
        "b": "9",
        "f": "8",
        "v": "8",
        "a": "",
        "e": "",
        "i": "",
        "o": "",
        "u": "",
    }

    for key, value in xx.items():
        frase = frase.replace(key, value)
    return frase


def main():
    parser = argparse.ArgumentParser(description="fonerica")
    parser.add_argument("frase", help="Frase a convertir")
    args = parser.parse_args()

    print(fonerica(args.frase.lower().replace(" ", "").strip()))


if __name__ == "__main__":
    main()
    sys.exit(0)
