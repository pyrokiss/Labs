import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

lamb = 5
num_events = 100
event_num = []
inter_event_times = []
event_times = []
event_time = 0


def plot_graph(a, b, name):
	fig = plt.figure()
	plot, = plt.plot(a, b, label=name)
	plt.legend(handles=[plot])
	plt.xlabel('Index of event')
	plt.ylabel('Time')
	plt.show()

def bar_graph(a, b):
	fig = plt.figure()
	plt.bar(a, b)
	plt.xlabel('Index of interval')
	plt.ylabel('Number of events')
	plt.show()

def s_formula(lamb, size):
	array = np.random.rand(size)
	result = -np.log(1.0 - array) / lamb
	return result

header_1 = ["EVENT_NUM", "INTER_EVENT_T", "EVENT_T"]
table_1 = [header_1]

for i in range(num_events):
	event_num.append(i)
	n = np.random.rand()
	inter_event_time = -np.log(1.0 - n) / lamb
	inter_event_times.append(inter_event_time)
	event_time = event_time + inter_event_time
	event_times.append(event_time)
	table_1.append([str(i), str(inter_event_time), str(event_time)])
print(tabulate(table_1))

plot_graph(event_num, event_times, 'Absolute time of event')

hist = np.array([np.sum(s_formula(lamb, 1)) for i in range(num_events)])
plt.hist(hist, 50, edgecolor = "white")
plt.show()

plt.hist(s_formula(lamb, num_events), 50, edgecolor = "white")
plt.show()

interval_nums = []
num_events_in_interval = []
interval_num = 1
num_events = 0


header_2 = ['INTERVAL_NUM', 'NUM_EVENTS']
table_2 = [header_2]
for i in range(len(event_times)):
	event_time = event_times[i]
	if event_time <= interval_num:
		num_events += 1
	else:
		interval_nums.append(interval_num)
		num_events_in_interval.append(num_events)
		table_2.append([str(interval_num), str(num_events)])
		interval_num += 1
		num_events = 1

print(tabulate(table_2))
print("Mean: ",np.mean(num_events_in_interval))
print("Var: ",np.var(num_events_in_interval))

bar_graph(interval_nums, num_events_in_interval)