from social_community_detection import get_clusters
import numpy as np
import csv
import json
from matrix_process import buildMatrix, readFileName, jsonMerge

def find_common_followings(cluster_i, whole_matrix, gap):
    commmon_following = []
    verify = np.zeros(len(whole_matrix[0]))
    
    for j in cluster_i:
        verify = verify + whole_matrix[j]
    
    for i in range(len(whole_matrix[0])):
        if verify[i] >= len(cluster_i) * (1 - gap):
            commmon_following.append(i)
    if len(commmon_following) == 0:
        gap = gap + 0.1
        
        return find_common_followings(cluster_i,whole_matrix,gap)

    if len(commmon_following) >= len(cluster_i):
        commmon_following = cluster_i
    
    #if len(commmon_following)
    # sorted_index = np.argsort(verify)
    # lenx = len(cluster_i)
    # commmon_following = sorted_index[(lenx * 9 // 10): lenx]
    
    return commmon_following

def find_opinion_leader(whole,whole_matrix,listname, leaders_num, threshold):
    opinion_leaders = []

    clusters_index, clusters, cluster_num = get_clusters(whole, whole_matrix, listname, threshold)
    for i in clusters_index:
        print(len(i))

    for i in clusters_index:
        
        current_cluster  = i
       
        while True:
            if len(current_cluster) <= leaders_num:
                opinion_leaders.append(current_cluster)
                break
            else:
                common_follownig = find_common_followings(current_cluster, whole_matrix, 0.1)
                # if len(common_follownig) == len(current_cluster):
                #     opinion_leaders.append(common_follownig)
                #     break
                if len(common_follownig) > leaders_num:
                    current_cluster = common_follownig
                
                elif len(common_follownig) > 0:
                    opinion_leaders.append(common_follownig)
                    break
                else:
                    opinion_leaders.append(current_cluster)
                    break
        
    for i in opinion_leaders:
        print(i)
    return opinion_leaders


listname_path = 'listname_of_all.csv'
usersA = []

with open(listname_path, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[1] == '':
            row[1] = 'A'
        usersA.append(row[1])


threshold = 0.4
leaders_num =6
whole = list(range(540))
filenames = readFileName()
json_merge, all_congressman = jsonMerge(filenames)
whole_matrix = buildMatrix(json_merge, all_congressman).T
listname = usersA
# clusters_index, clusters, cluster_num  = get_clusters(whole, whole_matrix,listname,threshold)
# print(clusters_index)
opinion_leaders = find_opinion_leader(whole, whole_matrix,listname, leaders_num, threshold)



