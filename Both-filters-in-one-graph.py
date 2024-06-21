import pandas as pd
import plotly.graph_objects as go

# Load the data from the CSV files
lu_data = pd.read_csv('LU0422T.csv', skiprows=1, names=['Wavelength', 'Transmittance'])
sh_data = pd.read_csv('SH0385T.csv', skiprows=1, names=['Wavelength', 'Transmittance'])
sp_data = pd.read_csv('SPF500T1.csv', skiprows=1, names=['Wavelength', 'Transmittance'])

# Create traces for the plot
trace1 = go.Scatter(x=lu_data['Wavelength'], y=lu_data['Transmittance'], mode='lines', name='LU0422')
trace2 = go.Scatter(x=sh_data['Wavelength'], y=sh_data['Transmittance'], mode='lines', name='SH0385')
trace3 = go.scatter(x=sp_data['Wavelength'], y=sp_data['Transmittance'], mode='lines', name='SPF500T1')


# Define the layout of the plot
layout = go.Layout(
    title='Transmittance Curves',
    xaxis=dict(title='Wavelength (nm)'),
    yaxis=dict(title='Transmittance (%)'),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

# Create the figure and plot it
fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)
fig.show()
