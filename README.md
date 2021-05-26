# House Listings DRF API
This Repo contains code to support a REST API for house listings built with Django and Django Rest Framework.
## How to test the API

### Download requirements
First clone the repository locally, activate a virtual environment, and install the requirements
```shell
python -m venv env

source env/bin/activate

pip install -r requirements.txt
```

### Migrate
The initial migrations file is already made, you just need to migrate them to the database.
```shell
cd src/

python manage.py migrate
```

### Populate the DB

The database is initially populated with a csv file of house listings. That csv file can be found in ```src/listing_data.csv``` from the root directory.

The script to populate the database uses a Django management command. This can be found in ```src/listings/management/commands/populate_listings.py```

To populate the database, invoke this command (from the ```src``` directory) as:

```shell
python manage.py populate_listings --path listing_data.csv
```

### Runserver
You'll need to run the server in order to test the API.
```shell
python manage.py runserver
```

### Curl an endpoint

For example, to get details about a listing:
```shell
curl http://127.0.0.1:8000/v1/listings/447/ | python -m json.tool
```
You should see the following response in your terminal:
```shell
{
    "id": 447,
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

See ```api_documentation.md``` for more information. 

*note about the DJango secret key*: it is exposed because this is not a production project.