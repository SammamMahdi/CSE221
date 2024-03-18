from collections import defaultdict


def customSortString(self, order: str, s: str) -> str:
    count = defaultdict(int)
    for c in s:
        count[c] += 1
    result = ""
    for c in order:
        if c in count:
            result += c * count[c]
            count.pop(c)
    for c in count:
        result += c * count[c]

    return result
