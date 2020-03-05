import xlrd
import pandas as pd

def excel(ea_file):
    """Loads the data from an excel spreadsheet that is exported from an Engineers Australia myCPD Record.
     
     Arguments:
        ea_file -- the path the to the myCPD Record xlsx file, including file extension
    """
    raw_data = pd.read_excel(ea_file, sheet_name=0, skiprows=[0])
    #print(raw_data.head(20))
    new_data = raw_data.iloc[::2, :]  #Each observation is split over two rows.  Get the odd rows
    #print(new_data.head(10))
    evenrows = raw_data.iloc[1::2, :]   #Get the even rows
    #print(evenrows['END DATE'].head(10))
    new_data['Learning outcome'] = evenrows['END DATE'].values
    new_data.drop(columns=['REF NO', 'Unnamed: 14'], inplace=True)
    new_data.columns = ['Type', 'Start date', 'End date', 'Activity', 'Topic','Provider', 'EA Division', 'Location', 'Hours: total', 'Hours: risk management', 'Hours: business and management', 'Hours: area of practice', 'Notes', 'Learning outcome']
    new_data['Start date'] = pd.to_datetime(new_data['Start date'])
    new_data['End date'] = pd.to_datetime(new_data['End date'])
    new_data['Type'] = new_data['Type'].map(lambda x: x.lstrip('Type '))
    new_data.reset_index(drop=True, inplace=True)
    return new_data 