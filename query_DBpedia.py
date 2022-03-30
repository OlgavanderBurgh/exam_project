import urllib.parse
import urllib.request
import urllib.response
import xmltodict
import json

# CONSTANTS

DBPEDIA_PREFIX = "https://lookup.dbpedia.org/api/search/PrefixSearch?QueryString="
# DBpedia lookup API prefix

CODES = {}
CODES[401] = "Unauthorized."
CODES[404] = "Not able to find."
CODES[429] = "Too Many Requests."
CODES[500] = "Internal Server Error."
# HTTP status codes https://www.restapitutorial.com/httpstatuscodes.html

def clean(string: str) -> str:
    """
    Clean and URL encode input string
    """
    string = string.strip()
    # strip leading and trailing spaces
    string = string.casefold()
    # convert all uppercase characters characters to lowercase
    string = urllib.parse.quote(string)
    # replace all special characters using the %xx escape
    return string

def query_DBpedia(search: str) -> bytes:
    """
    Query DBpedia lookup API,
    return response or exit with error code
    """
    search = clean(search)
    query_class = "&QueryClass=book"
    # DBpedia class that the results should have
    url = DBPEDIA_PREFIX + search + query_class
    try:
        with urllib.request.urlopen(url) as query:
            return query.read()
    except urllib.error.HTTPError as HTTPerr:
        exit(CODES.get(HTTPerr.code))
    except urllib.error.URLError as URLerr:
        exit(URLerr)

def convert_XML_to_JSON(response: bytes) -> dict:
    """
    Parse XML response and convert it to a Python dictionary,
    convert Python dictionary to a JSON string,
    convert JSON string to a Pythonic object
    """
    response_dictionary = xmltodict.parse(response)
    response_dictionary = json.dumps(response_dictionary)
    response_dictionary = json.loads(response_dictionary)
    return response_dictionary
