import numpy as np
import os
from scipy.fftpack import dct,idct
from scipy.io import loadmat
import matplotlib.pyplot as plt

# line_color = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
line_color = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

def load_data_file(filename, sub_name='DE_time'):
    # self.X_train = np.zeros((0, self.length))
    # self.X_test = np.zeros((0, self.length))
    # self.y_train = []
    # self.y_test = []

    mat_dict = loadmat(filename)
    key = list(filter(lambda x: sub_name in x, mat_dict.keys()))[0]
    time_series = mat_dict[key][:, 0]

    return time_series
    # idx_last = -(time_series.shape[0] % block_len)
    # clips = time_series[:idx_last].reshape(-1, block_len)
    #
    # n = clips.shape[0]
    # n_split = 3 * n / 4
    # self.X_train = np.vstack((self.X_train, clips[:n_split]))
    # self.X_test = np.vstack((self.X_test, clips[n_split:]))
    # self.y_train += [idx] * n_split
    # self.y_test += [idx] * (clips.shape[0] - n_split)


files = ['12k_Drive_End_IR007_2_107.mat', '12k_Drive_End_IR014_2_171']
rdir = os.path.join(os.path.expanduser('~'), 'Datasets', 'CWRU')
dct_block_size = 1024
dct_block_num = 0 #读取后更新
time_data = []

fig = plt.figure()
# x = np.linspace(1, dct_block_size, dct_block_size)
# dct_all_data = np.zeros((100,2048))

# file_num = 0
for file in files:
    file = os.path.join(rdir, file)
    time_all_data = load_data_file(file, sub_name='DE_time')
    dct_block_num = len(time_all_data) // dct_block_size
    dct_all_data = np.zeros((dct_block_num, dct_block_size))
    for i in range(dct_block_num):
        print(i)
        time_data = time_all_data[i*dct_block_size : (i+1)*dct_block_size]
        dct_data = dct(time_data, type=2, norm='ortho')
        dct_all_data[i] = dct_data
        # dct_all_data[i+file_num*50] = dct_data
    # file_num = file_num + 1

# 画一个文件不同点的走势图
init_idx = 50
for i in range(5):
    pltdata = dct_all_data[:,init_idx+i]
    plt.plot(np.linspace(1, len(pltdata), len(pltdata)), pltdata, line_color[i % line_color.__len__()], linewidth=0.5)

# 两个文件的idx50画图
# idx = 50
# # for i in range(2):
# pltdata = dct_all_data[0:50,idx]
# i=1
# plt.plot(np.linspace(1,len(pltdata),len(pltdata)), pltdata, line_color[i % line_color.__len__()], linewidth=0.5)
# pltdata = dct_all_data[50:100, idx]
# i=2
# plt.plot(np.linspace(1, len(pltdata), len(pltdata)), pltdata, line_color[i % line_color.__len__()], linewidth=0.5)

#  sss
print(dct_data)
idct_data = idct(dct_data, type=2, norm='ortho')
# plt.plot(x, idct_data, 'b', linewidth=1)
diff = time_data - idct_data
plt.plot(x, diff, 'b', linewidth=1)
for i in range(len(dct_data)):
    if time_data[i] != idct_data[i]:
        print(time_data[i] - idct_data[i])
        #max 2.2e-16,min -2.2e-16

