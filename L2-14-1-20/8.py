import plotly.express as px

data = dict(
    number=[50,110,250,180,70],
    stage=["Requirement Elicitation","Requirement Analysis","Software Development","Debugging & Testing","Others"])
fig = px.funnel(data, x='number', y='stage')
fig.show()
