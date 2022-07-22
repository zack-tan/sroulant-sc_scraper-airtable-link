import pyairtable as pyat
from pyairtable import Api, Base, Table
from pyairtable import formulas as fm
import pandas as pd

API_KEY = 'xx'
BASE_ID = 'xx'

if __name__ == '__main__':
    # api = Api('key2RncEIzaX4d00l')
    # api.all('base_id', 'table_name')
    # base = Base('apikey', 'base_id')
    # base.all('table_name')

    # Read in data to import
    df = pd.read_csv("latest_month_cleaned.csv")

    # Initialize Airtable API connector
    table = Table(API_KEY, BASE_ID, 'Client_Count_Monthly')

    # Get the month from df
    month = df.month.iloc[0]
    '''
    # Store Airtable IDs of retrieved records
    y = []
    for z in x:
        y.append(z.get('id'))
        
    # Retrieve records that match given condition
    x = table.all(formula = fm.match({'MONTH': month}))
    '''

    # WORKS FINE
    # table.update(record_id = 'rec0cbgjBj8reeDhH', fields = {'MONTH': 'hoohah'})
    
    # Sample record for automating the click sequence automation
    # table.update(record_id = 'rec0cbgjBj8reeDhH', fields = {'chocolate': True})

    # table.batch_update(records = [{"id": y, "fields": {"Extra": 100}}])
    
    # table.all()
    for i, row in df.iterrows():
        table.create({ 'CLIENT NAME': row['name'], 'MONTH': row['month'], 'Delivery status': row['delivery_status'], 'Price scale': row['price_scale'],
                        'Number of orders': row['n_orders'], 'Meals reg': row['meals_reg'], 'Meals large': row['meals_large'], 
                        'Extra': row['meals_large'], 'Montant facture': row['total']
        })

        print(f"Wrote {i+1} out of {len(df)} records")