#!/usr/bin/env python
# coding: utf-8

# In[51]:


import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.express as px
import urllib.parse
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import base64
import MyWebsiteFunctions50 as mf

            
table_header = [html.Thead(html.Tr([html.Th("Description"), html.Th("Value")]))]    
row1 = html.Tr([html.Td("Minimum monthly installment"), html.Td(id="MonthlyInstallment")])
row2 = html.Tr([html.Td("Total monthly installment"), html.Td(id="TotalMonthlyInstallMent")])
row3 = html.Tr([html.Td("Total payments made"), html.Td(id="TotalPaymentsMade")])
row4 = html.Tr([html.Td("Total interest paid"), html.Td(id="TotalInterestPaid")])              
row5 = html.Tr([html.Td("Total interest saved"), html.Td(id="TotalInterestSaved")])                
row6 = html.Tr([html.Td("Reduction in loan term"), html.Td(id="ReductionInLoanTerm")])
table_body = [html.Tbody([row1, row2, row3, row4,row5,row6])]                
table = dbc.Table(table_header + table_body, bordered=True, style = {'color':'#FFFFFF'})
 
            
image_filename = 'FinicalLogoWithoutWording.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())


SATaxi_LOGO = "https://cdn0.iconfinder.com/data/icons/cars-and-delivery/512/minibus-512.png"

external_stylesheets = [
    {
    'href': 'https://use.fontawesome.com/releases/v5.8.1/css/all.css',
    'rel': 'stylesheet',
    'integrity': 'sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf',
    'crossorigin': 'anonymous',
    },
]


app = dash.Dash(__name__,external_stylesheets=external_stylesheets)
app.title = "Finical advisory"

server = app.server

app.layout = html.Div(children=[
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content',style = {'margin':'0px','padding':'0px' })
])


page_1_layout = html.Div([

    mf.GenerateNavBar(),
    
    html.P(
                children="The impact of compound interest could either set you on the road to riches or spiraling into debt you may never recover from. One such example is your mortgage. Most people spend their whole lifes paying off their mortgage and end up paying more than twice the value of the their home. By paying an extra amount each month, you could save hundreds of thousands of rands over your life time.",className="header-description"),
  #html.Div([
                    
    

    #html.Div([
        html.Div([
            mf.GenerateSectionHeading("Please input your mortgage details below"), 
        
        html.Div([

            
            mf.GenerateInputCardObject(html.Div(id='LoanAmount-output-container',className = 'MySlider'
                                         ,style = {'width':'60%','margin':'auto'})
                                    ,mf.GenerateInput("Amountinput",0,10000000,"Number",1000000,'R1000 000')
                                    ,"col-xl-6 col-lg-6"  ),
            
                        
            mf.GenerateInputCardObject( html.Div(id='InterestRate-output-container',className = 'MySlider'
                                         ,style = {'width':'60%','margin':'auto'}),
                                       mf.GenerateInput("InterestRateinput",0,20,"Number",5,'5%')
                                      ,"col-xl-6 col-lg-6"),
            
            mf.GenerateInputCardObject( html.Div(id='LoanTerm-output-container',className = 'MySlider'
                                         ,style = {'width':'60%','margin':'auto'}),
                                       mf.GenerateInput("RemainingLoanTerm",0,40,"Number",20,'20 years')
                                      ,"col-xl-6 col-lg-6"),
            
            mf.GenerateInputCardObject( html.Div(id='AdditionalContribution-output-container',className = 'MySlider'
                                         ,style = {'width':'60%','margin':'auto'}),
            mf.GenerateInput("AdditionalContribution",0,20000,"Number",0,'R 1000')
                                      ,"col-xl-6 col-lg-6")
            
            
    
        ],className = 'card-body text-center row', style = {'margin': '0px', 'padding':'0px 0px'}),
            
            mf.GenerateSectionHeading("Your loan payment details"),
        
            html.Div([
                
                        
            mf.GenerateGraphBackGround("Payment details"
                                       ,table
                                       ,"col-xl-6 col-lg-6 "
                                      ),
            
            mf.GenerateGraphBackGround("Outstanding loan amount"
                                       ,dcc.Graph( id='Graph-Loan-Amount',config={"displayModeBar": False,'autosizable':True},)
                                       ,"col-xl-6 col-lg-6 "
                                      ),
                
            #mf.GenerateGraphBackGround("Payment details"
            #                           ,dcc.Graph( id='PaymentDetails-Amount',config={"displayModeBar": False,'autosizable':True})
           #                            ,"col-xl-4 col-lg-4 "
            #                          )

            ],style = {'display': 'flex',  'display': '-ms-flexbox' , 'display': 'flex', '-ms-flex-wrap': 'wrap', 'flex-wrap': 'wrap'})
    
        ]
            , className="card shadow mb-2 lg-4" ), 
   
    
    html.Div(
        dbc.NavLink(children = [
            html.I(className="fab fa-linkedin fa-3x"
                  ),
            html.Div(html.Span('Copyright © 2021'),className = "copyright text-center my-auto")
        ]          
                    ,style = {'color':'White','padding':"5% 0%"}
                    ,href="https://www.linkedin.com/in/michael-botha-tassa-a891ab9b/"
                   
        ) 
        ,className = "copyright text-center my-auto"
    ),
    

]) 
                

