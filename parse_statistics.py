from collections import Counter
from IP_packet import *
from stat_sort import *
from stat_count import *
import os

len_tcpdump_file_header = 24
len_packet_header = 16

filename = 'final'

result_root_name = '.\\result_statistics\\result_' + filename + '\\'
if os.path.isdir(result_root_name):
	pass
else:
	os.mkdir(result_root_name)

in_file = 'hex_' + filename + '.txt'
fin = open(in_file, 'r')

lines = fin.read()
list_hex = lines.split()
del list_hex[0:len_tcpdump_file_header]


number = 1

stat_protocol = {}
stat_fragment = {}
stat_fragment_TCP = {}
stat_fragment_UDP = {}
stat_DF = 0
stat_MF = 0
stat_TCP_fragmented = 0
stat_UDP_fragmented = 0

stat_length = []
stat_length_TCP = []
stat_length_UDP = []

stat_TCP_NS  = 0
stat_TCP_CWR = 0
stat_TCP_ECE = 0
stat_TCP_URG = 0
stat_TCP_ACK = 0
stat_TCP_PSH = 0
stat_TCP_RST = 0
stat_TCP_SYN = 0
stat_TCP_FIN = 0

stat_IP = []

localhost_IP = ''

stat_TCP_source = []
stat_TCP_dest = []
stat_UDP_source = []
stat_UDP_dest = []

stat_TCP_source_in = []
stat_TCP_dest_in = []
stat_TCP_source_out = []
stat_TCP_dest_out = []

stat_UDP_source_in = []
stat_UDP_dest_in = []
stat_UDP_source_out = []
stat_UDP_dest_out = []

while len(list_hex) > 0:
	saved_length = int(''.join((list_hex[8:12][::-1])), 16)
	info = IP_packet(list_hex[len_packet_header:saved_length+len_packet_header], number)

	stat_IP += [info.net_source_IP, info.net_destination_IP]
	
	if stat_protocol.has_key(info.net_protocol):
		stat_protocol[info.net_protocol][0] += 1;
		stat_protocol[info.net_protocol][1] += info.net_total_length;
	else:
		stat_protocol[info.net_protocol] = [1, info.net_total_length];
	
	if stat_fragment.has_key(info.net_identification):
		stat_fragment[info.net_identification] += 1;
	else:
		stat_fragment[info.net_identification] = 1;
	
	if info.net_protocol == 6:
		stat_length_TCP += [info.net_total_length]
		if stat_fragment_TCP.has_key(info.net_identification):
			stat_fragment_TCP[info.net_identification] += 1;
		else:
			stat_fragment_TCP[info.net_identification] = 1;
		
		stat_TCP_source += [(info.net_source_IP, info.tf_source_port, info.net_total_length)]
		stat_TCP_dest += [(info.net_destination_IP, info.tf_destination_port, info.net_total_length)]
		
		if info.tf_TCP_NS:	stat_TCP_NS  += 1
		if info.tf_TCP_CWR:	stat_TCP_CWR += 1
		if info.tf_TCP_ECE:	stat_TCP_ECE += 1
		if info.tf_TCP_URG:	stat_TCP_URG += 1
		if info.tf_TCP_ACK:	stat_TCP_ACK += 1
		if info.tf_TCP_PSH:	stat_TCP_PSH += 1
		if info.tf_TCP_RST:	stat_TCP_RST += 1
		if info.tf_TCP_SYN:	stat_TCP_SYN += 1
		if info.tf_TCP_FIN:	stat_TCP_FIN += 1
		
	if info.net_protocol == 17:
		stat_UDP_source += [(info.net_source_IP, info.tf_source_port, info.net_total_length)]
		stat_UDP_dest += [(info.net_destination_IP, info.tf_destination_port, info.net_total_length)]
		
		stat_length_UDP += [info.net_total_length]
		if stat_fragment_UDP.has_key(info.net_identification):
			stat_fragment_UDP[info.net_identification] += 1;
		else:
			stat_fragment_UDP[info.net_identification] = 1;
	
	if info.net_DF:	stat_DF += 1
	if info.net_MF:	stat_MF += 1
	
	stat_length += [info.net_total_length]

	del list_hex[0:saved_length+len_packet_header]
	number += 1
	
