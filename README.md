![Logo](https://github.com/jonathanrjpereira/Volcanic-Alert-Level-Dashboard/blob/master/img/logo.jpg)

An Internet connected physical indicator that visualizes Volcanic Alert Levels. The data is obtained by using the [GeoNet API](https://api.geonet.org.nz/) and is visualized using a Raspberry Pi.

## What are Volcanic Levels & How are they Classified?
In New Zealand, we use a system of Volcanic Alert Levels is used to define the current status of each volcano. The alert levels range from 0 to 5. The alert levels are used to guide any appropriate response.

![Volcanic Alert Level](https://github.com/jonathanrjpereira/Volcanic-Alert-Level-Dashboard/blob/master/img/VAL.JPG)

You can find more information about Volcanic Alert Levels at [GeoNet](https://www.geonet.org.nz/about/volcano/val).

## Features

 - Acquires volcanic alert level data from the GeoNet API.
 - Hourly Updates.
 - Displays alert level of volcanoes indivually using LED Bar-Graphs.
 - Plots a digital graph of the alert levels using Matplotlib.

## Prerequisites
**Hardware:**
1. [Raspberry Pi Zero W](https://amzn.to/2JDBh15) or [Raspberry Pi 3 B](https://amzn.to/2DmM1k5).
2. [LED Bar Graph](https://amzn.to/2SHoe2x). 

**Software Dependencies:**
1. Requests is an elegant and simple HTTP library for Python.  [Requests Installation & Documentation](http://docs.python-requests.org/en/master/user/install/)
2. Graph Plotting Library. [Matplotlib 3.0](https://matplotlib.org/) 

## Working

**API:**

The GeoNet Volcano API provides us with a simple JSON feed which contains the following properties:

 - **volcanoID** - a unique identifier for the volcano.
 - **volcanoTitle** - the volcano title.
 - **level** - volcanic alert level.
 - **activity** - volcanic activity.
 - **hazards** - most likely hazards

For this project we are only interested in volcanoID, volcanoTitle & level. The remaining features are fetched but are not used within the project.  

**Fetching the Data:**

The raw data can be simply retrieved by reading the JSON object using the `requests` library & Python's built in `JSON` package. The raw data is updated on an hourly basis & can be found at: [https://api.geonet.org.nz/volcano/val](https://api.geonet.org.nz/volcano/val)
The following code is used to fetch the raw data from the API:

    r = requests.get('https://api.geonet.org.nz/volcano/val')
    data = r.json()
Below is an example of what the raw data looks like:

![Raw Data](https://github.com/jonathanrjpereira/Volcanic-Alert-Level-Dashboard/blob/master/img/rawdata.JPG)

**Extracting Useful Data:**

We need to extract useful data such as volcanoID, volcanoTitle & level from the raw data. This useful information is encompassed within a nested [dictionary](https://www.w3schools.com/python/python_dictionaries.asp). We need to figure out which nests contain the data we require. 
From the raw data we can see that the useful data is contained within the following nests: `features`& `properties`. 

![Nest](https://github.com/jonathanrjpereira/Volcanic-Alert-Level-Dashboard/blob/master/img/nest.JPG)

The `features`nest includes a `properties` nest for each volcano. The `properties` nest contains the `volcanoID`, `volcanoTitle`, `level` & other information about the volcano.
The following code snippet is used to extract the useful data & groups them into individual [lists](https://www.w3schools.com/python/python_lists.asp): 

    feature = data['features']
    
    volcanoID = []
    volcanoTitle = []
    level = []

    for result in feature:
        properties = result['properties']

        volcanoID.append(properties['volcanoID'])
        volcanoTitle.append(properties['volcanoTitle'])
        level.append(properties['level'])

## Contributing

Are you a programmer, engineer or hobbyist who has a great idea for a new feature in this project? Maybe you have a good idea for a bug fix? Feel free to grab our code & schematics from Github and tinker with it. Don't forget to smash those Star & Pull Request buttons. [Contributor List](https://github.com/jonathanrjpereira/Volcanic-Alert-Level-Dashboard/graphs/contributors)

## Note

We are not affiliated with GeoNet. Please be mindful & limit the number of requests made to the website so as to not overwhelm their servers. Don't forget to read their [API documentation](https://api.geonet.org.nz/) too.
