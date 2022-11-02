# Comment

----

## Add Comment

### **Args:**

#### account_id (*int*):

  The identifier of the desired account
  
  *Example:*
  
	interface.account_comment.AddComment(account_id=1)

#### author (*str*):

  The desired name of the author of the newly created comment
  
  *Example:*
  
	interface.account_comment.AddComment(author="Leia Organa")

#### message (*str*):

  The desired comment content
  
  *Example:*
  
	interface.account_comment.AddComment(message="Help me Obi-Wan Kenobi")

----

## Update Comment

### **Args:**

#### account_id (*int*):

  The identifier of the desired account
  
  *Example:*
  
	interface.account_comment.UpdateComment(account_id=1)

#### comment_id (*int*):

  The identifier of the desired comment
  
  *Example:*
  
	interface.account_comment.UpdateComment(comment_id=1)

### **Kwargs:**

#### author (*str*):

  The name of the author of the desired comment
  
  *Example:*
  
	interface.account_comment.UpdateComment(author="Leia Organa")

#### message (*str*):

  The desired comment content
  
  *Example:*
  
	interface.account_comment.UpdateComment(message="You're my only hope")

----

## Get Comment

  *Example:*
  
	interface.account_info.GetComment()

----

## Delete Comment

### **Args:**

#### account_id (*int*):

  The identifier of the desired account
  
  *Example:*
  
	interface.account_comment.DeleteComment(account_id=1)

#### comment_id (*int*):

  The identifier of the desired comment
  
  *Example:*
  
	interface.account_comment.DeleteComment(comment_id=1)
