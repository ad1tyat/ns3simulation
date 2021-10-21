import matplotlib.pyplot as plt
x = [0,256,512,1000]

y = [36.43165267944336,36.94763046264649,36.95012252807617,36.96378280639649]
y2 = [36.43182815551758,36.786727600097656,36.78437225341797,36.81735641479492]
y3 = [36.431999359130856,36.78516937255859,36.807233276367185,36.82450698852539]


plt.plot(x, y, color='green',linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=6, label='Node 1')
plt.plot(x, y2, color='red',linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=6, label='Node 0')
plt.plot(x, y3, color='blue',linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=6, label='Node 2')
plt.xlabel('RTS Threshold in bytes',color="red")
plt.ylabel('Average Bandwidth spent in transmitting TCP SEGs in Mbps',color="red")
plt.title('Graph of Average Bandwidth spent vs RTS Threshold',color="magenta")
plt.legend()


plt.show()

