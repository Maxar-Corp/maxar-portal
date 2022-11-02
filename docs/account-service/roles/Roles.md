# Role

----

## Create Role

### **Args:**

#### name (*str*):

  The desired name for the newly created role
  
  *Example:*
  
	interface.roles.CreateRole(name="My new role")

----

## Update Role

### **Args:**

#### id (*int*):

  The identifier of the desired role
  
  *Example:*
  
	interface.roles.UpdateRole(id=1)

#### name (*str*):

  The name of the desired role
  
  *Example:*
  
	interface.roles.UpdateRole(name="My new role")

#### displayName (*str*):

  The desired display name of the role
  
  *Example:*
  
	interface.roles.UpdateRole(displayName="My role")

----

## Get Roles

  *Example:*
  
	interface.roles.GetRoles()

----

## Delete Role

### **Args:**

#### roleName (*str*):

  The name of the desired role
  
  *Example:*
  
	interface.roles.DeleteRole(roleName="My role")
