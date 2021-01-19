Information Science: exam project
Olga van der Burgh

For this project, I have built a program that accepts user input of a book title (e.g. "To Kill a Mockingbird",
"Pride and Prejudice", "Harry Potter and the Philosopher's Stone"). The program makes a call to the DBpedia lookup API,
searching for book titles that contain the search term. The API response is XML, which will be converted to a JSON string,
which will then be converted to a Pythonic object. For this task, I make use of the third-party library xmltodict.
The program then iterates over the pythonic object, and returns all titles found in the form of a list. The user is then asked to
copy-paste the title that they want to look up. The resource of this title, which is rendered in JSON format, is converted to a pythonic object. By iterating over the Pythonic object, the program collects metadata about the book: the title, the publication date, the author, and an abstract. As this is linked data, the program will use the metadata about the book to collect metadata about the author in the form of an abstract. 

Third-party libraries used: xmltodict.
