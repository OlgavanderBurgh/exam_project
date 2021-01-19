import pprint

def create_list_of_titles(response_dictionary: dict) -> list:
    """
    Iterate through response dictionary,
    return titles found
    """
    list_of_titles = []
    # create empty list
    for key, value in response_dictionary.items():
        if key == "ArrayOfResults":
            # this is the "master key"
            results_dictionary = value
            # the value of this key is again a dictionary
            for key, value in results_dictionary.items():
                list_of_results = value
                # the value of this dictionary is a list of dictionaries
                for result_dictionary in list_of_results:
                    for key, value in result_dictionary.items():
                        if key == "Label":
                            title = value
                            # the value of this key is the title of the book
                            list_of_titles.append(title)
                            # the title is appended to the list of titles
    print("\n")
    print("----------TITLES FOUND----------")
    print("\n")
    pprint.pprint(list_of_titles)
    print("\n")
    return list_of_titles

def choose_title(list_of_titles: list) -> str:
    """
    Let user choose a title they want to look up
    """
    chosen_title = ""
    # create empty string
    choice = input("Which of these titles would you like to look up? Please copy-paste your choice (without quotation marks): ")
    # the title should be copy-pasted, otherwise the resource will not be found
    # i.e. the resource will not be found if the title is lowercase
    for title in list_of_titles:
        if title == choice:
            chosen_title = choice
            print("\n")
            print("Title", ":", chosen_title)
            chosen_title = chosen_title.replace(" ", "_")
            # replace all spaces by underscores
            # these must be underscores, otherwise the resource will not be found
    return chosen_title
