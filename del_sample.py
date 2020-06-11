# %%
# delete some wrong samples
from utils import *

label_list = ['W', 'A', 'S', 'D',
              'WA', 'WD', 'SA', 'SD',
              'AW', 'DW', 'AS', 'DS',  '']

filepath = 'E:/GAME/GTA5/data/'
filenames = dir_file(filepath)

for filename in filenames:
    label = get_label(filename)
    if label not in label_list:
        print(filename)
        os.remove(filepath + filename)

