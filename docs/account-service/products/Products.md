# Product

----

## Create Products

### **Args:**

#### catalogType (*str*):

  The desired catalog type for the newly created product. Options are Archive or Online
   
  *Example:*
   
	interface.products.create_products(catalogType="Online")

#### productName (*str*):

  The desired name for the newly created product
  
  *Example:*
  
	interface.products.create_products(productName="My New Product")

#### productCategory (*str*):

  The desired product category for the newly created product
  
  *Example:*
  
	interface.products.create_products(productCategory="Vivid Standard")

#### usageType (*str*):

  The desired usage type for the newly created product. Options are Download or Streaming
  
  *Example:*
  
	interface.products.create_products(usageType="Streaming")

#### age (*str*):

  The desired age for the newly created product (defaults to None).
  
  *Example:*
  
	interface.products.create_products(age="5")

----

## Get Products

  *Example:*
  
	interface.products.get_products()

----

## Filter Products

### **Args:**

#### productCategory (*str*):

  The desired product category to filter by (defaults to None).
  
  *Example:*
  
	interface.products.filter_products(productCategory="Vivid Standard")

#### usageType (*str*):

  The desired usage type to filter by. Options are Download or Streaming (defaults to None).
  
  *Example:*
  
	interface.products.filter_products(usageType="Streaming")

#### age (*str*):

  The desired age to filter by (defaults to None).
  
  *Example:*
  
	interface.products.filter_products(age="5")

#### catalogType (*str*):

  The desired catalog type to filter by. Options are Archive or Online (defaults to None).
   
  *Example:*
   
	interface.products.filter_products(catalogType="Online")

----

## Delete Products

### **Args:**

#### productId (*int*):

  The identifier for the desired product
  
  *Example:*
  
	interface.products.delete_products(productId=1)
