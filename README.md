This script is used to create an XML file from data in a SQLite database. 

If the script is run as the main program, the get_xml() function is called with the predefined XML_FILENAME.
+ ID [id]
+ Title [title]
+ Description [description]
+ Link [link] 
+ Image link [image_link]
+ Additional image link [additional_image_link]
+ Availability [availability]
+ Price [price]
+ Brand [brand]
+ Condition [condition]

Additional details:
+ The field values included in the product feed conform to Google Merchant specifications
+ Disabled products (with status `0`) are not included in the feed 
+ All prices are in Hungarian Forints (HUF)
+ Brand represents the product manufacturer
+ All products are sold as new
+ The base domain for product image URLs is `butopea.com`, for example: [`https://butopea.com/image/catalog/DEJEL-NS3TE[D]_1.jpg`](https://butopea.com/image/catalog/DEJEL-NS3TE%5BD%5D_1.jpg)
+ Additional images are loaded in their respective sort orders
+ The product link is constructed by appending the product ID to `https://butopea.com/p/`, for example: [`https://butopea.com/p/3927`](https://butopea.com/p/3927)

The script includes two main functions: make_query(database) and get_xml(filename_save).

The varibles database and filname_save are taken from the config.py, from variables DATABASE_FILE and XML_FILENAME accordingly.

The make_query(database) function connects to the specified SQLite database and creates a cursor. It then executes a query to select specific data from the "product", "product_image", "product_description", and "manufacturer" tables, and returns the result as a list of tuples.

The get_xml(filename_save) function takes the data from the make_query() function and creates an XML file with the data. It first creates the root element "products" and then iterates through each product in the data, creating a "product" sub-element for each product. Within each "product" element, it creates sub-elements for specific data such as "id", "title", "description", "link", "image_link", "additional_image_link", "availability", "price", "brand", and "condition". The resulting XML file is saved to the specified filename.

To run a script, navigate to the script's directory and run a command:
python generator.py

*For the sake of safety, the database file is removed from the directory and needs to be added into for testing. The file must have a name 'data.sqlite'.
