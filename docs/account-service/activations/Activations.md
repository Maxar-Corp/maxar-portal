# Activation

----

## Create Activation

### **Args:**

#### name (*str*):

  The desired name for the newly created activation
  
  *Example:*
  
	interface.activations.CreateActivation(name="My Activation")

#### accountId (*int*):

  The identifier of the account to tie the activation to
  
  *Example:*
  
	interface.activations.CreateActivation(accountId=1)

#### activationTypeId (*int*):

  The identifier of the type of activation for the newly created activation
  
  *Example:*
  
	interface.activations.CreateActivation(activationTypeId=15001)

#### startDate (*str*):

  The desired start date for the newly created activation in yyyy-mm-dd format
  
  *Example:*
  
	interface.activations.CreateActivation(startDate="2022-10-31")

#### sapContractId (*str*):

  The desired SAP contract identifier. Must be 10 digits
  
  *Example:*
  
	interface.activations.CreateActivation(sapContractId="1234567890")

#### sapLineItem (*str*):

  The desired SAP line item. Must be 6 digits
  
  *Example:*
  
	interface.activations.CreateActivation(sapLineItem="123456")

#### rateTableId (*int*):

  The identifier of the desired rate table to tie to the newly created activation
  
  *Example:*
  
	interface.activations.CreateActivation(rateTableId=1)

### **Kwargs:**

#### creatorName (*str*):

  The desired name of the creator of the activation
  
  *Example:*
  
	interface.activations.CreateActivation(creatorName="Ben Kenobi")

#### endDate (*str*):

  The desired end date of the activation in yyyy-mm-dd format
  
  *Example:*
  
	interface.activations.CreateActivation(endDate="2022-12-25")

#### roles (*lst(str)*):

  The desired role or roles to be tied to the activation
  
  *Example:*
  
	interface.activations.CreateActivation(roles=["ARCHIVE_ORDERING"])

#### notes (*str*):

  Any desired notes to display within the activation
  
  *Example:*
  
	interface.activations.CreateActivation(notes="These are not the droids you are looking for")

#### imageryHoldbackValue (*str*):

  The desired value of the imagery holdback. Co-dependent with imageryHoldbackUnits
  
  *Example:*
  
	interface.activations.CreateActivation(imageryHoldbackValue="24")

#### imageryHoldbackUnits (*int*):

  The desired units of the imagery holdback. Available options are 0 - hours, 1 - days, 2 - months, 3 - years. Co-dependent with imageryHoldbackValue
  
  *Example:*
  
	interface.activations.CreateActivation(imageryHoldbackUnits=0)
	
----

## Update Activation

### **Args:**

#### activationId (*int*):

  The identifier for the desired activation
  
  *Example:*
  
	interface.activations.UpdateActivation(activationId=1)
   
### **Kwargs:**

#### name (*str*):

  The name of the desired activation
  
  *Example:*
  
	interface.activations.UpdateActivation(name="My Activation")

#### accountId (*int*):

  The identifier of the account to tie the activation to
  
  *Example:*
  
	interface.activations.UpdateActivation(accountId=1)

#### activationTypeId (*int*):

  The identifier of the type of activation for the newly created activation
  
  *Example:*
  
	interface.activations.UpdateActivation(activationTypeId=15001)

#### startDate (*str*):

  The desired start date for the newly created activation in yyyy-mm-dd format
  
  *Example:*
  
	interface.activations.UpdateActivation(startDate="2022-10-31")

#### sapContractId (*str*):

  The desired SAP contract identifier. Must be 10 digits
  
  *Example:*
  
	interface.activations.UpdateActivation(sapContractId="1234567890")

#### sapLineItem (*str*):

  The desired SAP line item. Must be 6 digits
  
  *Example:*
  
	interface.activations.UpdateActivation(sapLineItem="123456")

#### rateTableId (*int*):

  The identifier of the desired rate table to tie to the newly created activation
  
  *Example:*
  
	interface.activations.UpdateActivation(rateTableId=1)

#### endDate (*str*):

  The desired end date of the activation in yyyy-mm-dd format
  
  *Example:*
  
	interface.activations.UpdateActivation(endDate="2022-12-25")

#### roles (lst(*str*)):

  The desired role or roles to be tied to the activation
  
  *Example:*
  
	interface.activations.UpdateActivation(roles=["ARCHIVE_ORDERING"])

#### notes (*str*):

  Any desired notes to display within the activation
  
  *Example:*
  
	interface.activations.UpdateActivation(notes="Hello there")

#### imageryHoldbackValue (*str*):

  The desired value of the imagery holdback. Co-dependent with imageryHoldbackUnits
  
  *Example:*
  
	interface.activations.UpdateActivation(imageryHoldbackValue="24")

#### imageryHoldbackUnits (*int*):

  The desired units of the imagery holdback. Available options are 0 - hours, 1 - days, 2 - months, 3 - years. Co-dependent with imageryHoldbackValue
  
  *Example:*
  
	interface.activations.UpdateActivation(imageryHoldbackUnits=0)

----

## Get Activations

### **Args:**

#### activationId (*int*):

  The identifier of the desired activation (defaults to None).
  
  *Example:*
  
	interface.activations.GetActivations(activationId=1)

----

## Get Activation Types

  *Example:*
  
	interface.activations.GetActivationTypes()

----

## Get Activations For Account

### **Args:**

#### accountId (*int*):

  The identifier for the desired account
  
  *Example:*
  
	interface.activations.GetActivationsForAccount(accountId=1)

----

## Get Roles For Activation

### **Args:**

#### activationId (*int*):

  The identifier for the desired activation
  
  *Example:*
  
	interface.activations.GetRolesForActivation(activationId=1)

----

## Delete Activation

### **Args:**

#### activationId (*int*):

  The identifier of the desired activation
  
  *Example:*
  
	interface.activations.DeleteActivation(activationId=1)
