# PO_FA6-Social_Newwork

## There are 6 subtasks as following:

1、extract the Username from the Profile Page

2、get the UserA's tweets

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



##SubT1:extract the Username from the Profile Page

Go to the target's profile page to get the Username like "@Jerry" not "Jerry", with the file "List name of ...."


##SubT2:get the User's tweets

