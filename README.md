# This script is used to create an XML file from data in a SQLite database. 
This script exports data from an SQLite database and creates an XML file with the data. It uses Python's built-in sqlite3 and xml.etree.ElementTree modules to connect to the database, query the data and create the XML file.

# Getting started
These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

# Prerequisites
+ Python 3
+ SQLite3

# Installing
1. Clone this repository to your local machine
`git clone https://github.com/Asatillo/butopea_xml_generator.git`

2. Make sure the database file you want to export the data from is in the same directory as the script and the name of the file is specified in the configs.py file.

3. Run the script
`python generator.py`

# Script Description
The script exports data from an SQLite database using the `make_query()` function that takes the name of the database file as an argument, creates a connection, a cursor and executes the query. The query returns the data in the form of a list of tuples.

The `get_xml()` function takes the result of the query and creates an XML file with the data. It uses `xml.etree.ElementTree` module to create the structure of the XML file and writes it to a file with the name specified as an argument.

# Built With
+ Python 3 - The programming language
+ SQLite3 - The database management system
+ xml.etree.ElementTree - The module used to create the XML file

# Additional notes
+ The script uses the `configs.py` file to import the name of the database file and the name of the XML file to be created.
+ The script uses the `if __name__ == "__main__":` block to run the `get_xml()` function when the script is executed.
+ The script uses the `with open(filename_save, 'wb') as f:` block to write the XML file.