counter_IP = Counter(stat_IP)
counter_length = Counter(stat_length)
counter_length_TCP = Counter(stat_length_TCP)
counter_length_UDP = Counter(stat_length_UDP)

localhost_IP = counter_IP.most_common(1)

for item in stat_TCP_source:
	if item[0] == localhost_IP[0][0]:
		stat_TCP_source_out += [[item[0]+':'+str(item[1]), item[2]]]
	else:
		stat_TCP_source_in += [[item[0]+':'+str(item[1]), item[2]]]
		
for item in stat_TCP_dest:
	if item[0] == localhost_IP[0][0]:
		stat_TCP_dest_in += [[item[0]+':'+str(item[1]), item[2]]]
	else:
		stat_TCP_dest_out += [[item[0]+':'+str(item[1]), item[2]]]
		
for item in stat_UDP_source:
	if item[0] == localhost_IP[0][0]:
		stat_UDP_source_out += [[item[0]+':'+str(item[1]), item[2]]]
	else:
		stat_UDP_source_in += [[item[0]+':'+str(item[1]), item[2]]]
		
for item in stat_UDP_dest:
	if item[0] == localhost_IP[0][0]:
		stat_UDP_dest_in += [[item[0]+':'+str(item[1]), item[2]]]
	else:
		stat_UDP_dest_out += [[item[0]+':'+str(item[1]), item[2]]]

for element in stat_fragment_TCP.items():
	if element[1] != 1:
		stat_TCP_fragmented += 1
		
for element in stat_fragment_UDP.items():
	if element[1] != 1:
		stat_UDP_fragmented += 1

stat_TCP_source_out_top10 = stat_sort(stat_TCP_source_out)[0:11]
stat_TCP_source_in_top10 = stat_sort(stat_TCP_source_in)[0:11]
stat_TCP_dest_in_top10 = stat_sort(stat_TCP_dest_in)[0:11]
stat_TCP_dest_out_top10 = stat_sort(stat_TCP_dest_out)[0:11]
stat_UDP_source_in_top10 = stat_sort(stat_UDP_source_in)[0:11]
stat_UDP_source_out_top10 = stat_sort(stat_UDP_source_out)[0:11]
stat_UDP_dest_in_top10 = stat_sort(stat_UDP_dest_in)[0:11]
stat_UDP_dest_out_top10 = stat_sort(stat_UDP_dest_out)[0:11]


#	Output statistics results
	#	Task 1 Protocol
out_file = result_root_name+'statistics_1_' + filename + '.txt'
fout1 = open(out_file, 'w')
print >> fout1, '#Protocol\t#Packets\t#length'
for cata in stat_protocol.items():
	print >> fout1, str(cata[0])+'\t\t'+str(cata[1][0])+'\t\t'+str(cata[1][1])
fout1.close()

	#	Task 2 Fragment
out_file = result_root_name+'statistics_2_' + filename + '.txt'
fout2 = open(out_file, 'w')
print >> fout2, number
print >> fout2, len(stat_fragment)
print >> fout2, len(stat_fragment_TCP)
print >> fout2, stat_TCP_fragmented
print >> fout2, len(stat_fragment_UDP)
print >> fout2, stat_UDP_fragmented
fout2.close()

	#	Task 3	Length
out_file = result_root_name+'statistics_3_total_' + filename + '.txt'
fout3 = open(out_file, 'w')
list_length = sorted(counter_length.most_common(), cmp=lambda x, y:cmp(x[0], y[0]))
for item in list_length:
	print >> fout3, str(item[0])+'\t'+str(item[1])
fout3.close()

out_file = result_root_name+'statistics_3_TCP_' + filename + '.txt'
fout3 = open(out_file, 'w')
list_length = sorted(counter_length_TCP.most_common(), cmp=lambda x, y:cmp(x[0], y[0]))
for item in list_length:
	print >> fout3, str(item[0])+'\t'+str(item[1])
fout3.close()

