import requests
import json
KEY='01dfe69bc87274425012abfce1b398f9'
ENDPOINT='http://api.openweathermap.org/geo/1.0/zip?zip={zipcode},{countrycode}&appid={key}'
def get_your_location(pin_code:str,country:str)-> str:
    end_point=ENDPOINT.format(zipcode=pin_code,countrycode=country,key=KEY)
    response=requests.get(end_point).content
    return response

if __name__ == '__main__':
    zipcode = input('Enter your pin code/zip code:')
    countrycode = input('Enter your country code:')
    response = get_your_location(zipcode,countrycode)
    print(type(response))
    print(structured_response.name)
