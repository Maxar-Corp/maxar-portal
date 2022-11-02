# Search

----

## Search

### **Args:**

#### search (*str*):

  The desired search term.
  
  On an account level the function will search through account numbers, account names, SAP license ids, sold to, and licensees. 
  
  On an activation level the function will search through activation numbers, SAP contract identifiers, SAP line items, start dates, end dates, activation numbers, and activation ids. 
  
  On a user level the function will search through usernames, roles, activation numbers, and account numbers.
  
  *Examples:*
  
	interface.Search('account', 'My Account Name')
   
	interface.Search('activation', 'My Activation Name')
   
	interface.Search('user', 'My User')
