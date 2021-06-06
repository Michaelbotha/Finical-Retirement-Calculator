#!/usr/bin/env python
# coding: utf-8

# In[25]:


#Single selections dropdown working with freq

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.express as px
import urllib.parse
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc



SATaxi_LOGO = "https://cdn0.iconfinder.com/data/icons/cars-and-delivery/512/minibus-512.png"

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]


app = dash.Dash(__name__,external_stylesheets=external_stylesheets)
app.title = "Finical advisory"

server = app.server

app.layout = html.Div(children=[
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


page_2_layout = html.Div([

dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Investment calculator", href="/Investment calculator")),
    ],
    brand="Finical advisory",
    brand_href="#",
    color="#3edbf0",
    dark=True,
),   
        html.P(
            children="Most South africans are unaware of how much they really need to save for retirement and for how long their retirement income will last. We aim to assist our subscribers and broader society in the financial planning process through our range of financial calculators.  ",className="header-description"),
    
  html.Div([
     
    html.P(children="Please select the inputs applicable to you below",className="Graph-header"),  
    dbc.Row([
        
        html.Div([html.P(children="Do you plan to save a lump-sum amount or save recurring monthly contributions:",className="InDivText")], className = 'InvestmentTypeDiv'),        
        html.Div([
            dcc.Dropdown(
                id='Investment-type-dropdown',
                options=[
                    {'label': 'Lump-sum', 'value': 'LumpSum'},
                    {'label': 'Recurring', 'value': 'Recurring'}
                ],
                value='LumpSum'
            ),
        
        ]
        #, style = {'margin-left': '20px ', 'padding':'0px 0px'}
        ),

    
    ],align="center" ,justify="center"),
  
  ]),
      
    html.P(children="Investment horison factors",className="Graph-header"),
    
    html.Div([
    
    dbc.Row([
    
        dbc.Col([
     
            html.Div(id='Age-output-container',className = 'MySlider'),
            dcc.Slider(
                id='Age-slider',
                min=25,
                max=64,
                step=1,
                value=25,
            ),    
         ]),  
    
        dbc.Col([
    
            html.Div(id='RetAge-output-container' ,className = 'MySlider'),
            dcc.Slider(
                    id='RetAge-slider',
                    min = 55,
                    max= 80,
                    step=1,
                    value=55,
                ),
        ]), 
        
                
        dbc.Col([
            html.Div(id='LifeExpectancy-output-container' ,className = 'MySlider'), 
            dcc.Slider(
                    id='LifeExpectancy-investment-slider',
                    min = 15,
                    max= 40,
                    step=1,
                    value=15,
                ),
            ]),
    
        ] , no_gutters = True ,style = {'padding':'30px'} ,align="center" ,justify="center"),
      
      ]),
    
    
    html.Div([
    
        html.P(children="Economic growth factors",className="Graph-header"),
    
    dbc.Row([
        
        dbc.Col([], id = 'AmountsliderType-output-container',className = 'MySlider'), 
        
        dbc.Col([
            html.Div(id='GrowthRate-output-container' ,className = 'MySlider'),
            dcc.Slider(
                    id='GrowthRate-slider',
                    min = 0,
                    max= 0.15,
                    step=0.005,
                    value= 0.07,
                ),
            ]),


        dbc.Col([    
            html.Div(id='Inflation-output-container' ,className = 'MySlider'),    
            dcc.Slider(
                    id='Inflation-slider',
                    min = 0,
                    max= 0.1,
                    step= 0.005,
                    value= 0.05,
                ),
            ]),

        dbc.Col([
            html.Div(id='TargetretirementIncome-output-container' ,className = 'MySlider'),         
            dcc.Slider(
                    id='TargetretirementIncome-slider',
                    min = 1000,
                    max= 50000,
                    step=500,
                    value=1000,
                ),
            ]),
        
            ], style = {'padding':'30px'} ,align="center" ,justify="center"),
        
        ]),
        
 
        dbc.Col([
            html.P(children="Projected retirement assets (in today's terms)",className="Graph-header"), 
            dcc.Graph( id='Projected-retirement-assets',config={"displayModeBar": False},),],style = {'margin': '0px', 'padding':'0px 0px'}
     ),
    
       dbc.Col([
        html.P(children="Monthly retirement income (in today's terms)",className="Graph-header"), 
        dcc.Graph( id='Retirement-Income-assets',config={"displayModeBar": False},) ],style = {'margin': '0px', 'padding':'0px 0px'})
    
]) 


