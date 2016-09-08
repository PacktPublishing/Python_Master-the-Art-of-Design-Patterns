from operator import itemgetter

def min_max_indexes(seq):
    minimum = min(enumerate(seq), key=itemgetter(1))
    maximum = max(enumerate(seq), key=itemgetter(1))
    return minimum[0], maximum[0]
