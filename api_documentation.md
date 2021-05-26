# Listings API
The API allows you to create, update, and delete ```Listing``` objects. You can also retrieve individual listings as well as a list of all listings.
  

## Endpoints

| Method | Endpoint           | Description        |
| :------|:-------------------| :------------------|
| POST   | /v1/listings/      | create listing     |
| GET    | /v1/listings/:id   | retrieve a listing |
| PUT    | /v1/listings/:id   | update a listing   |
| DELETE | /v1/listings/:id   | delete a listing   |
| GET    | /v1/listings       | list all listings  |

  

## The Listing object

```json
{
    "id": 563,
    "area_unit": "SqFt",
    "bathrooms": 5.0,
    "bedrooms": 5,
    "home_size": 4607,
    "home_type": "SingleFamily",
    "last_sold_date": "2016-11-08",
    "last_sold_price": 2630000,
    "link": "https://www.zillow.com/homedetails/4159-Greenbush-Ave-Sherman-Oaks-CA-91423/20028492_zpid/",
    "price": "$2.63M",
    "property_size": 7972,
    "rent_price": null,
    "zillow_details": {
        "zillow_id": 20028492,
        "rentzestimate_amount": 11900,
        "rentzestimate_last_updated": "2018-08-07",
        "zestimate_amount": 3010997,
        "zestimate_last_updated": "2018-08-07"
    },
    "tax_value": 2630000.0,
    "tax_year": "2017",
    "year_built": "2013",
    "address": "4159 Greenbush Ave",
    "city": "Sherman Oaks",
    "state": "CA",
    "zipcode": "91423"
}
```
  

### Important Attributes

>**bathrooms** | float
>- Number of bathrooms.
>-----
>**bedrooms** | int
>- Number of bedrooms.
>-----
>**home_size** | int
>- Size of listing in square feet.
>-----
>**home_type** | string
>- Type of listing (single family, condominium, etc).
>-----
>**last_sold_price** | int
>- Price (in USD) the listing was last sold for.

....  
....  
....  
and so on ...


## Mandatory fields

Mandatory fields for creating and updating Listing objects are:
   >address  
   >city  
   >state   
   >zipcode  

*note* I just picked some arbitrary fields to make mandatory here.

## API Calls

**Get a listing**
```shell
curl http://127.0.0.1:8000/v1/listings/447/ | python3 -m json.tool
```

**List all listings**
```shell
curl http://127.0.0.1:8000/v1/listings/ | python3 -m json.tool
```
...  
...  
...  
and so on ...