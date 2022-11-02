# Account 

----

## Create Account

### **Args:**

#### type (*str*):

  The desired type of account to create. Options are internal, revenue, contractor, education, free
  
  *Example:*
  
    interface.account.CreateAccount(type="internal")

#### name (*str*):

  The desired name of the newly created account
  
  *Example:*
  
    interface.account.CreateAccount(name="My Account")

### **Kwargs:**

#### sapLicenseId (*int*):

  The desired SAP license number to tie to the account
  
  *Example:*
  
    interface.account.CreateAccount(sapLicenseId=123456)

#### soldTo (*str*):

  The name of the person the contract was sold to
  
 *Example:*
  
    interface.account.CreateAccount(soldTo="Darth Vader")

#### licensee (*str*):

  The name of the purchaser of the resold content
  
  *Example:*
  
    interface.account.CreateAccount(licensee="Darth Sidious")

#### isActive (*bool*):

  Flag that dictates whether or not the account is activated upon creation (defaults to False).
  
  *Example:*
  
	interface.account.CreateAccount(isActive=True)

#### firstName (*str*):

  The desired first name of the contact for the account
      
  *Example:*
  
    interface.account.CreateAccount(firstName="Luke")
   
#### lastName (*str*):

  The desired last name of the contact for the account
  
  *Example:*
  
    interface.account.CreateAccount(lastName="Skywalker")
   
#### emailAddress (*str*):

  The desired email address of the contact for the account
  
  *Example:*
  
    interface.account.CreateAccount(emailAddress="jedimaster@alderaan.net")

#### country (*str*):

  The desired country of origin of the contact for the account
  
  *Example:*
  
    interface.account.CreateAccount(country="Tatooine")

#### phone (*str*):

  The desired phone number of the contact for the account
  
  *Example:*
  
    interface.account.CreateAccount(phone="123-456-7890")

----

## Update Account

### **Args:**

#### account_id (*int*):

  The identifier of the desired account
  
  *Example:*
  
    interface.account.UpdateAccount(account_id=1)

### **Kwargs:**

#### name (*str*):

  The desired name of the newly created account
  
  *Example:*
  
    interface.account.UpdateAccount(name="My Account)

#### sapLicenseId (*int*):

  The desired SAP license number to tie to the account
  
  *Example:*
  
    interface.account.UpdateAccount(sapLicenseId=123456)

#### soldTo (*str*):

  The name of the person the contract was sold to
  
  *Example:*
  
    interface.account.UpdateAccount(soldTo="Darth Vader")

#### licensee (*str*):

  The name of the purchaser of the resold content
  
  *Example:*
  
    interface.account.UpdateAccount(licensee="Darth Sidious")

#### isActive (*bool*):

  Flag that dictates whether or not the account is activated upon creation (defaults to False).
  
  *Example:*
  
    interface.account.UpdateAccount(isActive=True)

#### firstName (*str*):

  The desired first name of the contact for the account
      
  *Example:*
  
    interface.account.UpdateAccount(firstName="Luke")
   
#### lastName (*str*):

  The desired last name of the contact for the account
  
  *Example:*
  
    interface.account.UpdateAccount(lastName="Skywalker")
   
#### emailAddress (*str*):

  The desired email address of the contact for the account
  
  *Example:*
  
    interface.account.UpdateAccount(emailAddress="jedimaster@alderaan.net")

#### country (*str*):

  The desired country of origin of the contact for the account
  
  *Example:*
  
    interface.account.UpdateAccount(country="Tatooine")

#### phone (*str*):

  The desired phone number of the contact for the account
  
  *Example:*
  
    interface.account.UpdateAccount(phone="123-456-7890")

----

## Get Accounts

### **Args:**

#### accountId (*int*):

  The identifier of the desired account (defaults to None).
  
  *Example:*
  
    interface.account_info.GetAccounts(accountId=1)

#### accountName (*str*):

  The name of the desired account (defaults to None).
  
  *Example:*
  
    interface.account_info.GetAccounts(accountName="My Account")

#### accountNumber (*str*):

  The number of the desired account (defaults to None).
  
  *Example:*
  
    interface.account_info.GetAccounts(accountNumber="ACC-123-456")

#### id_names (*bool*):

  Flag that dictates whether or not to return a condensed list of account ids and account names (defaults to False).
  
  *Example:*
  
    interface.account_info.GetAccounts(id_names=True)

#### types (*bool*):

  Flag that dictates whether or not to return a list of all account types (defaults to False).
  
  *Example:*
  
    interface.account_info.GetAccounts(types=True)

----

## Delete Account

### **Args:**

#### account_id (*int*):

  The identifier of the desired account
  
  *Example:*
  
    interface.account.DeleteAccount(account_id=1)