@app.callback([Output('LoanAmount-output-container', 'children'),
               Output('InterestRate-output-container', 'children'),
               Output('LoanTerm-output-container', 'children'),
               Output('AdditionalContribution-output-container', 'children'),
               Output('Graph-Loan-Amount', 'figure'),
               #Output('PaymentDetails-Amount', 'figure'),
               Output('MonthlyInstallment', 'children'),
               Output('TotalInterestPaid', 'children'),
               Output('TotalInterestSaved', 'children'),
               Output('ReductionInLoanTerm', 'children'),
               Output('TotalMonthlyInstallMent', 'children'),
               Output('TotalPaymentsMade','children')]
              ,[Input('Amountinput', 'value')
               ,Input('InterestRateinput', 'value')
               ,Input('RemainingLoanTerm', 'value')
               ,Input('AdditionalContribution', 'value')])

def LoanData(OutstandingLoanAmount, InterestRate, LoanTerm, ExtraAmountPaidOff):
    
    OutstandingLoanTerm = int(LoanTerm)
    ExtraPaymentMade = int(ExtraAmountPaidOff)
    N_rows = 12*OutstandingLoanTerm
    N_cols = 6
    LoanValue = int(OutstandingLoanAmount)
    MortgageInterest = int(InterestRate)
    LoanDataValues = pd.DataFrame(np.zeros((N_rows, N_cols)))
    Bar1Data = pd.DataFrame(np.zeros((1, 3)))
    MonthlyInterestRate = (1+int(MortgageInterest)/100)**(1/12) - 1
    AnnuityFactor = ((1-(1+MonthlyInterestRate)**(-N_rows))/MonthlyInterestRate)
    MonthlyInstallment = LoanValue/AnnuityFactor
    NewLoanTerm = 0 
    
    for x in range(N_rows):
        
        LoanDataValues.iloc[x][1] = x+1
        
        if x == 0 :
            LoanDataValues.iloc[x][2] = LoanValue
            LoanDataValues.iloc[x][3] = LoanValue*MonthlyInterestRate
            LoanDataValues.iloc[x][4] = LoanDataValues.iloc[x][2] + LoanDataValues.iloc[x][3] - MonthlyInstallment
            LoanDataValues.iloc[x][5] = MonthlyInstallment
            NewLoanTerm = x + 1
        
        elif (LoanDataValues.iloc[x-1][4] < (MonthlyInstallment + ExtraPaymentMade) ):
            LoanDataValues.iloc[x][2] = LoanDataValues.iloc[x-1][4]
            LoanDataValues.iloc[x][3] = LoanDataValues.iloc[x][2]*MonthlyInterestRate
            LoanDataValues.iloc[x][4] = 0
            LoanDataValues.iloc[x][5] = LoanDataValues.iloc[x-1][4]
            
            if (LoanDataValues.iloc[x-1][4] > 0):
                NewLoanTerm = x + 1
                
            
        
        elif (LoanDataValues.iloc[x-1][4] == 0 ):
            LoanDataValues.iloc[x][2] = LoanDataValues.iloc[x-1][4]
            LoanDataValues.iloc[x][3] = LoanDataValues.iloc[x][2]*MonthlyInterestRate
            LoanDataValues.iloc[x][4] = 0
            LoanDataValues.iloc[x][5] = 0
        
        else:
            LoanDataValues.iloc[x][2] = LoanDataValues.iloc[x-1][4]
            LoanDataValues.iloc[x][3] = LoanDataValues.iloc[x][2]*MonthlyInterestRate
            LoanDataValues.iloc[x][4] = LoanDataValues.iloc[x][2] + LoanDataValues.iloc[x][3] - MonthlyInstallment - ExtraPaymentMade
            LoanDataValues.iloc[x][5] = MonthlyInstallment + ExtraPaymentMade

    
    LoanDataValues = LoanDataValues.rename(columns = {1: 'Months into loan' , 2: 'Start Loan outstanding', 3: 'Interest paid', 4: 'Outstanding loan amount', 5:'Installments Made'}, inplace = False)
    OriginalLoanTermsGraph = px.line(LoanDataValues, x= 'Months into loan', y='Outstanding loan amount')
    
    Installment = ['Annual installment', (MonthlyInstallment + ExtraPaymentMade)*12]
    InterestPaid = ['Interest paid', LoanDataValues['Interest paid'].sum()]
    InterestPaidValue = LoanDataValues['Interest paid'].sum()
    Totalpaymentsmade = ['Total payments made', LoanDataValues['Interest paid'].sum() + LoanValue]
    Bar1Data = pd.DataFrame([Installment,InterestPaid,Totalpaymentsmade])
    InterestAmountSaved = (MonthlyInstallment*OutstandingLoanTerm*12 - LoanValue) - InterestPaidValue 
    LoanTermReduction = OutstandingLoanTerm*12-NewLoanTerm
                
    Bar1Data = Bar1Data.rename(columns = {0: 'Payment description', 1: 'Amount'})
    
    LoaninfoGraph = px.bar(Bar1Data, x= 'Payment description' ,y='Amount')
    
    LoanAmountInfo = html.H5('You have R{:,.0f} outstanding on your mortgage'.format(OutstandingLoanAmount),className="m-0 text-secondary text-center",style = {'justify-content':'center'})
    InterestRateInfo = html.H5('You pay a rate of interest rate of {}% '.format(InterestRate),className="m-0 text-secondary text-center",style = {'justify-content':'center'})
    LoanTermInfo = html.H5('Your outstanding loan term is {} years '.format(LoanTerm),className="m-0 text-secondary text-center",style = {'justify-content':'center'})
    AdditionalcontributionINfo = html.H5('You are paying R{} extra per month'.format(ExtraAmountPaidOff),className="m-0 text-secondary text-center",style = {'justify-content':'center'})
    MonthlyInstallmentInfo = "R{:,.1f}".format(round(MonthlyInstallment,2))
    InterestPaidValueInfo = "R{:,.1f}".format(round(InterestPaidValue,2)) 
    InterestAmountSavedInfo = "R{:,.1f}".format(round(InterestAmountSaved,2))
    LoanTermReductionInfo = "{} months reduction".format(round(LoanTermReduction,2))
    TotalMonthlyInstallmentInfo = "R{:,.1f}".format(round(MonthlyInstallment+ExtraPaymentMade,2))
    TotalPaymentsMadeInfo = "R{:,.1f}".format(round(LoanDataValues['Interest paid'].sum() + LoanValue,2))
    
    #html.I(className = "fas fa-home fa-2x",style = {'color':'#3C415C','margin':'margin-right:3px'})
    return LoanAmountInfo,            InterestRateInfo,            LoanTermInfo,            AdditionalcontributionINfo,            OriginalLoanTermsGraph,            MonthlyInstallmentInfo,            InterestPaidValueInfo,            InterestAmountSavedInfo,            LoanTermReductionInfo,            TotalMonthlyInstallmentInfo,            TotalPaymentsMadeInfo

               
            #LoaninfoGraph, \              
               
