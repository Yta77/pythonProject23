import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=2)

def layout():
    return html.Div([
    html.H3("People that I've had the pleasure to work with", style={'textAlign':'center'}, className='my-3'),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('#### Romeo Francia'),
            dcc.Markdown('Group Risk Control Consorzio Romagna Energia')
        ], width=2),
        dbc.Col([
            dcc.Markdown('Carlo is very professional. I really appreciate his quick thinking '
                         'and great teamwork. We enjoyed to build up the Risk Desk for our Company '
                         'i recommend working with himself.',
                         className='ms-3'),
        ], width=5)
    ], justify='center'),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('#### Mr.Imran'),
            dcc.Markdown('CFO Al Baraa')
        ], width=2),
        dbc.Col([
            dcc.Markdown('Carlo is always ready to help others and give his point of view with no fears'
                         'And he always shares goal opportunities with his teammates. Carlo likes works with people '
                         'and he is also an hard-worker',
                         className='ms-3'),
        ], width=5)
    ], justify='center'),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('#### Alessandro Misale '),
            dcc.Markdown('Head of Risk Control at ENGIE')
        ], width=2),
        dbc.Col([
            dcc.Markdown('I feel so lucky to have had a teammate like Carlo on my team. He is a self starter and proactive Manager '
                         'Carlo always looks forward and he is always ready to support others '
                         'I am happy to have spent time with him',
                         className='ms-3'),
        ], width=5)
    ], justify='center')
])