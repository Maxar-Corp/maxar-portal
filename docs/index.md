# Maxar Portal Services

## Getting started

**MPS Portal SDK** is a Python library for accessing Maxar's Portal Services API endpoints to 
retrieve and manipulate services including account, activation and user access as well as OGC services
The connection is established using login credentials stored in a local config file.


Installation:

There are two options recommended for environment set up to utilize the **MPS Portal SDK**.

1. Installation of rasterio package for georeferencing geotiff files.
	* First install the [Microsoft C++ Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
	* Create a conda environment with the `gdal`, `rasterio`, and `shapely` packages:
		
		Example: ``conda create -n <environment_name> python=3.7 gdal rasterio shapely``
		
	* Proceed with standard pip installation below
		
2. Standard pip installation without the `gdal`, `rasterio`, and `shapely` packages.

	Example: ``pip install Maxar-Portal-SDK``
	
	*Note: Mosaicing images is still available with this installation option but geotiff files will NOT be georeferenced. See [Download Full Resolution](ogc/get_full_res_image) and [Create Mosaic](ogc/create_mosaic)*

Config File

We recommend creating a credentials file to store your login information for future sessions in one of two ways. 

* Use the command line interface command ``config`` from the command prompt and follow the prompts. See [Command Line Interface](ogc/cli_commands)
* Create a credentials file called ``.MPS-config`` in your home directory with the following format:

			[mps] 
			user_name=<your-user-name>
			user_password=<your-password>

After creating your config file, you are now ready to start with the following guides:

  * [Quickstart Guide for OGC](ogc/quickstart) 
  * [Quickstart Guide for Admin](account-services/quickstart)