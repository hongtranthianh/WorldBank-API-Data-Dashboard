import pandas as pd
import plotly.graph_objs as go
import plotly.colors
from collections import OrderedDict
import requests
import datetime

def clean_data(current_year = datetime.date.today().year, last_n_year = 10):
    '''
    Pull data from World Bank Data API, clean and transform the data into desirable dataframe format 
    to be ready for visualization with Plotly
    '''

    # Countries in SEA region
    SEA_countries = OrderedDict([('Myanmar','MM'),('Singapore','SG'),('Laos','LA'),('Brunei','BN'),
                                 ('Philippines','PH'),('Malaysia','MY'),('Cambodia','KH'),
                                 ('Timor-Leste','TL'),('Thailand','TH'),('Indonesia','ID'),('Vietnam','VN')])
    # Get all SEA countries and store as a string, separated by ;
      ## Result: 'mm;sg;la;bn;ph;my;kh;tl;th;id;vn'
    SEA_countries_str = list(SEA_countries.values())
    SEA_countries_str = [x.lower() for x in SEA_countries_str]
    SEA_countries_str = ';'.join(SEA_countries_str)

    # World Bank indicators of interest
    indicators = {'Population, total':'SP.POP.TOTL',
                  'GDP per capita (current US$)':'NY.GDP.PCAP.CD',
                  'Unemployment, total (% of total labor force) (national estimate)':'SL.UEM.TOTL.NE.ZS',
                  'Foreign direct investment, net inflows (BoP, current US$)':'BX.KLT.DINV.CD.WD'}
    
    # URL endpoints for the World Bank API
    urls = []
    # Pass a dict of value as parameters to the url instead of specifying the entire URL in a single string
    payload = {'format': 'json', 'per_page': '1000', 'date':'{}:{}'.format(current_year-last_n_year, current_year)}
    # Store the data frames with the indicator data of interest
    data_frames = []
    
    # Pull data from World Bank API in json format and store in a dataframe
    for ind in indicators.values():
        url = 'http://api.worldbank.org/v2/countries/' + SEA_countries_str +'/indicators/' + ind
        urls.append(url)
        try:
            r = requests.get(url, params=payload)
            data = r.json()[1]
        except:
            print('Data not found for indicator: ', ind)
 
        for i, val in enumerate(data):
            val['indicator'] = val['indicator']['value']
            val['country'] = val['country']['value']

        data_frames.append(data)

    # create an Empty DataFrame object
    df = pd.DataFrame()
    # Append data to final dataframe
    for i in range(len(data_frames)):
        df_new = pd.DataFrame(data_frames[i])
        df = pd.concat([df,df_new])

    # Select columns of interest
    df = df[['indicator','country','date','value']]

    # Rename value
    df['indicator'] = df['indicator'].replace('Population, total','Total population')
    df['indicator'] = df['indicator'].replace('Unemployment, total (% of total labor force) (national estimate)','Total unemployment (%)')
    df['indicator'] = df['indicator'].replace('Foreign direct investment, net inflows (BoP, current US$)','FDI')
    df['indicator'] = df['indicator'].replace('GDP per capita (current US$)','GDP per capita')


    # Data type
    df['date'] = df['date'].astype('str')
    df['value'] = df['value'].astype('float64')
    
    return df


def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """
    df = clean_data()
    list_countries = df['country'].unique().tolist()
    last_n_year = len(df['date'].unique())

    # graph one
    graph_one = []
    for country in list_countries:
        df_graph_1 = df.loc[(df['country']==country)&(df['indicator']=='Total population')]
        x_val = df_graph_1['date'].tolist()
        y_val = df_graph_1['value'].tolist()
        graph_one.append(go.Scatter(x = x_val,
                                    y = y_val,
                                    mode = 'lines',
                                    name = country))
    layout_one = dict(title = 'Total population',
                      xaxis = dict(title = 'Year'),
                      yaxis = dict(title = 'Population'))

    # graph two
    graph_two = []
    for country in list_countries:
        df_graph_2 = df.loc[(df['country']==country)&(df['indicator']=='GDP per capita')]
        x_val = df_graph_2['date'].tolist()
        y_val = df_graph_2['value'].tolist()
        graph_two.append(go.Scatter(x = x_val,
                                    y = y_val,
                                    mode = 'lines',
                                    name = country))
    layout_two = dict(title = 'GDP per capita (current US$)',
                      xaxis = dict(title = 'Year'),
                      yaxis = dict(title = 'USD'))

# third chart plots percent of population that is rural from 1990 to 2015
    graph_three = []
    for country in list_countries:
        df_graph_3 = df.loc[(df['country']==country)&(df['indicator']=='Total unemployment (%)')]
        x_val = df_graph_3['date'].tolist()
        y_val = df_graph_3['value'].tolist()
        graph_three.append(go.Scatter(x = x_val,
                                      y = y_val,
                                      mode = 'lines',
                                      name = country))
    layout_three = dict(title = 'Total unemployment (%)',
                        xaxis = dict(title = 'Year'),
                        yaxis = dict(title = '% of Total labor force'))
    
# fourth chart shows rural population vs arable land
    graph_four = []
    for country in list_countries:
        df_graph_4 = df.loc[(df['country']==country)&(df['indicator']=='FDI')]
        x_val = df_graph_4['date'].tolist()
        y_val = df_graph_4['value'].tolist()
        graph_four.append(go.Scatter(x = x_val,
                                     y = y_val,
                                     mode = 'lines',
                                     name = country))
    layout_four = dict(title = 'Foreign direct investment (FDI), net inflows',
                       xaxis = dict(title = 'Year'),
                       yaxis = dict(title = 'USD'))
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures