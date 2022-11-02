import json
import requests
import MPS_Portal_SDK.process as process


class Address:

    def __init__(self, auth):
        self.base_url = auth.base_url
        self.response = None
        self.version = auth.version
        self.auth = auth

    def GetAddress(self, address_id):
        """
        Function lists an address' details
        Args:
            address_id (int) = ID of the address
        Returns:
            Dictionary of the desired address' details
        """

        authorization = process.authorization(self.auth)
        url = self.base_url + '/accountservice/api/v1/addresses/{}'.format(address_id)
        response = requests.request("GET", url, headers=authorization, verify=False)
        process_response = process._response_handler(response)
        return response.json()

    def AddAddress(self, city, country, postal_code, state, street1, **kwargs):
        """
        Function creates a new address
        Args:
            city (string) = Desired city for the new address. Must have correct capitalization
            country (string) = Desired country for the new address. Must have correct capitalization
            postal_code (string) = Desired postal/zip code for the new address. Must be in 5 digit format
            state (string) = Desired state for the new address in abbreviated form. Must be capitalized
            street1 (string) = Desired street address for the new address
        Kwargs:
            phone (string) = Desired phone number for the new address. Must be in XXX-XXX-XXXX form
            streetAddress2 (string) = Desired secondary street address for the new address
        Returns:
            Dictionary of the new address' details
        """

        authorization = process.authorization(self.auth)
        url = self.base_url + '/accountservice/api/v1/addresses'
        payload = {
            "city": city.title(),
            "country": country.title(),
            "postalCode": postal_code,
            "state": state.upper(),
            "streetAddress1": street1
        }
        for item in kwargs.keys():
            if item == "phone" and len(kwargs[item]) != 12:
                raise Exception("{} is not a valid phone number. "
                                "Phone number must be 10 digits long and separated by two hyphens".format(kwargs[item]))
            payload.update({item: kwargs[item]})
        payload = json.dumps(payload)
        response = requests.request("POST", url, headers=authorization, data=payload, verify=False)
        process_response = process._response_handler(response)
        return response.json()

    def UpdateAddress(self, address_id, **kwargs):
        """
        Function updates an existing address' details
        Args:
            address_id (int) = ID of the address
        Kwargs:
            city (string) = Desired city for the new address. Must have correct capitalization
            country (string) = Desired country for the new address. Must have correct capitalization
            postalCode (string) = Desired postal/zip code for the new address. Must be in 5 digit format
            state (string) = Desired state for the new address in abbreviated form. Must be capitalized
            phone (string) = Desired phone number for the new address. Must be in XXX-XXX-XXXX form
            streetAddress1 (string) = Desired street address for the new address
            streetAddress2 (string) = Desired secondary street address for the new address
        Returns:
            Dictionary of the updated address' details
        """

        authorization = process.authorization(self.auth)
        url = self.base_url + '/accountservice/api/v1/addresses/'
        address_info = self.GetAddress(address_id)
        payload = {
            "id": address_info["id"],
            "streetAddress1": address_info["streetAddress1"],
            "streetAddress2": address_info["streetAddress2"],
            "city": address_info["city"],
            "country": address_info["country"],
            "state": address_info["state"],
            "postalCode": address_info["postalCode"],
            "phone": address_info["phone"]
        }
        for item in kwargs.keys():
            if item == "id":
                raise Exception("Address ID cannot be updated")
            if item == "phone" and len(kwargs[item]) != 12:
                raise Exception("{} is not a valid phone number. "
                                "Phone number must be 10 digits long and separated by two hyphens".format(kwargs[item]))
            payload.update({item: kwargs[item]})
        payload = json.dumps(payload)
        response = requests.request("PUT", url, headers=authorization, data=payload, verify=False)
        process_response = process._response_handler(response)
        return response.json()

    def DeleteAddress(self, address_id):
        """
        Function deletes an address
        Args:
            address_id (int) = ID of the address
        Returns:
            Message of successfull deletion
        """

        authorization = process.authorization(self.auth)
        url = self.base_url + '/accountservice/api/v1/addresses?id={}'.format(address_id)
        response = requests.request("DELETE", url, headers=authorization, verify=False)
        process_response = process._response_handler(response)
        return "Address {} successfully deleted".format(address_id)