#!/usr/bin/env python
# coding: utf-8

# In[2]:


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

image_filename = 'FinicalLogoWithoutWording.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

def GenerateNavBar():
    MyNavBar = dbc.Navbar(
    [

                html.A(
                    html.Img(
                        src='data:image/png;base64,{}'.format(encoded_image.decode())
                        ,height='70px'
                        ,width='70px'
                        ,className = "float-left"
                    )
                    ,className ="nav-link float-left"
                ),



        html.Ul(

            html.Ul(

                html.A(
                    dbc.NavbarBrand("Finical advisory (ltd)")
                    ,style = {"width":"auto" , 'margin':'0%','padding':'0px'}
                    ,className =" navbar-nav float-left no-arrow"
                )


                ,className ="nav-item dropdown no-arrow"

            )

            ,className ="nav navbar-nav ml-auto no-arrow"
        ),


        dbc.DropdownMenu(right=True,
                         label="Choose your calculator",
                         children=[
                             dbc.DropdownMenuItem(dbc.NavLink("Investment calculator", href="/InvestmentCalculator")),
                             dbc.DropdownMenuItem(dbc.NavLink("Mortgage calculator", href="/Mortgagecalcs")),
                         ]
                         ,className = 'float-right'

                        ),


                ]
                ,color="#3C415C"
                ,dark=True
                ,className = "shadow"
                ,style = {"padding":'0% 10%'}
            )

    return MyNavBar


def GenerateInput(InputId,Minimum,Maximum,VariableType,DefaultValue,PlaceHolderValue):

    inputDiv = dbc.Col(
    [

            dbc.Input(id=InputId, placeholder=PlaceHolderValue, type=VariableType, min = Minimum, max = Maximum, value= DefaultValue, style = {'width':'50%','margin':'auto', 'margin-top':'20px', 'margin-bottom':'20px', 'padding':'20px 10px' })

    ],className = 'MySlider'
            )

    return inputDiv

def GenerateSectionHeading(TextForSectionHeader):
    MySectionHeaderObject =     html.Div(
            children = [
                html.Div(
                    children = [
                        html.Div(
                            children = [
                                html.Div(
                                    children = [
                                        html.Div(
                                            children = [

                                                html.P(children=TextForSectionHeader,className="Graph-header"),

                                            ],className = 'mt-6a text-center small description'
                                        )
                                    ],className = 'card-body pt-2 pb-2'
                                )
                            ],className = 'card shadow mb-2'
                        )
                    ],className = 'col-xl-12 col-lg-12'
                )
            ],className = 'row'
             ,style = {'margin':'0px'}
        )


    return MySectionHeaderObject

def generateRadioInputs(RadioObjectID,input1,input2):

    RadioInputObject = dbc.FormGroup(
        [
                dbc.RadioItems(
                    id=RadioObjectID,
                    options=[
                        {"label": input1, "value": input1},
                        {"label": input2, "value": input2},
                    ],style={'display': 'inline-block'}
                     ,value = input1
                     ,inline = True
                ),
        ]
        ,row=True
        ,style = {'justify-content':' center'}
    )
    return RadioInputObject

def GenerateInputCardObject(CardHeaderSection, InputobjectChoice,ClassNameOuter):
    InputCardObject = html.Div(
        html.Div( children = [
            html.Div(children = [

                CardHeaderSection ,

            ]

                ,className = "card-header py-3 d-flex flex-row align-items-center justify-content-between"
                ,style = {'justify-content':'center'}


                    ),
            html.Div(
                children = [
                    html.Div(
                        children = [
                                html.Div([
                                    InputobjectChoice
                                ],style = {'width':'90%','margin':'auto'}
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
        ,className = ClassNameOuter
    )

    return InputCardObject

def GenerateGraphBackGround(GraphObjectHeading,GraphObjectInput,OuterDivClass):

    GraphBackGround = html.Div(
        html.Div( children = [
            html.Div(children = [

                html.H5(GraphObjectHeading
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
                                    GraphObjectInput
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
        ,className = OuterDivClass
    )

    return GraphBackGround
