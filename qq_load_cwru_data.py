import numpy as np
import os
from scipy.io import loadmat

def load_and_slice_data_file(filename, block_len=384):
    # self.X_train = np.zeros((0, self.length))
    # self.X_test = np.zeros((0, self.length))
    # self.y_train = []
    # self.y_test = []

    mat_dict = loadmat(filename)
    keys = mat_dict.keys()
    print(keys)
    key = list(filter(lambda x: 'DE_time' in x, mat_dict.keys()))[0]
    time_series = mat_dict[key][:, 0]

    idx_last = -(time_series.shape[0] % block_len)
    clips = time_series[:idx_last].reshape(-1, block_len)

    n = clips.shape[0]
    n_split = 3 * n / 4
    # self.X_train = np.vstack((self.X_train, clips[:n_split]))
    # self.X_test = np.vstack((self.X_test, clips[n_split:]))
    # self.y_train += [idx] * n_split
    # self.y_test += [idx] * (clips.shape[0] - n_split)


files = ['12k_Drive_End_IR007_3_108.mat', '48k_Drive_End_OR021@3_2_252.mat']
rdir = os.path.join(os.path.expanduser('~'), 'Datasets/CWRU')

for file in files:
    file = os.path.join(rdir, file)
    load_and_slice_data_file(file, block_len=384)
