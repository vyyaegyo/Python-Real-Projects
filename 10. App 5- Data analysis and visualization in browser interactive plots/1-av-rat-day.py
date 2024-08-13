# Data visualization by using Javascripts from Highchart
import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

data = pandas.read_csv("/Users/nguyenthuyvy/Desktop/Basic Knowledge/PYTHON/Python Projects_Oreilly/10 Python Projects/Python_Real_Projects/9. App 4- Data analysis and visualization with pandas and Matplotlib/reviews.csv", parse_dates=['Timestamp'])
data['Day'] = data['Timestamp'].dt.date #dt gives you convenient access to operations on data stored as a pandas datetime
numeric_columns = data.select_dtypes(include='number').columns.tolist()
group_columns = ['Day'] + numeric_columns
day_average = data[group_columns].groupby(['Day']).mean() 

chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude',
        align: 'left'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model',  
        align: 'left'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: [
            [0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]
        ]

    }]
}
"""
def app():
    # Create a Quasar page
    wp = jp.QuasarPage()
    # Add a header
    h1 = jp.QDiv(a=wp, text="Analysis of Course Review", classes="text-h2 text-center q-mt-lg")
    # Add a paragraph
    p1 = jp.QDiv(a=wp, text="These graphs represent Course Review Analysis", classes="text-body1 text-center q-mt-md")
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.title.text = "Average Rating by Day"
    
    hc.options.xAxis.categories = list(day_average.index)
    hc.options.series[0].data = list(day_average['Rating'])
    print(type(hc.options))

    return wp
jp.justpy(app, port=8080)

