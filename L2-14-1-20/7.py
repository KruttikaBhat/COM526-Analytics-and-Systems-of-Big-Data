
import plotly.graph_objects as go

categories = ["Quarter 1","Quarter 2","Quarter 3","Quarter 4"]

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=[10,6,8,13],
      theta=categories,
      fill='toself',
      name='Textile'
))
fig.add_trace(go.Scatterpolar(
      r=[5,5,2,4],
      theta=categories,
      fill='toself',
      name='Jewellery'
))
fig.add_trace(go.Scatterpolar(
      r=[15,20,16,15],
      theta=categories,
      fill='toself',
      name='Cleaning Essentials'
))
fig.add_trace(go.Scatterpolar(
      r=[14,10,21,11],
      theta=categories,
      fill='toself',
      name='Cosmetics'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 25]
    )),
  showlegend=True
)

fig.show()
