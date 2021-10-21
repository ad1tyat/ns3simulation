import dpkt
import binascii

rts_sizes = ['0', '256', '512', '1000']

outarr= ['node1_cts.txt', 'node0_cts.txt', 'node2_cts.txt']
inarr = ['/AccessPoint-1-0.pcap', '/Station-0-0.pcap', '/Station-2-0.pcap']

def ratio(x):
	return (x*8.00)/(1024*1024*50)

for i in range(3):

	out = open(outarr[i],'w')

	for rts_thres in rts_sizes:
		ele1=rts_thres
		filename = 'assignment-4-data/'+ele1+ inarr[i]
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

			if wlan.subtype == dpkt.ieee80211.C_CTS:
				frame_rts_total  = frame_rts_total + len(packet)
				frame_rts = frame_rts + 1
		x = ratio(frame_rts_total)
		ele2 = rts_thres
		out.write(str(x)+' '+ele2+'\n')
	out.close()
