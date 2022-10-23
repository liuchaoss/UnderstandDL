import util
import numpy as np
from scipy import stats


def col(d, c):
    return np.array(d[:, c].tolist())


def row(d, col, cond):
    return np.array([line for line in d.tolist() if line[col] == cond])


if __name__ == '__main__':
    ds = util.load_csv('rawdata-preprocess.csv')
    ds = np.array([[float(i) for i in d] for d in ds])
    ls = util.load_csv('taxonomy-code.csv')

    col_viewcount = 2
    col_score = 3
    col_time = 5
    col_level1 = -2
    col_level2 = -1

    data = []
    for l in ls:
        l1 = float(l[1])
        l2 = float(l[2])
        key = l[2:]
        line = np.array([d for d in ds.tolist() if d[col_level1] == l1 and d[col_level2] == l2])
        m = np.median(line, axis=0)
        data.append(m)
    util.save_csv('taxonomy-analysis.csv', data)

    data = []
    for l in ls:
        l1 = float(l[1])
        key = l[2:]
        line = np.array([d for d in ds.tolist() if d[col_level1] == l1])
        m = np.median(line, axis=0)
        data.append(m)
    util.save_csv('taxonomy-analysis-overall.csv', data)

    a = stats.pearsonr(ds[:, col_viewcount], ds[:, col_score])
    a = stats.pearsonr(ds[:, col_viewcount], ds[:, col_time])

    print()
