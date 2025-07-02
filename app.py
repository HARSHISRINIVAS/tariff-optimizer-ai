from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)

@app.route('/')
def index():
    df = pd.read_csv(r'C:\Users\VASAVI\Downloads\inspro\Tariff_data.csv')
    df.dropna(subset=['year', 'value'], inplace=True)
    df['year'] = df['year'].astype(int)
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    df.dropna(subset=['value'], inplace=True)
    yearly_trade = df.groupby('year')['value'].sum().reset_index()
    fig = px.line(
        yearly_trade,
        x='year',
        y='value',
        title='India vs USA Trade',
        labels={
            'year': 'Year',
            'value': 'Total Trade Value (USD)'
        },
        width=900,
        height=500
    )
    fig.update_layout(showlegend=False)

    graph_html = pio.to_html(fig, full_html=False)

    return render_template('index.html', graph_html=graph_html)

if __name__ == '__main__':
    app.run(debug=True)