out_file = result_root_name+'statistics_3_UDP_' + filename + '.txt'
fout3 = open(out_file, 'w')
list_length = sorted(counter_length_UDP.most_common(), cmp=lambda x, y:cmp(x[0], y[0]))
for item in list_length:
	print >> fout3, str(item[0])+'\t'+str(item[1])
fout3.close()

	#	Task 4 Port Traffic
out_file = result_root_name+'stat_TCP_source_out_top10'+ '.txt'
fout4 = open(out_file, 'w')
for item in stat_TCP_source_out_top10:
	print >> fout4, item[0]
	list_length = item[1][1]
	stat_sorted = stat_count(list_length)
	for ele in stat_sorted:
		print >> fout4, str(ele[0])+'\t'+str(ele[1])
fout4.close()

out_file = result_root_name+'stat_TCP_source_in_top10'+ '.txt'
fout4 = open(out_file, 'w')
for item in stat_TCP_source_in_top10:
	print >> fout4, item[0]
	list_length = item[1][1]
	stat_sorted = stat_count(list_length)
	for ele in stat_sorted:
		print >> fout4, str(ele[0])+'\t'+str(ele[1])
fout4.close()
	
out_file = result_root_name+'stat_TCP_dest_out_top10'+ '.txt'
fout4 = open(out_file, 'w')
for item in stat_TCP_dest_out_top10:
	print >> fout4, item[0]
	list_length = item[1][1]
	stat_sorted = stat_count(list_length)
	for ele in stat_sorted:
		print >> fout4, str(ele[0])+'\t'+str(ele[1])
fout4.close()
	
out_file = result_root_name+'stat_TCP_dest_in_top10'+ '.txt'
fout4 = open(out_file, 'w')
for item in stat_TCP_dest_in_top10:
	print >> fout4, item[0]
	list_length = item[1][1]
	stat_sorted = stat_count(list_length)
	for ele in stat_sorted:
		print >> fout4, str(ele[0])+'\t'+str(ele[1])
fout4.close()
	
out_file = result_root_name+'stat_UDP_source_out_top10'+ '.txt'
fout4 = open(out_file, 'w')
for item in stat_UDP_source_out_top10:
	print >> fout4, item[0]
	list_length = item[1][1]
	stat_sorted = stat_count(list_length)
	for ele in stat_sorted:
		print >> fout4, str(ele[0])+'\t'+str(ele[1])
fout4.close()

out_file = result_root_name+'stat_UDP_source_in_top10'+ '.txt'
fout4 = open(out_file, 'w')
for item in stat_UDP_source_in_top10:
	print >> fout4, item[0]
	list_length = item[1][1]
	stat_sorted = stat_count(list_length)
	for ele in stat_sorted:
		print >> fout4, str(ele[0])+'\t'+str(ele[1])
fout4.close()

out_file = result_root_name+'stat_UDP_dest_out_top10'+ '.txt'
fout4 = open(out_file, 'w')
for item in stat_UDP_dest_out_top10:
	print >> fout4, item[0]
	list_length = item[1][1]
	stat_sorted = stat_count(list_length)
	for ele in stat_sorted:
		print >> fout4, str(ele[0])+'\t'+str(ele[1])
fout4.close()
	
out_file = result_root_name+'stat_UDP_dest_in_top10'+ '.txt'
fout4 = open(out_file, 'w')
for item in stat_UDP_dest_in_top10:
	print >> fout4, item[0]
	list_length = item[1][1]
	stat_sorted = stat_count(list_length)
	for ele in stat_sorted:
		print >> fout4, str(ele[0])+'\t'+str(ele[1])
fout4.close()


	#	Task 5
out_file = result_root_name+'statistics_5_' + filename + '.txt'
fout5 = open(out_file, 'w')
print >> fout5, str(len(stat_length_TCP))
print >> fout5, str(stat_TCP_NS)
print >> fout5, str(stat_TCP_CWR)
print >> fout5, str(stat_TCP_ECE)
print >> fout5, str(stat_TCP_URG)
print >> fout5, str(stat_TCP_ACK)
print >> fout5, str(stat_TCP_PSH)
print >> fout5, str(stat_TCP_RST)
print >> fout5, str(stat_TCP_SYN)
print >> fout5, str(stat_TCP_FIN)
fout5.close()

