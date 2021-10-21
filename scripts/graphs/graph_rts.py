import matplotlib.pyplot as plt
x = [0,256,512,1000]
y = [0.09903594970703125,
0.06676788330078125,
0.06681808471679687,
0.06643081665039062]

y2 = [0.09924560546875,
0.0686053466796875,
0.06870437622070312,
0.06835250854492188
]
y3 = [0.09922607421875,
0.06860076904296875,
0.068406982421875,
0.06807510375976562
]
# plotting the points
plt.plot(x, y, color='green',linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=6, label='Node 1')
plt.plot(x, y2, color='red',linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=6, label='Node 0')
plt.plot(x, y3, color='blue',linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=6, label='Node 2')
plt.xlabel('RTS Threshold in bytes',color="red")
plt.ylabel('Average Bandwidth spent in transmitting RTS in Mbps',color="red")
plt.title('Graph of Average Bandwidth spent vs RTS Threshold',color="magenta")
plt.legend()
plt.show()