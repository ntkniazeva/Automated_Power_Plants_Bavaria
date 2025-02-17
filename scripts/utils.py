import pandas as pd

# The function takes a list of cities in Bavaria from Wikipedia and returns this list.
def get_bavaria_city_list():
    # Store link in a variable
    url = 'https://en.wikipedia.org/wiki/List_of_cities_in_Bavaria_by_population#'

    # Reads all HTML tables on this page. Returns a list of DataFrames,
    # where each DataFrame corresponds to a table found on the webpage
    tables = pd.read_html(url)
    # Selects the first table on the page
    city_table = tables[0]

    # Accesses the 'City' column converts it to a list using .tolist().
    # This list contains the names of the cities in Bavaria.
    city_list = city_table['City'].tolist()

    return city_list


# Cleans up the column names by replacing special German characters (such as umlauts)
# with their ASCII equivalents
# and removing unwanted characters like parentheses and colons.
# It also strips whitespace from the beginning and the end of the string.
# '\xad' is a soft hyphen, an invisible character,
# but becomes visible can cause problems when working with text data
# '⁰' is a superscript zero character,
# a numeric character, but it is not useful for typical string operations
def clear_column_names(table): # Takes a table,
    '''чистит имена столбцов в датафрейме'''
    columns_list = table.columns # retrieves the list of column names
    replacements = { # Creates a dictionary
                'ä': 'a', # replace German letters with ASCII equiavalent
                'ö': 'o',
                'ü': 'u',
                'Ä': 'A',
                'Ö': 'O',
                'Ü': 'U',
                'ß': 'ss',
                '(': '', # remove special characters (paranthesis and colons)
                ')': '',
                ':': '',
                '\xad': '', # a soft hyphen
                '⁰': '' # superscript zero character
            }
    for i in columns_list: # i is a column name. Iterates over each column name. Creates a copy called new_i
        new_i = i
        # For each column name new_i, it iterates through the replacements dictionary
        # It replaces each occurrence of the German character or unwanted character (umlaut)
        # in new_i with its corresponding replacement value (replacement).
        for umlaut, replacement in replacements.items():
            new_i = new_i.replace(umlaut, replacement)
        new_i = new_i.strip() # Removes any leading or trailing whitespace from new_i.
        # Renames the column i in the table DataFrame to new_i
        table.rename(columns={i:new_i}, inplace=True) # rename method of pandas.
        # The inplace=True parameter ensures that the DataFrame is modified directly
        # without the need to assign it back.


LIST_COLUMNS = [
    'name',
    'postcode',
    'status',
    'warm_output',
    'state',
    'city'
]