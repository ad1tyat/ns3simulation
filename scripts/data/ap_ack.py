import sys
import dpkt
import struct
import socket
import itertools
import binascii

l = ['0', '256', '512', '1000']
out = open('ap_ack.txt','w')

for rts_thres in l:
	ele1 = rts_thres
	filename = 'assignment-4-data/'+ele1+'/AccessPoint-1-0.pcap'
	f = open(filename, 'rb')
	print(filename)
	pcap = dpkt.pcap.Reader(f)

	frame_rts = 0
	frame_rts_total = 0
	for ts,packet in pcap:
		tap = dpkt.radiotap.Radiotap(packet)
		t_len = binascii.hexlify(packet[2:3])
		t_len = int(t_len, 16)
		ieee80211Frame = packet[t_len:]
		sequenceControl = packet[t_len + 22:t_len + 24]
		wlan = dpkt.ieee80211.IEEE80211(ieee80211Frame)

		if wlan.subtype == dpkt.ieee80211.C_ACK:
			frame_rts_total  = frame_rts_total + len(packet)
			frame_rts = frame_rts + 1
	x = (frame_rts_total*8.00)/(1024*1024*50)
	ele2 = rts_thres
	out.write(str(x)+' '+ele2+'\n')

out.close()

out = open('sta1_ack.txt','w')

for rts_thres in l:
	ele1=rts_thres
	filename = 'assignment-4-data/'+ele1+'/AccessPoint-1-0.pcap'
	f = open(filename, 'rb')
	print(filename)
	pcap = dpkt.pcap.Reader(f)

	frame_rts = 0
	frame_rts_total = 0
	for ts,packet in pcap:
		packet = packet
		tap = dpkt.radiotap.Radiotap(packet)
		t_len = binascii.hexlify(packet[2:3])
		t_len = int(t_len, 16)
		ieee80211Frame = packet[t_len:]
		sequenceControl = packet[t_len + 22:t_len + 24]
		wlan = dpkt.ieee80211.IEEE80211(ieee80211Frame)

		if wlan.subtype == dpkt.ieee80211.C_ACK:
			frame_rts_total  = frame_rts_total + len(packet)
			frame_rts = frame_rts + 1
	x = (frame_rts_total*8.00)/(1024*1024*50)
	ele2=rts_thres
	out.write(str(x)+' '+ele2+'\n')
out.close()


out = open('sta2_ack.txt','w')

for rts_thres in l:
	ele1=rts_thres
	filename = 'assignment-4-data/'+ele1+'/AccessPoint-1-0.pcap'
	f = open(filename, 'rb')
	print(filename)
	pcap = dpkt.pcap.Reader(f)

	frame_rts = 0
	frame_rts_total = 0
	for ts,packet in pcap:
		packet = packet
		tap = dpkt.radiotap.Radiotap(packet)
		t_len = binascii.hexlify(packet[2:3]) 
		t_len = int(t_len, 16)
		ieee80211Frame = packet[t_len:]
		sequenceControl = packet[t_len + 22:t_len + 24]
		wlan = dpkt.ieee80211.IEEE80211(ieee80211Frame)
		
		if wlan.subtype == dpkt.ieee80211.C_ACK:
			frame_rts_total  = frame_rts_total + len(packet)
			frame_rts = frame_rts + 1
	x = (frame_rts_total*8.00)/(1024*1024*50)
	ele2=rts_thres
	out.write(str(x)+' '+ele2+'\n')

out.close()
