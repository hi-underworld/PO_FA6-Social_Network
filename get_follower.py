from scweet.user import get_user_information, get_users_following, get_users_followers
import csv
import json
env_path = '.env'
listname_path = 'listname_of_all.csv'

users = []
with open(listname_path, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        users.append(row[1])
#print(users)


'''
users_info = []
for i in range(100):
    print(users[i])
    target = []
    target.append(users[i])
    users_info.append(get_user_information(users = target, headless = False))
''' 
target = []
for i in range(67,456):
    print(users[i])
    print(i)
    target.append(users[i])
    if (len(target) == 10) or (i == len(users) - 1):
        followers = get_users_followers(users=target, env=env_path, verbose=0, headless=False, limit = 540, wait=2, file_path=None)
        target = []


#1-55,

#445-457
#458-467,468-477,478-487,488-497,498-507,508-517,518-527,528-537,538-544
#58-