from dash import Dash, html, dcc, callback, Output, Input
from dash.dash_table import DataTable
import plotly.express as px
import pandas as pd
import pathlib
import os

# Read all sectors dynamically
sector_paths = list(pathlib.Path('data').glob('*.xlsx'))
sectors = [path.stem for path in sector_paths]  # Correct way to get names


# Load all data
data_sectors = {
    sector: pd.read_excel(f"data/{sector}.xlsx") for sector in sectors
}

# Convert formula columns to title
formula_titles = {
    "Entreprise": "Entreprise",
    "resultat / vc": "ROE( resultat / vc )",
    "resultat/total actif": "ROA( resultat / total actif )",
    "dette /total": "ratio 1( dette / total )",
    "dette / total passif": "ratio 2( dette / total passif)",
    "R&D/vc": "S.R.Kloe( R&D / vc )",
}
app = Dash(__name__)
app.title = 'Dashboard'
server = app.server   # VERY IMPORTANT for gunicorn

app.layout = html.Div([
    html.H1(children='Dashboard des entreprises par secteur dans la bourse de Tunis',
            style={"font-family": "Arial", "margin": "20px 40px", "color": "#333"}),

    html.Div([
        dcc.Dropdown(sectors, id='dropdown-selection', multi=False,
                     value=sectors[0], style={'width': '40%', "margin": "20px 0"}),
        html.H2(children='Tableau des entreprises par secteur',
                style={'fontSize': '20px', "color": "#333", "font-family": "Arial"}),
        DataTable(
            id='data-table',
            columns=[{"name": formula_titles[col], "id": col}
                     for col in data_sectors[sectors[0]].columns],
            style_table={'overflowX': 'auto'},
            style_cell={'textAlign': 'left', 'padding': '5px'},
            style_header={'backgroundColor': 'lightgrey', 'fontWeight': 'bold'}
        ),
        html.Div(
            [
                html.H2(children='Graphique des entreprises par secteur',
                        style={'fontSize': '20px', "color": "#333", "font-family": "Arial"}),
                dcc.Graph(id='graph-content'),

            ],
            style={'margin': '20px 0', 'padding': '10px', 'border-radius': '10px',
                   'border': '1px solid #ccc',
                   }
        )

    ], style={
        'border-radius': '10px',
        'padding': '20px',
        'margin': '20px 40px',
        'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.2)'
    }),
])


@callback(
    [Output('graph-content', 'figure'),
     Output('data-table', 'data')],
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = data_sectors[value]
    id_column = dff.columns[0]
    # Pass to percentage
    dff.iloc[:, 1:] = dff.iloc[:, 1:].apply(lambda x: x * 100, axis=1)

    # Melt the dataframe
    dff_melted = dff.melt(
        id_vars=[id_column], var_name='Metric', value_name='Value'
    )
    dff_melted = dff_melted.rename(columns=formula_titles)

    # Create figure
    fig = px.bar(
        dff_melted,
        x=id_column,
        y='Value',
        color='Metric',
        barmode='group',
        height=800,
    )

    fig.update_layout(
        xaxis_title='Entreprise',
        yaxis_title='Pourcentage (%)',
        legend_title='Metric',
        xaxis_tickangle=15,
        xaxis_title_font=dict(
            family="Arial Black",    # Font family
            size=16,           # Font size
            color="#333",      # Font color
        ),
        yaxis_title_font=dict(
            family="Arial Black",  # Bolder font family
            size=16,
            color="#333"
        ),


    )

    return fig, dff.to_dict('records')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
