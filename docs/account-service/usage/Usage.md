# Usage

----

## Get Usage

### **Args:**

#### activation_id (*int*):

  The identifier for the desired activation
  
  *Example:*
  
	interface.usage.get_usage(activation_id=1)

----

## Get Usage Allowed

### **Args:**

#### activation_id (*int*):

  The identifier for the desired activation
  
  *Example:*
  
	interface.usage.get_usage_allowed(activation_id=1)

----

## Get Usage Allowed Download

### **Args:**

#### bbox (*str*):

  The AOI of the desired area. Only works with EPSG:4326 at this time. Bbox must be in miny,minx,maxy,maxx format
  
  *Example:*
  
	interface.usage.get_usage_download(bbox="39.702432,-105.026207,39.763686,-104.941750")

#### productId (*str*):

  The identifier of the desired product
  
  *Example:*
  
	interface.usage.get_usage_download(productId="1")

#### activation_id (*int*):

  The identifier of the desired activation
  
  *Example:*
  
	interface.usage.get_usage_download(activation_id=1)

----

## Get Usage Overview

  *Example:*
  
	interface.usage.get_usage_overview()