page_2_layout = html.Div([
    
mf.GenerateNavBar(),

        html.P(
            children="Most South africans are unaware of how much they really need to save for retirement and for how long their retirement income will last in retirement. The below investment calculator allows you to guage the amount of retirement assets you may accumulate under different scenarios and assumes that you will purchase a retirement income anuity ,from which you will draw a monthly income, from a trusted financial services provider.",className="header-description"),

    
    mf.GenerateSectionHeading("Please select the inputs applicable to you below"),

                             
    html.Div(children = [
        
            mf.GenerateInputCardObject(                 
                html.H6('Do you plan to save a lump-sum amount or save recurring monthly contributions?'
                         ,className="m-0 text-secondary text-center"
                        )  
                ,                                 
                mf.generateRadioInputs('Investment-type-dropdown','Lump-sum','Recurring')
                ,"col-xl-4 col-lg-4"
            ),
    
        html.Div(id = 'AmountsliderType-output-container',className = "col-xl-4 col-lg-4"),
        
    mf.GenerateInputCardObject( html.Div(id='TargetretirementIncome-output-container' 
                                         ,className = 'MySlider'
                                         ,style = {'width':'60%','margin':'auto'})
                               ,                       
                               
                               dcc.Slider(
                                            id='TargetretirementIncome-slider',
                                            min = 10000,
                                            max= 100000,
                                            step=1000,
                                            value=10000,
                                            marks={
                                                10000: {'label':'R10 000' , 'style': {'color': '#F9F9F9','width':'100%'}},
                                                25000: {'label':'R25 000' , 'style': {'color': '#F9F9F9'}},
                                                50000: {'label':'R50 000' , 'style': {'color': '#F9F9F9'}},
                                                75000: {'label':'R75 000' , 'style': {'color': '#F9F9F9'}},
                                                100000: {'label':'R100 000' , 'style': {'color': '#F9F9F9','width':'100%'}},
                                            }
                                            
                                        )
                              ,"col-xl-4 col-lg-4")

        
    ],className = 'row'
     ,style = {'padding':'0px','margin':'0px'}       ),

    mf.GenerateSectionHeading("Investment horizon factors"), 

    html.Div([

    dbc.Row([

        dbc.Col([
            html.I(className="fas fa-child fa-3x"),
            html.Div(id='Age-output-container',className = 'MySlider'),
            dcc.Slider(
                id='Age-slider',
                min=25,
                max=65,
                step=1,
                value=25,    
                marks={
                    25: {'label':'25' , 'style': {'color': '#F9F9F9'}},
                    40: {'label':'40' , 'style': {'color': '#F9F9F9'}},
                    55: {'label':'55' , 'style': {'color': '#F9F9F9'}},
                    65: {'label':'65' , 'style': {'color': '#F9F9F9'}}
                }
            ),
         ],className = 'MySlider'),

        dbc.Col([
            html.I(className="fas fa-hands-helping fa-3x", style = {'display': 'inline-block', 'width': '100%'}),
            html.Div(id='RetAge-output-container' ,className = 'MySlider'),
            dcc.Slider(
                    id='RetAge-slider',
                    min = 35,
                    max= 80,
                    step=1,
                    value=55,                
                    marks={
                        35: {'label':'35' , 'style': {'color': '#F9F9F9'}},
                        65: {'label':'65' , 'style': {'color': '#F9F9F9'}},
                        70: {'label':'70' , 'style': {'color': '#F9F9F9'}},
                        80: {'label':'80' , 'style': {'color': '#F9F9F9'}}
                
                    }
                ),
        ],className = 'MySlider'),


        dbc.Col([
            html.I(className="fas fa-umbrella fa-3x", style = {'display': 'inline-block', 'width': '100%'}),
            html.Div(id='LifeExpectancy-output-container' ,className = 'MySlider'),
            dcc.Slider(
                    id='LifeExpectancy-investment-slider',
                    min = 15,
                    max= 40,
                    step=1,
                    value=15,
                    marks={
                        15: {'label':'15' , 'style': {'color': '#F9F9F9'}},
                        20: {'label':'20' , 'style': {'color': '#F9F9F9'}},
                        30: {'label':'30' , 'style': {'color': '#F9F9F9'}},
                        40: {'label':'40' , 'style': {'color': '#F9F9F9'}}
                
                    }
                ),
            ],className = 'MySlider'),

        ] , no_gutters = True ,style = {'padding':'30px','margin':'0px'} ,align="center" ,justify="center"),

      ]),


    html.Div([

        mf.GenerateSectionHeading("Economic growth factors"),

    dbc.Row([

        

        dbc.Col([

            html.I(className="fas fa-seedling fa-3x", style = {'display': 'inline-block', 'width': '100%'}),
            html.Div(id='GrowthRate-output-container' ,className = 'MySlider'),
            dcc.Slider(
                    id='GrowthRate-slider',
                    min = 0,
                    max= 0.15,
                    step=0.005,
                    value= 0.07,
                    marks={
                        0: {'label':'0%' , 'style': {'color': '#F9F9F9'}},
                        0.05: {'label':'5%' , 'style': {'color': '#F9F9F9'}},
                        0.1: {'label':'10%' , 'style': {'color': '#F9F9F9'}},
                        0.15: {'label':'15%' , 'style': {'color': '#F9F9F9'}},
                
                    }
                ),
            ],className = 'MySlider'),


        dbc.Col([
            html.I(className="fas fa-shopping-basket fa-3x", style = {'display': 'inline-block', 'width': '100%'}),
            html.Div(id='Inflation-output-container' ,className = 'MySlider'),
            dcc.Slider(
                    id='Inflation-slider',
                    min = 0,
                    max= 0.1,
                    step= 0.005,
                    value= 0.05,
                    marks={
                        0: {'label':'0%' , 'style': {'color': '#F9F9F9'}},
                        0.05: {'label':'5%' , 'style': {'color': '#F9F9F9'}},
                        0.075: {'label':'7.5%' , 'style': {'color': '#F9F9F9'}},
                        0.1: {'label':'10%' , 'style': {'color': '#F9F9F9'}},
                    }
                ),
            ],className = 'MySlider'),
        


            ], style = {'padding':'30px' , 'margin':'0px'} ,align="center" ,justify="center"),

        ],className = 'MySlider'),
    
        mf.GenerateSectionHeading("Your retirement savings results"),
    
    html.Div(children = [
    html.Div(
        html.Div( children = [
            html.Div(children = [ 

                html.H6("Projected retirement assets (in today's terms)"
                         ,className="m-0 text-secondary text-center"
                         
                        
                         
                        )

            ]

                ,className = "card-header"
                     ,style = {'justify-content':' center'}
             
                    ),
            html.Div( 
                children = [
                    html.Div( 
                        children = [
                                html.Div([
                                    dcc.Graph( id='Projected-retirement-assets',config={"displayModeBar": False},)
                                ]
                                ),
                        ],
                        className = "chart-container"
                    ) 
            
                ]
                ,className="card-body pt-4 pb-2"
                ,style = {'background-color':'#3C415C'}
            )
            
        ],className = "card shadow mb-2"
                )
        ,className = "col-xl-6 col-lg-6 "  
    ),

    
        html.Div(
        html.Div( children = [
            html.Div(children = [ 

                html.H6("Monthly retirement income (in today's terms)"
                         ,className="m-0 text-secondary text-center"
                        ,style = {'justify-content':' center'}
                         
                        )

            ]

                ,className = "card-header"
                     ,style = {'justify-content':' center'}
                     
             
                    ),
            html.Div( 
                children = [
                    html.Div( 
                        children = [
                                html.Div([
                                    dcc.Graph( id='Retirement-Income-assets'
                                              ,config={"displayModeBar": False}
                                              ,style = {'width':'100%','height':'100%'})
                                ]
                                ),
                        ],
                        className = "chart-container"
                    ) 
            
                ]
                ,className="card-body pt-4 pb-2"
                ,style = {'background-color':'#3C415C'}
            )
            
        ],className = "card shadow mb-2"
                )
        ,className = "col-xl-6 col-lg-6"  
    )
        ],className = "row"
        ,style = {'margin':'0px'}     
            ),


    
            
    html.Div(
        dbc.NavLink(children = [
            html.I(className="fab fa-linkedin fa-3x"
                  ),
            html.Div(html.Span('Copyright © 2021'),className = "copyright text-center my-auto")
        ]          
                    ,style = {'color':'White','padding':"5% 0%"}
                    ,href="https://www.linkedin.com/in/michael-botha-tassa-a891ab9b/"
                   
        ) 
        ,className = "copyright text-center my-auto"
    ),

], style = {'background-color': '#2978B5'
            , 'width': '100%'
            , 'height': '100%'
            , 'margin': '0px'
            , 'padding': '0px'
            , 'overflow-x': 'hidden'})