@app.callback(Output('AmountsliderType-output-container', 'children')
              ,Input('Investment-type-dropdown', 'value'))

def InvestmentTypegetter(typeselected):
    
    if typeselected == 'LumpSum':
        
        slidervalues = dbc.Col([html.Div(id='Principal-output-container' ,className = 'MySlider'),    
                            dcc.Slider(
                                    id='Principal-investment-slider',
                                    min = 100000,
                                    max= 10000000,
                                    step=50000,
                                    value=100000,
                                )])

    else:
        
        slidervalues = dbc.Col([html.Div(id='Principal-output-container' ,className = 'MySlider'),    
                            dcc.Slider(
                                    id='Principal-investment-slider',
                                    min = 500,
                                    max= 30000,
                                    step= 100,
                                    value= 1000,
                                )])
        
    return slidervalues


@app.callback([Output('Age-output-container', 'children'),
               Output('RetAge-output-container', 'children'),
               Output('LifeExpectancy-output-container', 'children'),
               Output('Principal-output-container', 'children'),
               Output('GrowthRate-output-container', 'children'),
               Output('Inflation-output-container', 'children'),
               Output('TargetretirementIncome-output-container', 'children'),
               Output('Projected-retirement-assets', 'figure'),
               Output('Retirement-Income-assets', 'figure')],
              [Input('Age-slider', 'value'),
               Input('RetAge-slider', 'value'),
               Input('LifeExpectancy-investment-slider', 'value'),
               Input('Principal-investment-slider', 'value'),
               Input('GrowthRate-slider', 'value'),
               Input('Inflation-slider', 'value'),
               Input('TargetretirementIncome-slider', 'value')])


