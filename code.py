import statistics
import csv
import pandas as pd
import plotly.figure_factory as ff
import random
import plotly.graph_objects as go

df=pd.read_csv("StudentsPerformance.csv")
data=df["math score"].tolist()
mean=sum(data)/len(data)

median=statistics.median(data)

mode=statistics.mode(data)

std_dvi=statistics.stdev(data)

#Finding first standard deviation start and end values and second standard deviation start and end values
first_stdev_start, first_stdev_end=mean-std_dvi, mean+std_dvi
second_stdev_start, second_stdev_end=mean-(2*std_dvi), mean+(2*std_dvi)
third_stdev_start, third_stdev_end=mean-(3*std_dvi), mean+(3*std_dvi)

#Plotting the chart for mean and standard deviation 1&2
fig=ff.create_distplot([data], ["math score"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean], y=[0,0.17],mode="lines", name="mean"))
fig.add_trace(go.Scatter(x=[first_stdev_start, first_stdev_start], y=[0,0.17], mode="lines", name="1st standard deviation start"))
fig.add_trace(go.Scatter(x=[first_stdev_end, first_stdev_end], y=[0,0.17], mode="lines", name="1st standard deviation end"))
fig.add_trace(go.Scatter(x=[second_stdev_start, second_stdev_start], y=[0,0.17], mode="lines", name="2nd standard deviation start"))
fig.add_trace(go.Scatter(x=[second_stdev_end, second_stdev_end], y=[0,0.17], mode="lines", name="2nd standard deviation end"))
fig.add_trace(go.Scatter(x=[third_stdev_start, third_stdev_start], y=[0,0.17], mode="lines", name="3d standard deviation start"))
fig.add_trace(go.Scatter(x=[third_stdev_end, third_stdev_end], y=[0,0.17], mode="lines", name="3d standard deviation end"))
fig.show()

list_of_data_within_1_std_deviation = [result for result in data if result > first_stdev_start and result < first_stdev_end]
list_of_data_within_2_std_deviation = [result for result in data if result > second_stdev_start and result < second_stdev_end]
list_of_data_within_3_std_deviation = [result for result in data if result > third_stdev_start and result < third_stdev_end]

print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(data)))
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(data)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(data)))
#print(std_dvi)
#print(mode)
#print(median)
#print(mean)
    