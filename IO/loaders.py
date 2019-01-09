from skimage import io
from scipy.io import loadmat


def load_tiff(path):
    mat = dict()
    mat['im'] = io.imread(path)

    return mat


def load_mat(path):
    mat = loadmat(path)

    return mat
