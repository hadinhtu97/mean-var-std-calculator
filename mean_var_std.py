import numpy as np


def calculate(x):
    if len(x) < 9:
        raise ValueError('List must contain nine numbers.')
    else:
        matrix = np.array([
            [x[0], x[1], x[2]],
            [x[3], x[4], x[5]],
            [x[6], x[7], x[8]]
        ], dtype=int)
        return {
            'mean': [list(matrix.mean(axis=0)), list(matrix.mean(axis=1)), matrix.mean()],
            'variance': [list(matrix.var(axis=0)), list(matrix.var(axis=1)), matrix.var()],
            'standard deviation': [list(matrix.std(axis=0)), list(matrix.std(axis=1)), matrix.std()],
            'max': [list(matrix.max(axis=0)), list(matrix.max(axis=1)), matrix.max()],
            'min': [list(matrix.min(axis=0)), list(matrix.min(axis=1)), matrix.min()],
            'sum': [list(matrix.sum(axis=0)), list(matrix.sum(axis=1)), matrix.sum()]
        }
