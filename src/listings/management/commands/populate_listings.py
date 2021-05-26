import csv, datetime
from typing import Optional, Union

from django.core.management import BaseCommand
from api.models import Listing, ZillowEstimate

class Command(BaseCommand):
    help = 'Load a listings csv file into db'

    @staticmethod
    def convert_string_to_date(string: str, 
            input_format: Optional[str] = '%m/%d/%Y', 
            output_format: Optional[str] = '%Y-%m-%d') -> Union[str, None]:
        if string:
            return datetime.datetime.strptime(string, input_format).strftime(output_format)
        return None

    @staticmethod
    def handle_empty_string(string: str) -> Union[str, None]:
        if not string:
            return None
        return string

    def add_arguments(self, parser) -> None:
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs) -> None:
        path = kwargs['path']
        
        if (listings:= Listing.objects.all()):
            listings.delete()

        with open(path, 'rt') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                zestimate = ZillowEstimate.objects.create(
                    zillow_id=row[18],
                    rentzestimate_amount=self.handle_empty_string(row[11]),
                    rentzestimate_last_updated=self.convert_string_to_date(row[12]), 
                    zestimate_amount=self.handle_empty_string(row[16]),
                    zestimate_last_updated=self.convert_string_to_date(row[17])
                )

                listing = Listing.objects.create(
                    area_unit=row[0],
                    bathrooms=self.handle_empty_string(row[1]),
                    bedrooms=self.handle_empty_string(row[2]),
                    home_size=self.handle_empty_string(row[3]),
                    home_type=row[4],
                    last_sold_date=self.convert_string_to_date(row[5]),
                    last_sold_price=self.handle_empty_string(row[6]),
                    link=self.handle_empty_string(row[7]),
                    price=self.handle_empty_string(row[8]),
                    property_size=self.handle_empty_string(row[9]),
                    rent_price=self.handle_empty_string(row[10]),
                    zillow_details=zestimate,
                    tax_value=self.handle_empty_string(row[13]),
                    tax_year=row[14],
                    year_built=row[15],
                    address=row[19],
                    city=row[20],
                    state=row[21],
                    zipcode=row[22]
                )
                    