from sys import get_coroutine_origin_tracking_depth
from scweet.user import get_user_information, get_users_following, get_users_followers
from scweet.scweet import scrape
import csv
import json
import numpy as np

listname_path = 'listname_of_all.csv'
listname_path_sen = 'listname_of_senators.csv'
usersA = []
usersB = []
with open(listname_path_sen, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[1] == '':
            row[1] = 'A'
        usersA.append(row[1])

with open(listname_path, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[1] == '':
            row[1] = 'A'
        usersB.append(row[1])


from_account_list = usersA
to_account_list = usersB
mention_account_list = usersB


#TODO remember to clear the unused list to change the save directory
save_dir = ""
if mention_account_list is not None:
    save_dir = "mention_outputs"
else:
    save_dir = "from_to_outputs"

#TODO add or remove the argument if necessary
data = scrape(since="2021-01-03", until="2021-12-03", from_accounts=from_account_list, mention_accounts=mention_account_list, interval=334, headless=False, display_type="Latest", save_images=False, save_dir=save_dir, resume=False, filter_replies=True, proximity=False)
'''
# i mention j
co_occur1 = np.zeros([100, len(users)])

for i in range(444,len(users)):
    for j in range(len(users)):
        if i == j:
            break
        useri = users[i]
        userj = users[j]
        print("%d-%d"%(i,j))
        data = scrape(since="2021-01-03", until="2021-12-03", from_account = useri,mention_account=userj, interval=7,headless = False,display_type="Top", save_images=False, lang="en",resume=False, filter_replies=False, proximity=False)
        co_occur1[i - 444,j] = data.size
#i reply to j
co_occur2 = np.zeros([100, len(users)])

for i in range(444,len(users)):
    for j in range(len(users)):
        if i == j:
            break
        useri = users[i]
        userj = users[j]
        print("%d-%d"%(i,j))
        data = scrape(since="2021-01-03", until="2021-12-03", from_account = useri,to_account=userj, interval=7,headless = False,display_type="Top", save_images=False, lang="en",resume=False, filter_replies=False, proximity=False)
        co_occur2[i-444,j] = data.size


#i & j occured in a tweet
co_occur3 = np.zeros([100, len(users)])
for i in range(444,len(users)):
    for j in range(len(users)):
        if i == j:
            break
        useri = users[i]
        userj = users[j]
        print("%d-%d"%(i,j))
        data = scrape(since="2021-01-03", until="2021-12-03", words = [useri,userj], interval=7,headless = False,display_type="Top", save_images=False, lang="en",resume=False, filter_replies=False, proximity=False)
        co_occur3[i-444,j] = data.size
'''