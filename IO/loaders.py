from skimage import io
from scipy.io import loadmat


def load_tiff(path):
    """
    Loading a .tiff file using the scikit-image `io.imread()` function

    Args:
        path (str): The path of the .tiff file to load.

    Returns:
        ndarray: A dictionary with the image as a matrix under the *im* key.
    """

    mat = dict()
    mat['im'] = io.imread(path)

    return mat


def load_mat(path):
    mat = loadmat(path)

    return mat
