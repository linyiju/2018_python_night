#20180820 學習如何用plotly畫圖

#1. plotly網站上下載(https://plot.ly/python/getting-started/)
#2.在網站上sign up 
#3.setting -> API Keys 

# import plotly
# plotly.tools.set_credentials_file(username='lynn8301', api_key='9G6Tzf9qnbThzvn0YUW0')
import plotly.plotly as py
import plotly.graph_objs as go

#建立資料
#1.圓餅圖
# Pie = go.Pie(
#     labels=["Google","Yahoo","Bing"],
#     values=[70,15,15]
# )
# data = [Pie]

#2.長條圖
line1 = go.Scatter(
    x=[1,2,3,4],
    y=[400,300,200,100],
    line={
        "shape":"spline"
    }
)
line2 = go.Scatter(
    x=[1,2,3,4],
    y=[100,200,300,400]
)
data = [line1,line2]

#畫圖
# py.plot(data,filename="mychart-Pie") #畫圓餅圖
py.plot(data,filename="mychart-Scatter")