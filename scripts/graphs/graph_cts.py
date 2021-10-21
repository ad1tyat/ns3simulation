import matplotlib.pyplot as plt
x = [0,256,512,1000]
y = [0.0762158203125,0.051141357421875,0.0511798095703125,0.0508831787109375]
y2 = [0.0781903076171875,0.0539825439453125,0.05402313232421875,0.05371002197265625]
y3 = [0.0781866455078125,0.0539825439453125,0.05402313232421875,0.05371002197265625]
# plotting the points
plt.plot(x, y, color='green',linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=6, label='Node 1')
plt.plot(x, y2, color='red',linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=6, label='Node 0')
plt.plot(x, y3, color='blue',linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=6, label='Node 2')
plt.xlabel('RTS Threshold in bytes',color="red")
plt.ylabel('Average Bandwidth spent in transmitting CTS in Mbps',color="red")
plt.title('Graph of Average Bandwidth spent vs RTS Threshold',color="magenta")
plt.legend()
plt.show()