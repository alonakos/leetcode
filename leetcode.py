from typing import Optional, NamedTuple

import logging

MAX_ROWS = 1000000000
MAX_COLUMNS = 1000000000

#
# Complete the 'sortBinaryNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY bitArrays as parameter.
#

class IndexValuePair(NamedTuple):
    index: int
    value: int

def sortBinaryNumbers(bitArrays: list[list[int]]) -> list[int]:
    assert len(bitArrays) >= 1
    assert len(bitArrays) <= MAX_ROWS

    values: list[IndexValuePair] = []
    m: Optional[int] = None
    for i, row in enumerate(bitArrays):
        if m is None:
            m = len(row)
        assert len(row) == m

        value = 0
        for leftShiftBits in row:
            value |= 1 << leftShiftBits
        values.append(IndexValuePair(i, value))
   
    orderedIndices: list[str] = [pair.index for pair in sorted(values, key=lambda kvp: kvp.value, reverse=True)]
    return orderedIndices