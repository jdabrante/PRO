import sys

import pycheck

CHECK_CASES = [
    [["AGTCCCAGGT"], "AGUCCCAGGU"],
    [["GCGCACTCTTCTTTGCTCTT"], "GCGCACUCUUCUUUGCUCUU"],
    [["CCGGAGATTGGCTACTGAAGATCCA"], "CCGGAGAUUGGCUACUGAAGAUCCA"],
]


def run(adn: str) -> str:
    arn = ""

    for base in adn:
        if base == "U":
            arn += "T"
        elif base == "T":
            arn += "U"
        else:
            arn += base
    return arn


if __name__ == "__main__":
    pycheck.check(run, CHECK_CASES, sys.argv)
