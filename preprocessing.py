# %%
from utils import *
from random import sample

LABEL_LIST = ['W', 'A', 'S', 'D',
              'WA', 'WD', 'SA', 'SD',
              'AW', 'DW', 'AS', 'DS',  '']

FILEPATH = 'F:/data/'
# FILEPATH = 'E:/GAME/GTA5/data/'

# %%
# delete some wrong samples
def delete_sample():
    filenames = dir_file(FILEPATH)
    for filename in filenames:
        label = get_label(filename)
        if label not in LABEL_LIST:
            print(filename)
            os.remove(FILEPATH + filename)
# %%
# data balance
def data_balance(target_num):
    filenames = dir_file(FILEPATH)
    index_label = [[] for i in range(len(LABEL_LIST))]
    # 行数等于LABEL数量，每行存储对应该标签的file索引
    
    for index_file, filename in enumerate(filenames):
        label = get_label(filename)
        index_label[LABEL_LIST.index(label)].append(index_file)
    label_num = [len(arr) for arr in index_label]
    
    if min(label_num) < target_num:
        lack_index = [i for i,x in enumerate(label_num) if x < target_num]
        for i in lack_index:
            print('Lack samples with label {}, which have {} samples now.'.format(LABEL_LIST[i],label_num[i]))
        return False

    catched_file = []
    for i in range(len(LABEL_LIST)):
        ind = sample(index_label[i], k=target_num)
        for i in ind:
            catched_file.append(filenames[i])
    return catched_file

if __name__ == "__main__":
    delete_sample()
    balanced_samples = data_balance(1)
    

