
import json

__json_path = './src/sample4.json'

def check_characters(input, *args, **kwargs):
    """
    Check if character buffer reads the same backwards as forwars.

    Args:
        input (string, float, int): the characters you want to check.

    Returns:
        bool: Returns True if it read the same backwards as forwards.
        bool: Return False if not.
    """

    ### check if the input parameter is a string and if it reads the same backwars as forwards ###
    if str(input).lower() == str(input).lower()[::-1]:
        return True
    else:
        return False

def check_characters_from_json(*args, **kwargs):
    """
    Check if character buffer reads the same backwards as forwars from a json file.

    Returns:
        list: Returns a list with True of False if the character buffer reads the same backwards as forwars.
    """
    ### get the json data ###
    with open(__json_path) as f:
        data = json.load(f)
    characters = [people.get('firstName') for people in data.get('people')]

    ### map check_characters function with characters to get True or False ###
    # return map(check_characters, characters)
    checks = [check_characters(character) for character in characters]

    return checks

if __name__ == "__main__":
    ### Test it ###

    ### uncomment the two lines below to check characters from json file ###
    check_json = check_characters_from_json()
    print(check_json)

    ### uncomment the two lines below t check characters manualy ###
    # check_manual = check_characters('madam')
    # print(check_manual)




