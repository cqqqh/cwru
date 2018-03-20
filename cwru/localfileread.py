import os

fileinfo = ['12DriveEndFault', '1797', '0.007-Ball', 'http://csegroups.case.edu/sites/default/files/bearingdatacenter/files/Datafiles/118.mat']
fpath = '/Users/qq/Datasets/CWRU/12DriveEndFault/1797/0.007-Ball.mat'
rdir = os.path.join(os.path.expanduser('~'), 'Datasets/CWRU')

def _copyfile_from_dataset(fpath, rdir, info):
    fmeta = os.path.join(os.path.dirname(__file__), 'metadata.txt')
    all_lines = open(fmeta).readlines()
    new_lines = []
    new_fmeta = os.path.join(os.path.dirname(__file__), 'metadata_new.txt')
    all_exit_files = dict()

    for root, dirs, files in os.walk(rdir):
        for file in files:
            last_word = file.split('_')[-1]
            if last_word.split('.')[-1] == 'mat':
                if last_word in all_exit_files:
                    print('wrong experiment')
                    exit(1)
                    # 有一些问题，有一些文件名会重复，比如276.mat
                all_exit_files[last_word] = file
        break

    for line in all_lines:
        l = line.split()
        # 还有许多未完成

    with open(new_fmeta, 'w') as f:
        f.writelines(new_lines)

    # existed_file_name_list = os.walk()
    # existed_file_path = os.path.join(rdir, info[0], info[1])


_copyfile_from_dataset(fpath, rdir, fileinfo)
