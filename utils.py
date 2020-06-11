import os

def dir_file(filepath):
    """Get all filenames in path."""
    filenames = []
    for parent, dirnames, filename in os.walk(filepath):
        filenames = filename
    print('number of original figure is {}'.format(len(filenames)))
    return filenames

def myfind(pattern, name):
    return [a for a in range(len(name)) if name[a] == pattern]

def get_label(filename):
    index = myfind('_', filename)
    return filename[index[0]+1:-4]