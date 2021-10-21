import dpkt
import binascii

l = ['0', '256','512','1000']

outarr= ['tcp_ack_node1.txt', 'tcp_ack_node0.txt', 'tcp_ack_node2.txt']
outarr1= ['tcp_seg_node1.txt', 'tcp_seg_node0.txt', 'tcp_seg_node2.txt']
inarr = ['/AccessPoint-1-0.pcap', '/Station-0-0.pcap', '/Station-2-0.pcap']

for i in range(3):

	out=open(outarr[i],'w')
	out1=open(outarr1[i],'w')

	for rts_thres in l:
		ele1=rts_thres
		filename = 'assignment-4-data/'+ele1+inarr[i]
		f = open(filename, 'rb')
		print(filename)
		pcap=dpkt.pcap.Reader(f)
		frame_tcp_ack=0
		frame_tcp_seg=0
		frame_tcp_Ack_total=0
		frame_tcp_seg_total=0

		for ts,packet in pcap:
			tap = dpkt.radiotap.Radiotap(packet)
			t_len = binascii.hexlify(packet[2:3])  
			t_len = int(t_len, 16)
			ieee80211Frame = packet[t_len:]
			sequenceControl = packet[t_len + 22:t_len + 24]
			wlan = dpkt.ieee80211.IEEE80211(ieee80211Frame)

			try:
				tcp=dpkt.tcp.TCP(wlan.data)
				if(tcp.flags & dpkt.tcp.TH_ACK) != 0:
					frame_tcp_ack += 1
					frame_tcp_Ack_total += len(packet)
				if len(tcp.data) >0 :
					frame_tcp_seg += 1
					frame_tcp_seg_total += len(packet)
			except dpkt.Error as e:
				zz =1


		x1 = (frame_tcp_Ack_total*8.00)/(1024*1024*50)
		x2 = (frame_tcp_seg_total*8.00)/(1024*1024*50)
		out.write(ele1+' '+str(x1)+'\n')
		out1.write(ele1+' '+str(x2)+'\n')

	out.close()
	out1.close()

