# PO_FA6-Social_Network

## There are 6 subtasks as following:

1、extract the Username from the Profile Page

2、get the tweets

3、get the list of follwers and followings of UserA

4、construct the social network between the targets

5、develop the webdemo

6、Prepare for the presentation



This assignment is based on the project:https://github.com/Altimis/Scweet. If you want to use the code , please pay attention to the MIT Liensence of the Altimis's project.Here are the steps:

Step1: download the source code from the link or download it as python library:

```python
pip3 install Scweet==1.6
```

Ps: If you download it with command pip3,  please pay attention to the function Log_in() in the file Utils.py.Due to the log_in page on twitter changed,  Scweet 1.6 couldn't work as you wish.  You'd better change the Utils.py with the same one of this:https://github.com/Altimis/Scweet

Step2: call the functions

With the code as an example, you could collect tweets within the limitation.

```python
from Scweet.scweet import scrape

data = scrape(words=['bitcoin','ethereum'], since="2021-10-01", until="2021-10-05", from_account = None,interval=1, headless=False, display_type="Top", save_images=False, lang="en",resume=False, filter_replies=False, proximity=False)

```

ps: "data" above  is pd.dataframe, so you can use some packages to save it as .csv or .json and more formats.

With the code as an example, you could collect followers and followings.(Two functions return the dictionary.)

```python
from Scweet.user import get_user_information, get_users_following, get_users_followers
users = ['@username']
env_path = ".env"

following = get_users_following(users=users, env=env_path, verbose=0, headless=False, wait=2, limit=50, file_path=None)

followers = get_users_followers(users=users, env=env_path, verbose=0, headless=False, wait=2, limit=50, file_path=None)
```

ps:The file '.env' should include  your twitter account imformation, required to log in with the Selenium. You need to edit it and save it in the root directory of the project.

```python
# file_name = '.env'
SCWEET_USERNAME=your username
SCWEET_PASSWORD=your password
```



### SubT1:extract the Username from the Profile Page

Go to the target's profile page to get the Username like "@Jerry" not "Jerry", with the file "List name of ...."


### SubT2:get the tweets
Before the starting the subtask, we have to know how to set three parameters 'from account','to account'and 'mention account' in the func:scrape() 

#### Cond1:if you want to get tweets by User1 to User2, set from_account = User1, to_account = User2.  

Here are an example:

<img width="297" alt="截屏2021-12-07 下午7 26 19" src="https://user-images.githubusercontent.com/63695492/145022637-cb0735b5-5db7-4f25-8bc5-1fe6f49771eb.png">
In this example, with the code as following:

```python
data = scrape(since="2021-12-05", until="2021-12-06", from_account = 'Bugeater12',to_account='SenatorFischer', interval=1,headless = False,display_type="Top", save_images=False, lang="en",resume=False, filter_replies=False, proximity=False)
```

you could get this:
<img width="956" alt="截屏2021-12-07 下午7 27 45" src="https://user-images.githubusercontent.com/63695492/145022250-4c00f485-d2f7-4f42-b41e-0c7822bc3c5f.png">

#### Cond2:if you want to get tweets by User1, where User2 are mentioned, set from_account = User1, mention_account = User2

Here are an example:

<img width="437" alt="截屏2021-12-07 下午7 42 24" src="https://user-images.githubusercontent.com/63695492/145023252-8149ac62-ee04-4094-bdd6-e215dcf4bd08.png">
In this example, with the code as following:

```python
data = scrape(since="2021-12-04", until="2021-12-05", from_account = 'SenatorFischer',to_account='growneb', interval=1,headless = False,display_type="Top", save_images=False, lang="en",resume=False, filter_replies=False, proximity=False)
```

you could get this tweet finally.

#### Cond3:if you want to get tweets by someone you don't care, where User1 & User2 are mentioned together.However, setting mention_account(not accounts) = User1,User2 is not practical, but we could set the parameter words = [User1, User2].

Here are an example(here, the senator is the one that we don't care):

<img width="438" alt="截屏2021-12-07 下午7 59 22" src="https://user-images.githubusercontent.com/63695492/145025334-fa0b9643-fb3d-4948-a740-94653f7824cd.png">

```python
data = scrape(since="2021-11-17", until="2021-11-18", from_account = 'SenatorFischer',words =['ASA_Soybeans','UsChamber'], interval=1,headless = False,display_type="Top", save_images=False, lang="en",resume=False, filter_replies=False, proximity=False)
```

you could get this tweet finally.

Now, we discuss how to get the tweets where User1 and User2 appear together. Maybe, we can also divide it in 3 conditions: 

(1)User1 tweets, and User2 is mentioned in User1's tweet; 

(2)User1 tweets, and User2 reply to User1's tweet as a comment;

(3)Someone tweets, and User1 & User2 are mentioned is the tweet.

In our project, we get the list of Sens & Reps. Then traverse all Sens & Reps as User1 and User2 in above 3 conditions, recycling 544 * (544 - 1) times in each one.
### SubT3:get the followings(&followers)
