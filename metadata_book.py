import urllib.parse
import urllib.request
import urllib.response
import json

def get_metadata(chosen_title: str) -> dict:
    """
    Render resource in JSON format,
    convert JSON string to Pythonic object
    """
    url = f"http://dbpedia.org/data/{chosen_title}.json"
    # format chosen title into URL
    request = urllib.request.urlopen(url)
    request = request.read()
    request_dictionary = json.loads(request)
    for key, value in request_dictionary.items():
        if key == f"http://dbpedia.org/resource/{chosen_title}":
            # this is the "master key"
            metadata_dictionary = value
            # the value of this key is again a dictionary
    return metadata_dictionary

def get_abstract(metadata_dictionary: dict) -> str:
    """
    Iterate through metadata dictionary,
    return abstract of chosen title in English
    """
    if "http://dbpedia.org/ontology/abstract" in metadata_dictionary:
        # account for the possibility of an abstract not being available
        for key, value in metadata_dictionary.items():
            if key == "http://dbpedia.org/ontology/abstract":
                # the abstract can be found under this key
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
                                        abstract = value
                                        print("\n")
                                        print("Abstract", ":", abstract)
        return abstract
    else:
        print("\n")
        print("Abstract: Abstract not found.")

def get_publication_date(metadata_dictionary: dict) -> str:
    """
    Iterate through metadata dictionary,
    return publication date of chosen title
    """
    if "http://dbpedia.org/ontology/publicationDate" in metadata_dictionary:
        # account for the possibility of a publication date not being available
        for key, value in metadata_dictionary.items():
            if key == "http://dbpedia.org/ontology/publicationDate":
                # the publication date can be found under this key
                list_of_publication_dates = value
                # the value of this key is a list of dictionaries
                for publication_date_dictionary in list_of_publication_dates:
                    for key, value in publication_date_dictionary.items():
                        if key == "value":
                            # the actual publication date can again be found under a key named "value"
                            publication_date = value
                            print("\n")
                            print("Publication date", ":", publication_date)
        return publication_date
    else:
        print("\n")
        print("Publication date: Publication date not found.")

def get_author(metadata_dictionary: dict) -> str:
    """
    Iterate through metadata dictionary,
    return author of chosen title
    """
    if "http://dbpedia.org/ontology/author" in metadata_dictionary:
        # account for the possibility of an author being unknown
        for key, value in metadata_dictionary.items():
            if key == "http://dbpedia.org/ontology/author":
                # the author URI can be found under this key
                list_of_authors = value
                # the value of this key is a list of dictionaries
                for author_dictionary in list_of_authors:
                    for key, value in author_dictionary.items():
                        if key == "value":
                            # the actual author URI can again be found under a key named "value"
                            author_URI = value
                            author = author_URI.rsplit('/', 1)[-1]
                            # extract the name of the author by splitting the URI at the last slash
                            # e.g. http://dbpedia.org/resource/J._K._Rowling -> J._K._Rowling
                            author_with_spaces = author.replace("_", " ")
                            # replace all underscores by spaces
                            print("\n")
                            print("Author", ":", author_with_spaces)
        return author
        # return the name of the author with underscores instead of spaces
    else:
        print("\n")
        print("Author: Author unkown.")
