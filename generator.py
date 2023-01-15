from configs import *
import xml.etree.ElementTree as ET
import sqlite3

def make_query(database):
    """
    It connects to the database, creates a cursor, executes the query, and returns the result
    
    :param database: The name of the database file
    :return: A list of tuples.
    """
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    try:
        cursor.execute('''
        SELECT 
            product.product_id AS id,
            product_description.name AS title,
            product_description.description AS description,
            "https://butopea.com/p/" || product.product_id AS link,
            "https://butopea.com/" || product.image AS image_link,
            GROUP_CONCAT("https://butopea.com/" || product_image.image) AS additional_images,
            CASE 
                WHEN product.quantity>0 THEN "in_stock"
                ELSE "out_of_stock"
            END AS availability,
            ROUND(product.price, 2) || " HUF" AS price,
            manufacturer.name as brand,
            "new" AS condition
        FROM product
        LEFT JOIN product_image ON product.product_id = product_image.product_id
        LEFT JOIN product_description ON product.product_id = product_description.product_id
        LEFT JOIN manufacturer ON product.manufacturer_id = manufacturer.manufacturer_id
        WHERE status = "1"
        GROUP BY product.product_id''')

        return cursor.fetchall()
        
    except Exception as e: 
        print("An error occured", e)
        return []

def get_xml(filename_save):    
    """
    It takes the data from the SQLite database and creates an XML file with the data
    
    :param filename_save: The name of the file you want to save the XML to
    """
    root = ET.Element("products")
    
    products = make_query(DATABASE_FILE)
    for product in products:
        prod = ET.SubElement(root, "product")

        # + ID [id]
        id = ET.SubElement(prod, "id")
        id.text = product[0]

        # + Title [title]
        title = ET.SubElement(prod, "title")
        title.text = product[1]

        # + Description [description] 
        description = ET.SubElement(prod, "description")
        description.text = product[2]

        # + Link [link] It is easier to user this function rather than doing it in SQLite
        link = ET.SubElement(prod, "link")
        link.text = product[3]

        # + Image link [image_link]
        image_link = ET.SubElement(prod, "image_link")
        image_link.text = product[4]

        # + Additional image link [additional_image_link] if null then miss
        if product[5]: 
            additional_links = product[5].split(',')
            for link in additional_links:
                additional_image_link = ET.SubElement(prod, "additional_image_link")
                additional_image_link.text = link

        # + Availability [availability]
        availability = ET.SubElement(prod, "availability")
        availability.text = product[6]

        # + Price [price] 
        price = ET.SubElement(prod, "price")
        price.text = product[7]

        # + Brand [brand]
        brand = ET.SubElement(prod, "brand")
        brand.text = product[8]

        # + Condition [condition]
        condition = ET.SubElement(prod, "condition")
        condition.text = product[9]
        

    tree = ET.ElementTree(root)
    with open(filename_save, 'wb') as f:
        tree.write(f)


if __name__ == "__main__":
    get_xml(XML_FILENAME)