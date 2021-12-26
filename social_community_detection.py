import numpy as np
import csv
import json
from matrix_process import buildMatrix, readFileName, jsonMerge

def cal_similarity(vec1, vec2):
    dot_result = np.dot(vec1,vec2)
    module_result = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    return dot_result / module_result

def cal_avg_vec(matrix):
    avg = np.zeros([1,len(matrix[0])])
    num = matrix.shape[0]
    for i in range(num):
        avg = avg + matrix[i]
    return avg / num

def get_a_cluster(whole, whole_matrix,threshold):
    cluster = []
    if whole is not None:
        cluster.append(whole[0])
    else:
        print("Left is empty")
        return None, None
    
    for i in range(1,len(whole)):
        cluster_matrix = np.zeros([len(cluster), len(whole_matrix)])
        for j in range(len(cluster)):
            cluster_matrix[j] = whole_matrix[cluster[j]]

        cluster_avg_vec = cal_avg_vec(cluster_matrix)
        vec_i = whole_matrix[i]
        similarity = cal_similarity(cluster_avg_vec, vec_i)
        if similarity >= threshold:
            cluster.append(whole[i])

    cluster_matrix = np.zeros([len(cluster), len(whole_matrix)])
    
    for i in range(len(cluster)):
        cluster_matrix[i] = whole_matrix[cluster[i]]
        whole.remove(cluster[i])

    left = whole
    # print(cluster)
    # print(left)
    return cluster, left

def get_clusters(whole, whole_matrix, listname, threshold):
    
    clusters = []
    cluster_num = 0
    clusters_index = []
    while True:
        name = []
        cluster, left = get_a_cluster(whole, whole_matrix,threshold)
        
        for i in cluster:
            name.append(listname[i])

        clusters_index.append(cluster)
        clusters.append(name)
        if len(name) > 30:
            cluster_num = cluster_num + 1
        
        if len(left) != 0:
            whole = left
        else:
            break
    
    return clusters_index, clusters, cluster_num

# listname_path = 'listname_of_all.csv'
# usersA = []

# with open(listname_path, newline='') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         if row[1] != '':
#             usersA.append(row[1])
#         else:
#             print(row[0])


# threshold = 0.7
# leaders_num = 3
# whole = list(range(540))
# filenames = readFileName()
# # print(filenames)
# json_merge, all_congressman = jsonMerge(filenames)
# whole_matrix = buildMatrix(json_merge, all_congressman)
# listname = usersA

# cluster_index, clusters, cluster_num = get_clusters(whole, whole_matrix,listname, threshold)
# for i in clusters:
#     print(len(i))









    

