import xlrd
import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'

def readEAExcel(ea_file: str) -> pd.DataFrame:
    """Loads the data from an excel spreadsheet that is exported from an Engineers Australia myCPD Record.

    This imports cpd data from an excel spreadsheet that uses from the Engineers Australia myCPD format.  The data cleaned and put into a pandas.DataFrame which is returned.  The function insertDataframe() from this same module needs to be called to write the contents of the dataframe in to the current CPEngLog database. 
     
    Arguments:
        ea_file -- the path the to the myCPD Record xlsx file, including file extension.
    
    Returns:
        None if error,otherwise a pandas.DataFrame object containing the imported data.
    """
    raw_data = pd.read_excel(ea_file, sheet_name=0, nrows=1)
    headerText = raw_data.columns[0]
    if headerText.find('CPD ACTIVITY REPORT') >= 0:
        raw_data = pd.read_excel(ea_file, sheet_name=0, skiprows=[0])
        new_data = raw_data.iloc[::2, :]  #Each observation is split over two rows.  Get the odd rows
        evenrows = raw_data.iloc[1::2, :]   #Get the even rows
        new_data['Learning outcome'] = evenrows['END DATE'].values
        new_data.drop(columns=['REF NO', 'Unnamed: 14'], inplace=True)
        new_data.columns = ['Type', 'Start date', 'End date', 'Activity', 'Topic','Provider', 'EA Division', 'Location', 'Hours: total', 'Hours: risk management', 'Hours: business and management', 'Hours: area of practice', 'Notes', 'Learning outcome']
        new_data['Start date'] = pd.to_datetime(new_data['Start date'])
        new_data['End date'] = pd.to_datetime(new_data['End date'])
        new_data['Type'] = new_data['Type'].map(lambda x: x.lstrip('Type '))
        new_data.reset_index(drop=True, inplace=True)
        return new_data
    else:
        return None