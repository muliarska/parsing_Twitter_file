# parsing_Twitter_file
A list of Donald Trump's friends on Twitter is displayed. 
The user must select the friend for whom he wants to receive the information. 
Then the user has to enter the key to get information on it (examples of keys that the user can select are displayed).
As a result, the user receives the information contained in the file 'friends.json' under a given key. 
If there is no such information about the friend, the program outputs: "No information provided by user".
If this key does not exist in the dictionary, the program outputs: "There is no such key in the file".
The user must press "Enter" to exit.

### An example of running the program:
```
Your friends' screen names: JudgeJeanine, Jim_Jordan, MariaBartiromo, VP, GOPChairwoman, parscale, PressSec, TuckerCarlson, JesseBWatters, WhiteHouse
Enter screen name of the friend for who you want to receive information: Jim_Jordan
Enter the key for receiving information (examples: id, id_str, name, screen_name,
location, description, url, expanded_url, followers_count, friends_count,
favourites_count, profile_image_url, etc.): description
Result: Proudly serving Ohio's beautiful fourth district. Ranking Member on @GOPoversight. Fighting to #DoWhatWeSaid
Press Enter to exit
```
### Conclusion:
This module creates fast and convenient navigation for json file 'friends.json' obtained through the Twitter API.
In addition to this, it provides access to the keys of various friends of the user.

## Author: Yana Muliarska
