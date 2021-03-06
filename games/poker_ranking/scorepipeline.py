import numpy as np
import functools


_NORESULT = -1

class ScoreHand:
    def __init__(self, matrix):

        self.matrix = matrix
        self.collapsed = np.sum(matrix, axis=0)


def tohexscore(klass, ms, ls):
    return 16**2 * klass + 16 * ms + max(0, ls) # max since -1 is indicator

class Pipeline:
    def __init__(self, *funcs):

        self.pipeline = funcs

    def add(self, func):

        self.pipeline.append(func)

    def evaluate(self, matrix):
        klasses = 9

        hand = ScoreHand(matrix)

        mapper = map(lambda f: f(hand), self.pipeline)


        scores = []
        for i, bits in enumerate(mapper):
            klass = klasses - i
            ls, ms = bits[-2:]
        #    print(klass, ms, ls)
            if ms != _NORESULT:
                #hexscore = int(tohexscore(klass, ms, ls))
                #scores.append(hexscore)
                scores.append([klass,ms,ls])

        return scores 


def collapsed(func):
    @functools.wraps(func)
    def _wrapper(hand):
        if isinstance(hand, ScoreHand):
            indices = func(hand.collapsed)
            return np.insert(indices, 0, [_NORESULT, _NORESULT])
        else:
            return func(hand)

    return _wrapper


def matrix(func):
    @functools.wraps(func)
    def _wrapper(hand):
        if isinstance(hand, ScoreHand):
            indices = func(hand.matrix)
            return np.insert(indices, 0, [_NORESULT, _NORESULT])
        else:
            return func(hand)
    return _wrapper


@matrix
def royalflush(x):
    subselect = x[:, -5:]
    if np.any(np.sum(subselect, axis=1) == 5):
        return 1
    else:
        return np.array([])

@matrix
def straightflush(x):
    suits = np.where(
        np.sum(x, axis=1) >= 5
    )[0]

    if len(suits) == 1:
        row = x[suits[0]]
        ind = straight(row)
        return ind

    else:
        return np.array([])

@collapsed
def fourofakind(x):
  return np.where(x==4)[0]


@collapsed
def fullhouse(x):
    twos = np.where(x == 2)[0]
    threes = np.where(x == 3)[0]

    if len(twos) >= 1 and len(threes) >= 1:
        return np.array([twos[0], threes[0]])

    return np.array([]) 


@matrix
def flush(x):
    suits = np.where(
        np.sum(x, axis=1) >= 5
    )[0]

    indices = []
    if len(suits) == 1:
        return np.where(x[suits[0]] == 1)
    else:
        return np.array([])


@collapsed
def straight(x):
    highlow = np.hstack(
        ([x[-1]], x)
    )

    indices = []
    for window in range(0, len(highlow) - 5):
        subview = highlow[window:window+4]
        if sum([1 for i in subview if i >= 1])==5:
            indices.append(window+4)

    return np.array(indices)

@collapsed
def tripples(x):
    return np.where(x == 3)[0]


@collapsed
def twopair(x):
    indices = np.where(x == 2)[0]
    if len(indices) >= 2:
        return indices
    else:
        return np.array([])

@collapsed
def pair(x):
    return np.where(x == 2)[0]


@collapsed
def highcard(x):
    return np.where(x >= 1)[0]


if __name__ == "__main__":

    pipeline = Pipeline(
    royalflush,
    straightflush,
    fourofakind,
    fullhouse,
    flush,
    straight,
    tripples,
    twopair,
    pair,
    highcard
    )

    print(pipeline.evaluate(
        np.array(
            [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
        )
    ))