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
GROUP BY product.product_id