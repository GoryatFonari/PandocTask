from panflute import *
import sys

headers = []


def projectWord(elem, _):
    file.replace_keyword("project", Strong(Str("project")))


def headChanger(elem, _):
    if isinstance(elem, Header) and elem.level >= 2:
        return Header(Str(stringify(elem).upper()), level=elem.level)


def headerRepetitionMessage(elem):
    if isinstance(elem, Header):
        if stringify(elem) in headers:
            sys.stderr.write("Exchange headers, repetition detected." + stringify(elem))
        else:
            headers.append(stringify(elem))