def CalculateRetirement(Client_age,Client_Retirement_Age,TermInRetirement,InvestmentAmount, Client_GrowthRate,Client_Inflation , Client_target_Income ):
    
    age = Client_age
    RetireMentAge = Client_Retirement_Age
    MaxDrawdown = 0.175
    MinDrawdown = 0.025
    Fundvalue = InvestmentAmount
    period = RetireMentAge - age + 1 + TermInRetirement
    GrowthRate = Client_GrowthRate
    Inflation = Client_Inflation
    RealReturn = ((1+ GrowthRate)/(1+Inflation ) -1)
    N_rows = period
    N_cols = 6
    ValuesMatrix = pd.DataFrame(np.zeros((N_rows, N_cols)))
    TargetIncome = Client_target_Income

    for x in range(period):
    
        if (x + age) <  RetireMentAge :
            ValuesMatrix.iloc[x][0] = age + x
    
            if x == 0 :
                ValuesMatrix.iloc[x][1] = Fundvalue
            else :
                ValuesMatrix.iloc[x][1] = ValuesMatrix.iloc[x-1][3]
    
            ValuesMatrix.iloc[x][2] = ValuesMatrix.iloc[x][1]*RealReturn
            ValuesMatrix.iloc[x][3] = ValuesMatrix.iloc[x][2] + ValuesMatrix.iloc[x][1] 
            ValuesMatrix.iloc[x][5] = ValuesMatrix.iloc[x][3]
    
        elif ((x + age) >=  RetireMentAge) :
        
            ValuesMatrix.iloc[x][0] = age + x
            
        
            if (((12*TargetIncome/ValuesMatrix.iloc[x-1][3]) <= MaxDrawdown) & ((12*TargetIncome/ValuesMatrix.iloc[x-1][3]) >= MinDrawdown)) :
                ValuesMatrix.iloc[x][1] = ValuesMatrix.iloc[x-1][3] - 12*TargetIncome
                ValuesMatrix.iloc[x][2] = ValuesMatrix.iloc[x][1]*RealReturn
                ValuesMatrix.iloc[x][3] = ValuesMatrix.iloc[x][2] + ValuesMatrix.iloc[x][1]
                ValuesMatrix.iloc[x][4] = TargetIncome
        
            elif ((12*TargetIncome/ValuesMatrix.iloc[x-1][3]) > MaxDrawdown):
                ValuesMatrix.iloc[x][1] = ValuesMatrix.iloc[x-1][3]*(1-MaxDrawdown)
                ValuesMatrix.iloc[x][2] = ValuesMatrix.iloc[x][1]*RealReturn
                ValuesMatrix.iloc[x][3] = ValuesMatrix.iloc[x][2] + ValuesMatrix.iloc[x][1]
                ValuesMatrix.iloc[x][4] = ValuesMatrix.iloc[x-1][3]*MaxDrawdown/12
        
            elif ((12*TargetIncome/ValuesMatrix.iloc[x-1][3]) < MinDrawdown):
                ValuesMatrix.iloc[x][1] = ValuesMatrix.iloc[x-1][3]*(1-MinDrawdown)
                ValuesMatrix.iloc[x][2] = ValuesMatrix.iloc[x][1]*RealReturn
                ValuesMatrix.iloc[x][3] = ValuesMatrix.iloc[x][2] + ValuesMatrix.iloc[x][1]
                ValuesMatrix.iloc[x][4] = ValuesMatrix.iloc[x-1][3]*MinDrawdown/12
            
            ValuesMatrix.iloc[x][5] = ValuesMatrix.iloc[x][3]
            
    ValuesMatrix = ValuesMatrix.rename(columns = {0: 'Age', 1: 'Start fund value' , 2: 'Growth', 3: 'Retirement fund value', 4: 'Retirement income', 5: 'Real retirement fund value'}, inplace = False)
    
    RetirementGraph = px.bar(ValuesMatrix, x= 'Age', y='Real retirement fund value')

    
    RetirementIncome = px.bar(ValuesMatrix[ValuesMatrix['Age'] >= Client_Retirement_Age], x= 'Age', y= 'Retirement income')

    
    #Formatting outputs
    Client_GrowthRate = round(Client_GrowthRate*100,1)
    Client_Inflation = round(Client_Inflation*100,1)
    
    
    return 'You are {} years of age'.format(Client_age), 'You want to retire at {} years of age'.format(Client_Retirement_Age), 'You will live {} years in retirement'.format(TermInRetirement),'You want to invest R{}'.format(InvestmentAmount) , '{}% nominal growth per year'.format(Client_GrowthRate),  '{}% inflation per year'.format(Client_Inflation) , 'You require monthly income of R{} in retirement'.format(Client_target_Income), RetirementGraph, RetirementIncome


@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/ActuarialDashboard':
        return page_2_layout
    elif pathname == '/TimeSeriesAnalysis':
        return page_1_layout
    else:
        return page_2_layout


if __name__ == "__main__":
    app.run_server(debug=False)


# In[ ]:




@app.callback([Output('Age-output-container', 'children'),
               Output('RetAge-output-container', 'children'),
               Output('LifeExpectancy-output-container', 'children'),
               Output('AmountsliderType-output-container', 'children'),
               Output('GrowthRate-output-container', 'children'),
               Output('Inflation-output-container', 'children'),
               Output('Projected-retirement-assets', 'figure'),
               Output('Retirement-Income-assets', 'figure')],
              [Input('Age-slider', 'value'),
               Input('RetAge-slider', 'value'),
               Input('LifeExpectancy-investment-slider', 'value'),
               Input('Investment-type-dropdown', 'value'),
               Input('Principal-investment-slider', 'value'),
               Input('GrowthRate-slider', 'value'),
               Input('Inflation-slider', 'value'),
               Input('TargetretirementIncome-slider', 'value')])