@app.callback(Output('AmountsliderType-output-container', 'children')
              ,Input('Investment-type-dropdown', 'value'))

def InvestmentTypegetter(typeselected):

    if typeselected == 'Lump-sum':

        slidervalues = html.Div( children = [
            html.Div(children = [  
                html.Div(id='Principal-output-container',style = {'width':'50%','margin':'auto'}),
            ],className = "card-header py-3 d-flex flex-row align-items-center justify-content-between text-center"
                    ),
            html.Div( 
                children = [
                    html.Div( 
                        children = [
                                dcc.Slider(
                                    id='Principal-investment-slider',
                                    min = 100000,
                                    max= 10000000,
                                    step=50000,
                                    value=100000,
                                    marks={
                                        100000: {'label':'R100k' , 'style': {'color': '#F9F9F9'}},
                                        1000000: {'label':'R1 mil' , 'style': {'color': '#F9F9F9'}},
                                        5000000: {'label':'R5 mil' , 'style': {'color': '#F9F9F9'}},
                                        10000000: {'label':'R10 mil' , 'style': {'color': '#F9F9F9','width':'100%'}},
                                    }
                                ),
                        ],
                        className = "chart-container"
                    ) 
            
                ]
                ,className="card-body pt-4 pb-2"
                ,style = {'background-color':'#3C415C'}
            )
            
        ],className = "card shadow mb-2"
                
                               )
        
    else:

         slidervalues = html.Div( children = [
            html.Div(children = [  
                html.Div(id='Principal-output-container',style = {'width':'50%','margin':'auto'}),
            ],className = "card-header py-3 d-flex flex-row align-items-center justify-content-between text-center"
                    ),
            html.Div( 
                children = [
                    html.Div( 
                        children = [
                                dcc.Slider(
                                    id='Principal-investment-slider',
                                    min = 500,
                                    max= 30000,
                                    step= 100,
                                    value= 1000,
                                    marks={
                                        500: {'label':'R500' , 'style': {'color': '#F9F9F9'}},
                                        5000: {'label':'R5 000' , 'style': {'color': '#F9F9F9'}},
                                        10000: {'label':'R10 000' , 'style': {'color': '#F9F9F9'}},
                                        30000: {'label':'R30 000' , 'style': {'color': '#F9F9F9','width':'100%'}},
                                    }
                                ),
                        ],
                        className = "chart-container"
                    ) 
            
                ]
                ,className="card-body pt-4 pb-2"
                ,style = {'background-color':'#3C415C'}
            )
            
        ],className = "card shadow mb-2"
                
                               )

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
               Input('TargetretirementIncome-slider', 'value'),
               Input('Investment-type-dropdown', 'value')])


