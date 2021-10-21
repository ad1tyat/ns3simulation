import sys
import dpkt
import struct
import socket
import binascii


l = ['0', '256','512','1000']

out=open('tcp_ack_ap.txt','w')
out1=open('tcp_seg_ap.txt','w')

for rts_thres in l:
	ele1=rts_thres
	filename = 'assignment-4-data/'+ele1+'/AccessPoint-1-0.pcap'
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

out=open('tcp_ack_sta1.txt','w')
out1=open('tcp_seg_sta1.txt','w')

for rts_thres in l:
	ele2=rts_thres
	filename = 'assignment-4-data/'+ele2+'/Station-0-0.pcap'
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
	out.write(ele2+' '+str(x1)+'\n')
	out1.write(ele2+' '+str(x2)+'\n')

out.close()
out1.close()

out=open('tcp_ack_sta2.txt','w')
out1=open('tcp_seg_sta2.txt','w')

for rts_thres in l:
	ele3=rts_thres
	filename = 'assignment-4-data/'+ele3+'/Station-2-0.pcap'
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
				#print("a")
				frame_tcp_ack += 1
				frame_tcp_Ack_total += len(packet)
			if len(tcp.data) >0 :
				frame_tcp_seg += 1
				frame_tcp_seg_total += len(packet)
		except dpkt.Error as e:
			zz =1


	x1 = (frame_tcp_Ack_total*8.00)/(1024*1024*50)
	x2 = (frame_tcp_seg_total*8.00)/(1024*1024*50)
	out.write(ele3+' '+str(x1)+'\n')
	out1.write(ele3+' '+str(x2)+'\n')

out.close()
out1.close()