def CalculateRetirement(Client_age,Client_Retirement_Age, InvestmentType ,InvestmentAmount,TermInRetirement, Client_GrowthRate,Client_Inflation , Client_target_Income ):
    
    age = Client_age
    RetireMentAge = Client_Retirement_Age
    MaxDrawdown = 0.175
    MinDrawdown = 0.025
    Fundvalue = InvestmentAmount
    period = RetireMentAge - age + 1 + TermInRetirement
    GrowthRate = Client_GrowthRate
    Inflation = Client_Inflation
    RealReturn = ((1+ GrowthRate)/(1+Inflation ) -1)
    N_rows = period
    N_cols = 6
    ValuesMatrix = pd.DataFrame(np.zeros((N_rows, N_cols)))
    TargetIncome = Client_target_Income

    for x in range(period):
    
        if (x + age) <  RetireMentAge :
            ValuesMatrix.iloc[x][0] = age + x
    
            if x == 0 :
                ValuesMatrix.iloc[x][1] = Fundvalue
            else :
                ValuesMatrix.iloc[x][1] = ValuesMatrix.iloc[x-1][3]
    
            ValuesMatrix.iloc[x][2] = ValuesMatrix.iloc[x][1]*RealReturn
            ValuesMatrix.iloc[x][3] = ValuesMatrix.iloc[x][2] + ValuesMatrix.iloc[x][1] 
            ValuesMatrix.iloc[x][5] = ValuesMatrix.iloc[x][3]
    
        elif ((x + age) >=  RetireMentAge) :
        
            ValuesMatrix.iloc[x][0] = age + x
            
        
            if (((12*TargetIncome/ValuesMatrix.iloc[x-1][3]) <= MaxDrawdown) & ((12*TargetIncome/ValuesMatrix.iloc[x-1][3]) >= MinDrawdown)) :
                ValuesMatrix.iloc[x][1] = ValuesMatrix.iloc[x-1][3] - 12*TargetIncome
                ValuesMatrix.iloc[x][2] = ValuesMatrix.iloc[x][1]*RealReturn
                ValuesMatrix.iloc[x][3] = ValuesMatrix.iloc[x][2] + ValuesMatrix.iloc[x][1]
                ValuesMatrix.iloc[x][4] = TargetIncome
        
            elif ((12*TargetIncome/ValuesMatrix.iloc[x-1][3]) > MaxDrawdown):
                ValuesMatrix.iloc[x][1] = ValuesMatrix.iloc[x-1][3]*(1-MaxDrawdown)
                ValuesMatrix.iloc[x][2] = ValuesMatrix.iloc[x][1]*RealReturn
                ValuesMatrix.iloc[x][3] = ValuesMatrix.iloc[x][2] + ValuesMatrix.iloc[x][1]
                ValuesMatrix.iloc[x][4] = ValuesMatrix.iloc[x-1][3]*MaxDrawdown/12
        
            elif ((12*TargetIncome/ValuesMatrix.iloc[x-1][3]) < MinDrawdown):
                ValuesMatrix.iloc[x][1] = ValuesMatrix.iloc[x-1][3]*(1-MinDrawdown)
                ValuesMatrix.iloc[x][2] = ValuesMatrix.iloc[x][1]*RealReturn
                ValuesMatrix.iloc[x][3] = ValuesMatrix.iloc[x][2] + ValuesMatrix.iloc[x][1]
                ValuesMatrix.iloc[x][4] = ValuesMatrix.iloc[x-1][3]*MinDrawdown/12
            
            ValuesMatrix.iloc[x][5] = ValuesMatrix.iloc[x][3]
            
    ValuesMatrix = ValuesMatrix.rename(columns = {0: 'Age', 1: 'Start fund value' , 2: 'Growth', 3: 'Retirement fund value', 4: 'Retirement income', 5: 'Real retirement fund value'}, inplace = False)
    
    RetirementGraph = px.bar(ValuesMatrix, x= 'Age', y='Real retirement fund value')

    
    RetirementIncome = px.bar(ValuesMatrix[ValuesMatrix['Age'] >= Client_Retirement_Age], x= 'Age', y= 'Retirement income')

    
    #Formatting outputs
    Client_GrowthRate = round(Client_GrowthRate*100,1)
    Client_Inflation = round(Client_Inflation*100,1)
    
    
    return 'You are {} years of age'.format(Client_age), 'You want to retire at {} years of age'.format(Client_Retirement_Age), 'You will live {} years in retirement'.format(TermInRetirement) , slidervalues,'You want to invest R{}'.format(InvestmentAmount) , '{}% nominal growth per year'.format(Client_GrowthRate),  '{}% inflation per year'.format(Client_Inflation) , 'You require monthly income of R{} in retirement'.format(Client_target_Income), RetirementGraph, RetirementIncome

