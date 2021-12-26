import json
import os
import numpy as np
import csv

def readFileName():
    path = r"outputs"
    filenames = os.listdir(path)
    return filenames

def jsonMerge(filenames):
    json_datas = []
    for filename in filenames:
        path = r"outputs/"
        path += filename
        with open(path, 'r') as f:
            json_datas.append(json.load(f))
    json_merge = {}
    for json_data in json_datas:
        json_merge.update(json_data)
    all_congressman = list(json_merge.keys())
    for i in range(len(all_congressman)):
        all_congressman[i] = '@' + all_congressman[i]
    return json_merge, all_congressman

def buildMatrix(json_merge, all_congressman):
    name2index = {}
    for i in range(len(all_congressman)):
        name2index[all_congressman[i]] = i
    # print(name2index)
    user_len = len(all_congressman)
    ret_matrix = np.zeros([user_len, user_len])
    for key, value in json_merge.items():
        key_tmp = '@' + key
        for i in value:
            # print(key_tmp, i)
            ret_matrix[name2index[key_tmp]][name2index[i]] = 1
    return ret_matrix


if __name__ == '__main__':

    filenames = readFileName()
    # print(filenames)
    json_merge, all_congressman = jsonMerge(filenames)
    buildMatrix(json_merge, all_congressman)