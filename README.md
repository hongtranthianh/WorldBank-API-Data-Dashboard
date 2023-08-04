# WorldBank-Data-Dashboard

### Table of Contents

1. [Installation](#installation)
2. [Project Description](#description)
3. [File Structure](#files)
4. [How to run web app](#instruction)
5. [Licensing, Authors, and Acknowledgements](#licensing)
6. [Learn more](#learnmore)

This is a flask app that visualizes data from the world bank API. Data is pulled directly from the API and then visualized using Plotly.

Develop and deploy a data dashboard as a web app using Bootstrap, Plotly, Flask and Heroku.

Pull data directly from the [World Bank API](https://documents.worldbank.org/en/publication/documents-reports/api), clean the data in the back-end using pandas, and then display the results on your front-end. This would be instead of using a csv file for your data.

## Installation <a name="installation"></a>


## Project Description<a name="description"></a>

The main focus of this project is to practice how to pull data from an API, design a web app and deploy it to Heroku

1. Pull data from [World Bank API](https://documents.worldbank.org/en/publication/documents-reports/api)
2. Requirements.txt file containing the bare minimum package list/lists all of the Python packages that your app depends on.

## File Structure <a name="files"></a>




## How to run web app  <a name="instruction"></a>
Pull this source code from github to your local machine and run the following commands in the project's root directory:

```
python myapp.py
```

To install the flask app, you need:

- python3
- python packages in the requirements.txt file

Install the packages with
```
pip install -r requirements.txt
```

## Learn more <a name="learnmore"></a>

### APIs Besides the World Bank
A few examples of public APIs include the [Twitter API](https://developer.twitter.com/en/docs), the [Google Maps API](https://mapsplatform.google.com/), and the [Facebook Graph API](https://developers.facebook.com/docs/graph-api).

You can pull data from these APIs to create your own application.

### Deploy the web app in the cloud

You can go beyond by deploying the worldbank dashboard app in [Heroku](https://dashboard.heroku.com/apps). This is going to be written in the [next post]()

The big internet companies offer similar services like [Amazon's Lightsail](https://aws.amazon.com/lightsail/), [Microsoft's Azure](https://learn.microsoft.com/en-us/samples/azure-samples/python-docs-hello-world/python-flask-sample-for-azure-app-service-linux/), and [Google Cloud](https://cloud.google.com/appengine/docs/legacy/standard/python/setting-up-environment). However, these services tend to require more configuration. Most of these also come with either a free tier or a limited free tier that expires after a certain amount of time.