def CalculateRetirement(Client_age,Client_Retirement_Age,TermInRetirement,InvestmentAmount, Client_GrowthRate,Client_Inflation , Client_target_Income,investmentType3 ):

    age = Client_age
    RetireMentAge = Client_Retirement_Age
    MaxDrawdown = 0.175
    MinDrawdown = 0.025
    Fundvalue = InvestmentAmount
    RecurringContribution = InvestmentAmount
    period = RetireMentAge - age + 1 + TermInRetirement
    GrowthRate = Client_GrowthRate
    Inflation = Client_Inflation
    RealReturn = ((1+ GrowthRate)/(1+Inflation ) -1)
    MonthlyRealreturn = (1+RealReturn)**(1/12) -1
    N_rows = period
    N_cols = 6
    ValuesMatrix = pd.DataFrame(np.zeros((N_rows, N_cols)))
    TargetIncome = Client_target_Income

    for x in range(period):

        if (x + age) <  RetireMentAge :

            ValuesMatrix.iloc[x][0] = age + x

            if investmentType3 == 'Lump-sum':

                if x == 0 :
                    ValuesMatrix.iloc[x][1] = Fundvalue
                else :
                    ValuesMatrix.iloc[x][1] = ValuesMatrix.iloc[x-1][3]

                ValuesMatrix.iloc[x][2] = ValuesMatrix.iloc[x][1]*RealReturn
                ValuesMatrix.iloc[x][3] = ValuesMatrix.iloc[x][2] + ValuesMatrix.iloc[x][1]
                ValuesMatrix.iloc[x][5] = ValuesMatrix.iloc[x][3]

            else:

                if x == 0 :
                    ValuesMatrix.iloc[x][1] = 0
                else :
                    ValuesMatrix.iloc[x][1] = ValuesMatrix.iloc[x-1][3]

                ValuesMatrix.iloc[x][2] = ValuesMatrix.iloc[x][1]*RealReturn
                ValuesMatrix.iloc[x][3] = ValuesMatrix.iloc[x][2] + ValuesMatrix.iloc[x][1] + RecurringContribution*(((1+MonthlyRealreturn)**12 -1)/MonthlyRealreturn)
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
    
    AmountInvestedmessage = html.H6('You want to invest R{}'.format(InvestmentAmount),className="m-0 text-secondary text-center")
    TargetRetirementIncomemessage = html.H6( 'Required monthly income in retirement: R{} '.format(Client_target_Income),className="m-0 text-secondary text-center")
    
    return 'You are {} years of age'.format(Client_age), 'You want to retire at {} years of age'.format(Client_Retirement_Age), 'You will live {} years in retirement'.format(TermInRetirement), AmountInvestedmessage , '{}% nominal growth per year'.format(Client_GrowthRate),  '{}% inflation per year'.format(Client_Inflation) ,TargetRetirementIncomemessage, RetirementGraph, RetirementIncome


@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/InvestmentCalculator':
        return page_2_layout
    elif pathname == '/Mortgagecalcs':
        return page_1_layout
    else:
        return page_1_layout


if __name__ == "__main__":
    app.run_server(debug=False)

