# Role

----

## Add Roles

### **Args:**

#### account_number (*str*):

  The number of the desired account
  
  *Example:*
  
	interface.account.AddRoles(account_number="ACC-123-456")

#### role_name (*str or list of strs*):

  The name or names of the desired role(s)
  
  *Example:*
  
	interface.account.AddRoles(role_name="AERIAL_CELLS")

----

## Get Roles

  *Example:*
  
	interface.account_info.GetRoles()

----

## Remove Roles

### **Args:**

#### account_number (*str*):

  The number of the desired account
  
  *Example:*
  
	interface.account.RemoveRoles(account_number="ACC-123-456")

#### role_name (*str or list of strs*):

  The name of the desired role
  
  *Example:*
  
	interface.account.RemoveRoles(role_name="AERIAL_CELLS")
