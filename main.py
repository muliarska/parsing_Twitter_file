import json


def json_to_dictionary(file_name):
    """
    (str) -> dict
    This function converts the json file to a dictionary
    and returns this dictionary.
    """
    f = open(file_name, encoding='utf-8')
    f_dict = json.load(f)
    return f_dict


def analyze_dictionary(name, user_key, f_dict):
    """
    (str, str, dict) -> object (str, int, list or dict, etc.)
    This function accepts the nickname of a friend for whom
    it will return information (name), the key (user_key)
    and a dictionary. The function returns information
    if present and retrieved "No information provided by user"
    if not. If no such key exists, the function returns
    "There is no such key in the file"
    """
    for friend in f_dict["users"]:
        if friend["screen_name"] == name:
            for i in friend:
                if i == user_key:
                    result = friend[user_key]
                    if result != [] and result != "" and result is not None:
                        return result
                    else:
                        return "No information provided by user"

            if "url" in friend["entities"]:
                if user_key == "urls":
                    result = friend["entities"]["url"]["urls"]
                    if result != [] and result != "" and result is not None:
                        return result
                    else:
                        return "No information provided by user"

                for j in friend["entities"]["url"]["urls"][0]:
                    if j == user_key:
                        result = friend["entities"]["url"]["urls"][0][user_key]
                        if result != [] and result != "" and \
                                result is not None:
                            return result
                        else:
                            return "No information provided by user"

            for el in friend["status"]:
                if el == user_key:
                    result = friend["status"][el]
                    if result != [] and result != "" and result is not None:
                        return result
                    else:
                        return "No information provided by user"

                if el == "entities":
                    for k in friend["status"][el]:
                        if k == user_key:
                            result = friend["status"][el][k]
                            if result != [] and result != "" and \
                                    result is not None:
                                return result
                            else:
                                return "No information provided by user"

    return "There is no such key in the file"


if __name__ == '__main__':
    f_dict = json_to_dictionary('friends.json')
    name_lst = []
    for friend in f_dict["users"]:
        name_lst.append(friend["screen_name"])

    name_str = ''
    for i in name_lst:
        name_str += i + ', '

    print("Your friends' screen names: {}".format(name_str[:-2]))
    name = input("Enter screen name of the friend for who you want"
                 " to receive information: ")

    while True:
        print("Enter the key for receiving information (examples: id, "
              "id_str, name, screen_name,")
        print("location, description, url, expanded_url, followers_count, "
              "friends_count,")
        user_key = input("favourites_count, profile_image_url, etc.): ")
        if user_key == "":
            break
        print("Result:", analyze_dictionary(name, user_key, f_dict))
        print("Press Enter to exit\n\n")
