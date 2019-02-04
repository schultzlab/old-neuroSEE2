from skimage import io
from scipy.io import loadmat


def load_tiff(path):
    """Loads a .tiff file using the scikit-image `io.imread()` function

    Args:
        path (str): The path of the .tiff file to load.

    Returns:
        ndarray: A dictionary with the image as a matrix under the *im* key.
    """

    mat = dict()
    mat['im'] = io.imread(path)

    return mat


def load_mat(path):
    """Loads a .mat file using the `scipy.io.loadmat()` function

        Args:
            path (str): The path of the .mat file to load.

        Returns:
            ndarray: A dictionary with the image as a matrix and where the key is whatever the variable name was saved
            as in Matlab.
        """
    mat = loadmat(path)

    return mat
