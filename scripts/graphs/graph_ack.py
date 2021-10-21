import matplotlib.pyplot as plt
x = [0,256,512,1000]
y =[0.0008575439453125, 0.00140777587890625, 0.0013323974609375, 0.00141845703125]
y2 =[0.0008441162109375, 0.001376953125,0.00130523681640625,0.00139404296875]
y3 =[0.000843505859375, 0.00138397216796875, 0.00130889892578125, 0.001390380859375]
# plotting the points
plt.plot(x, y, color='green',linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=6, label='Node 1')
plt.plot(x, y2, color='red',linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=6, label='Node 0')
plt.plot(x, y3, color='blue',linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=6, label='Node 2')
plt.xlabel('RTS Threshold in bytes',color="red")
plt.ylabel('Average Bandwidth spent in transmitting ACK in Mbps',color="red")
plt.title('Graph of Average Bandwidth spent vs RTS Threshold',color="magenta")
plt.legend()
plt.show()