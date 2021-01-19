import urllib.parse
import urllib.request
import urllib.response
import json

def get_metadata_author(author: str) -> dict:
    """
    Render resource author in JSON format,
    convert JSON string to Pythonic object
    """
    url = f"http://dbpedia.org/data/{author}.json"
    # format author into URL
    request = urllib.request.urlopen(url)
    request = request.read()
    request_dictionary = json.loads(request)
    for key, value in request_dictionary.items():
        if key == f"http://dbpedia.org/resource/{author}":
            # this is the "master key"
            metadata_author_dictionary = value
            # the value of this key is again a dictionary
    return metadata_author_dictionary

def get_abstract_author(metadata_author_dictionary: dict) -> str:
    """
    Iterate through metadata author dictionary,
    return abstract of the author
    """
    if "http://dbpedia.org/ontology/abstract" in metadata_author_dictionary:
        # account for the possibility of an abstract of the author not being available
        for key, value in metadata_author_dictionary.items():
            if key == "http://dbpedia.org/ontology/abstract":
                # the abstract of the author can be found under this key
                list_of_abstracts = value
                # the value of this key is a list of dictionaries
                for abstract_dictionary in list_of_abstracts:
                    for key, value in abstract_dictionary.items():
                        # each dictionary contains two keys:
                        # "value": the actual abstract
                        # "lang": the language of the abstract
                        if key == "lang":
                            language = value
                            if language == "en":
                                # extract only the abtract in English
                                for key, value in abstract_dictionary.items():
                                    if key == "value":
                                        abstract_author = value
                                        print("\n")
                                        print("Abstract author", ":", abstract_author)
        return abstract_author
    else:
        print("\n")
        print("Abstract author: Author abstract not found.")
        print("\n")
