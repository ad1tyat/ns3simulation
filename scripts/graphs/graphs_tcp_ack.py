import matplotlib.pyplot as plt
x = [0,256,512,1000]
y = [18.221826324462892,18.47938491821289,18.481697235107422,18.486190490722656]
y2 = [18.221991424560546,18.39738494873047,18.398790740966795,18.412581787109374]
y3 = [18.22216323852539,18.397979736328125,18.409461517333984,18.415886840820313]

plt.plot(x, y, color='green',linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=6, label='Node 1')
plt.plot(x, y2, color='red',linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=6, label='Node 0')
plt.plot(x, y3, color='blue',linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=6, label='Node 2')
plt.xlabel('RTS Threshold in bytes',color="red")
plt.ylabel('Average Bandwidth spent in transmitting TCP ACK in Mbps',color="red")
plt.title('Graph of Average Bandwidth spent vs RTS Threshold',color="magenta")
plt.legend()

plt.show()

