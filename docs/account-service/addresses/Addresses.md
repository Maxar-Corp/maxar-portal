# Address

----

## Add Address

### **Args:**

#### city (*str*):

  The desired city for the newly created address. Must have correct capitalization
  
  *Example:*
  
	interface.address.AddAddress(city="Denver")

#### country (*str*):

  The desired country for the newly created address. Must have correct capitalization
  
  *Example:*
  
	interface.address.AddAddress(country="United States of America")

#### postal_code (*str*):

  The desired postal code for the newly created address. Must be in 5 digit format
  
  *Example:*
  
	interface.address.AddAddress(postal_code="80211")

#### state (*str*):

  The desired state for the newly created address. Must be in abbreviated form and capitalized
   
  *Example:*
   
	interface.address.AddAddress(state="CO")

#### street1 (*str*):

  The desired street address for the newly created address
  
  *Example:*
  
	interface.address.AddAddress(street1="1234 Fake Street")

### **Kwargs:**

#### phone (*str*):

  The desired phone number for the newly created address. Must be in XXX-XXX-XXXX format
  
  *Example:*
  
	interface.address.AddAddress(phone="123-456-7890")

#### streetAddress2 (*str*):

  The desired secondary street address for the newly created address
  
  *Example:*
  
	interface.address.AddAddress(streetAddress2="123 Other Street")

----

## Update Address

### **Args:**

#### address_id (*int*):

  The identifier for the desired address
  
  *Example:*
  
	interface.address.UpdateAddress(address_id=1)
   
### **Kwargs:**

#### city (*str*):

  The city for the desired address. Must have correct capitalization
  
  *Example:*
  
	interface.address.UpdateAddress(city="Denver")

#### country (*str*):

  The country for the desired address. Must have correct capitalization
  
  *Example:*
  
	interface.address.UpdateAddress(country="United States of America")

#### postal_code (*str*):

  The postal code for the desired address. Must be in 5 digit format
  
  *Example:*
  
	interface.address.UpdateAddress(postal_code="80211")

#### state (*str*):

  The state for the desired address. Must be in abbreviated form and capitalized
   
  *Example:*
   
	interface.address.UpdateAddress(state="CO")

#### street1 (*str*):

  The street address for the desired address
  
  *Example:*
  
	interface.address.UpdateAddress(street1="1234 Fake Street")

#### phone (*str*):

  The phone number for the desired address. Must be in XXX-XXX-XXXX format
  
  *Example:*
  
	interface.address.UpdateAddress(phone="123-456-7890")

#### streetAddress2 (*str*):

  The secondary street address for the desired address
  
  *Example:*
  
	interface.address.UpdateAddress(streetAddress2="123 Other Street")

----

## Get Address

### **Args:**

#### address_id (*int*):

  The identifier of the desired address
  
  *Example:*
  
	interface.address.GetAddress(address_id=1)

----

## Delete Address

### **Args:**

#### address_id (*int*):

  The identifier for the desired address
  
  *Example:*
  
	interface.address.DeleteAddress(address_id=1)
