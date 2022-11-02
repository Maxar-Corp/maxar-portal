# Rate Table

----

## Create Table

### **Args:**

#### name (*str*):

  The desired name for the newly created rate table
  
  *Example:*
  
	interface.rate_table.CreateTable(name="My Rate Table")

#### tables (*lst(lst)*)

  The desired credit ammount (*int*) and credit unit type id (*int*). List must include the same amount of tables as there are products. Must be in the following format: [[<credits>, <creditUnitTypeId>]]
  
  *Example:*
  
	rate_amts = [[100, 15003], [100, 15003], [100, 15003], [100, 15002], [100, 15003],  [100, 15002], [100, 15003],
            [100, 15004], [110, 15004], [100, 15002],  [100, 15000], [100, 15005], [100, 15003], [100, 15003],
            [100, 15002],  [100, 15004], [100, 15003], [100, 15003], [100, 15003], [100, 15003], [100, 15003],
            [100, 15003]]
  
	interface.rate_table.CreateTable(tables=rate_amts)

----

## Get Table

### **Args:**

#### table_id (*int*):

  The identifier of the desired rate table (defaults to None).
  
  *Example:*
  
	interface.rate_table_info.GetTable(table_id=1)
	
----

## Get Activations For Table

### **Args:**

#### table_id (*int*):

  The identifier for the desired rate table
  
  *Example:*
  
	interface.rate_table_info.GetActivationsForTable(table_id=1)

----

## Get Rate Amounts

### **Args:**

#### table_id

  The identifier for the desired rate table
  
  *Example:*
  
	interface.rate_table_info.GetRateAmounts(table_id=1)

----

## Get Credit Types

  *Example:*
  
	interface.rate_table_info.GetCreditTypes()

----

## Delete Table

### **Args:**

#### table_id (*int*):

  The identifier of the desired rate table
  
  *Example:*
  
	interface.rate_table.DeleteTable(table_id=1)
