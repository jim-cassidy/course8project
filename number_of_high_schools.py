


   


```python
import requests # library to handle requests
import pandas as pd # library for data analsysis
import numpy as np # library to handle data in a vectorized manner
import random # library for random number generation

!conda install -c conda-forge geopy --yes 
from geopy.geocoders import Nominatim # module to convert an address into latitude and longitude values

# libraries for displaying images
from IPython.display import Image 
from IPython.core.display import HTML 
    
# tranforming json file into a pandas dataframe library
from pandas.io.json import json_normalize

!conda install -c conda-forge folium=0.5.0 --yes
import folium # plotting library

print('Folium installed')
```

    Collecting package metadata: done
    Solving environment: done
    
    # All requested packages already installed.
    
    Collecting package metadata: done
    Solving environment: done
    
    # All requested packages already installed.
    
    Folium installed



```python

```

import requests # library to handle requests
import pandas as pd # library for data analsysis
import numpy as np # library to handle data in a vectorized manner
import random # library for random number generation

!conda install -c conda-forge geopy --yes 
from geopy.geocoders import Nominatim # module to convert an address into latitude and longitude values

# libraries for displaying images
from IPython.display import Image 
from IPython.core.display import HTML 
    
# tranforming json file into a pandas dataframe library
from pandas.io.json import json_normalize

!conda install -c conda-forge folium=0.5.0 --yes
import folium # plotting library

print('Folium installed')


```python
CLIENT_ID = 'JAH2Y0HES01BIMCMSRULSHTXIVUYLOQPGNJBIC0LWJ4KWMUL' # your Foursquare ID
CLIENT_SECRET = 'GEZ1UJJVLK5YIXKZPMG03UBNBYHMJPA52NAEDO1GSP5IL1PA' # your Foursquare Secret
VERSION = '20180604'
LIMIT = 1000
print('Your credentails:')
print('CLIENT_ID: ' + CLIENT_ID)
print('CLIENT_SECRET:' + CLIENT_SECRET)
```

    Your credentails:
    CLIENT_ID: JAH2Y0HES01BIMCMSRULSHTXIVUYLOQPGNJBIC0LWJ4KWMUL
    CLIENT_SECRET:GEZ1UJJVLK5YIXKZPMG03UBNBYHMJPA52NAEDO1GSP5IL1PA



```python

```

  


```python
city = input("Enter the name of the city : ")
state =  input("Enter the name of the state :")

address = city + ", " + state


print (address)


CID = '4bf58dd8d48988d13d941735'

geolocator = Nominatim(user_agent="foursquare_agent")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print(latitude, longitude)
```

<a id="item1"></a>


```python
search_query = 'High School'
radius = 2000
print(search_query + ' .... OK!')
```


```python
url = 'https://api.foursquare.com/v2/venues/search?client_id={}&client_secret={}&ll={},{}&v={}&query={}&radius={}&categoryId={}&limit={}'.format(CLIENT_ID, CLIENT_SECRET, latitude, longitude, VERSION, search_query, radius, CID, LIMIT)
url
```


```python
results = requests.get(url).json()
results
```

#### Get relevant part of JSON and transform it into a *pandas* dataframe


```python
# assign relevant part of JSON to venues
venues = results['response']['venues']

# tranform venues into a dataframe
dataframe = json_normalize(venues)
dataframe.head()
```


```python
dataframe
# keep only columns that include venue name, and anything that is associated with location
filtered_columns = ['name', 'categories'] + [col for col in dataframe.columns if col.startswith('location.')] + ['id']
dataframe_filtered = dataframe.loc[:, filtered_columns]

# function that extracts the category of the venue
def get_category_type(row):
    try:
        categories_list = row['categories']
    except:
        categories_list = row['venue.categories']
        
    if len(categories_list) == 0:
        return None
    else:
        return categories_list[0]['name']

# filter the category for each row
dataframe_filtered['categories'] = dataframe_filtered.apply(get_category_type, axis=1)

# clean column names by keeping only last term
dataframe_filtered.columns = [column.split('.')[-1] for column in dataframe_filtered.columns]

dataframe_filtered
```


```python
dataframe_filtered.shape[0]
```


```python
******** THIS IS THE NUMBER OF SCHOOLS **************
```


```python

```
