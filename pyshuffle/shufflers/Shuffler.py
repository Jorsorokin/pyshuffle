import numpy as np


def shuffle_tensor(X, axis, randomness_level=0, kind='circular'):
    """
    suffles the data tensor X over one of 3 dimensions
    
    Params
    ------
    axis: int (0, 1, 2)
        this dictates which dimension to circularly permute

    randomness_level: int (0, 1, 2)
        this determines the amount of randomness applied to the shuffling procedure.
        Higher values result in more randommness.

        0: shuffle the values only within the axis specified
        1: shuffle the values within the axis specified over the second axis
        2: shuffle the values within the axis specified over the second axis randomized over the third axis

    kind: str ('circular', 'random')
        this determines the shuffling procedure (combined with `randomness_level`)

    Returns:
    -------
    shuffled_X: np.array
    """
    N, M, P = data.shape
    
    def get_shuffler(kind):
        def shuffle_circular(x, ind):
            return np.roll(x, ind)

        def shuffle_random(x, ind):
            return np.permute(x)

        shufflers = {
            'circular': shuffle_circular,
            'random': shuffle_random
        }
        return shufflers[kind]

    # returns a function call
    shuffler = shuffle_funcs[kind]

    if axis == 0:
        transpose_dims = [1, 0, 2]
        size = N
    elif axis == 2:
        transpose_dims = [0, 2, 1]
        size = P
    else:
        transpose_dims = None
        size = M
        
    if randomness_level == 0:
        def do_shuffle(Z):
            if kind == 'circular':
                return np.c_[]

    elif randomness_level == 1:
        def do_shuffle(Z):
            pass

    return None

