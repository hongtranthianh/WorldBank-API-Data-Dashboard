# WorldBank-Data-Dashboard

### Table of Contents

1. [Installation](#installation)
2. [Project Description](#description)
3. [File Structure](#files)
4. [How to run web app](#instruction)
5. [Licensing, Authors, and Acknowledgements](#licensing)
6. [Learn more](#learnmore)

## Installation <a name="installation"></a>

- The virtual environment [worldbankenv](https://github.com/hongtranthianh/WorldBank-Data-Dashboard/tree/main/worldbankenv) contains all Python packages that the app depends on.
- The code should run with no issues using Python versions 3.*. Currently using `Python 3.11.3` on `Windowns 10`.

## Project Description<a name="description"></a>

Develop and deploy a data dashboard as a web app using Bootstrap, Plotly, and Flask.

Data was pulled directly from the [World Bank API](https://documents.worldbank.org/en/publication/documents-reports/api), clean the data in the back-end using pandas ([wrangle_data.py](https://github.com/hongtranthianh/WorldBank-Data-Dashboard/blob/main/wrangling_scripts/wrangle_data.py)) and then display the results on the front-end ([index.html](https://github.com/hongtranthianh/WorldBank-Data-Dashboard/blob/main/myapp/templates/index.html)).

The output is a functioning flask app that was deployed in local host successfully
<p ><img src="Images/main-page.png" alt="image" ></p>

## File Structure <a name="files"></a>

```
- Images # containing images used in README.md

- myapp
|- static  # containing images for front end
|- template
| |- index.html  # main page of web app
|- __init__.py  # entry point for the app
|- routes.py  # make sure correct web address associated with correct html template

- worldbankenv # virtual environment for this project

- wrangling_scripts
|- wrangle_data.py  # Read in data API and set up Plotly plots

- myapp.py # Flask file running the app in local host

- requirements.txt # list all of the Python packages that the app depends on

- README.md
```


## How to run web app  <a name="instruction"></a>
1. Pull this repository to your local machine

```
git clone https://github.com/hongtranthianh/WorldBank-Data-Dashboard.git
```

2. Run this app locally in the project's root directory

```
python myapp.py
```
or
```
py myapp.py
```

## Learn more <a name="learnmore"></a>

### APIs Besides the World Bank
A few examples of public APIs include the [Twitter API](https://developer.twitter.com/en/docs), the [Google Maps API](https://mapsplatform.google.com/), and the [Facebook Graph API](https://developers.facebook.com/docs/graph-api).

You can pull data from these APIs to create your own application.

### Deploy the web app in the cloud

You can go beyond local host by deploying the worldbank dashboard app in [Heroku](https://dashboard.heroku.com/apps). This is going to be written in [next post]()

The big internet companies offer similar services like [Amazon's Lightsail](https://aws.amazon.com/lightsail/), [Microsoft's Azure](https://learn.microsoft.com/en-us/samples/azure-samples/python-docs-hello-world/python-flask-sample-for-azure-app-service-linux/), and [Google Cloud](https://cloud.google.com/appengine/docs/legacy/standard/python/setting-up-environment). However, these services tend to require more configuration. Most of these also come with either a free tier or a limited free tier that expires after a certain amount of time.
