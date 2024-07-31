"""
>>> sorted(get_anags('qwe', {'qwe', 'asd', 'ewq'}))
['ewq', 'qwe']
"""


def get_anags(word, wordlist):
    return set(
        filter(
            lambda candidate: sorted(candidate.lower())
            == sorted(word.lower()),
            wordlist,
        )
    )
