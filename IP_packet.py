#	IP_packet
def convert_IP(list_IP):
	if len(list_IP) != 4:
		print 'convert_IP ERROR !'
	else:
		dec_addr = []
		for item in list_IP:
			dec_addr += [str(int(item, 16))]
		return '.'.join(dec_addr)
		
class IP_packet:
    def __init__(self):
		self.num = 0
		self.link_destination_mac = ''
		self.link_source_mac = ''
		self.link_protocol_type = ''
		self.net_version = ''
		self.net_IHL = 0
		self.net_total_length = 0
		self.net_identification = 0
		self.net_DF = False
		self.net_MF = False
		self.net_fragment_offset = 0
		self.net_TTL = 0
		self.net_protocol = 0
		self.net_destination_IP = ''
		self.net_source_IP = ''
		self.tf_destination_port = 0
		self.tf_source_port = 0
    def __init__(self, hex_data, number):
		self.num = number
		self.link_destination_mac = '-'.join(hex_data[0:6])
		self.link_source_mac = '-'.join(hex_data[6:12])
		self.link_protocol_type = ''.join(hex_data[12:14])
		self.net_version = 'IPv' + str(int(hex_data[14][0], 16))
		self.net_IHL = int(hex_data[14][1], 16)
		self.net_total_length = int(''.join(hex_data[16:18]), 16)
		self.net_identification = int(''.join(hex_data[18:20]), 16)
		self.net_DF = int(hex_data[20][0], 16) & (1 << 2) != 0
		self.net_MF = int(hex_data[20][0], 16) & (1 << 1) != 0
		self.net_fragment_offset = int(bin(int(hex_data[20][0], 16))[-1] + \
									bin(int(hex_data[20][1]+hex_data[21], 16))[2::], 2)
		self.net_TTL = int(hex_data[22], 16)
		self.net_protocol = int(hex_data[23], 16)
		self.net_source_IP = convert_IP(hex_data[26:30])
		self.net_destination_IP = convert_IP(hex_data[30:34])
		self.tf_source_port = int(''.join(hex_data[34:36]), 16)
		self.tf_destination_port = int(''.join(hex_data[36:38]), 16)
		
		if self.net_protocol == 6:
			self.tf_TCP_header_length = int(hex_data[46][0], 16)
			self.tf_TCP_NS = int(hex_data[46][1], 16) & 1 != 0
			status_bits = int(hex_data[47], 16)
			self.tf_TCP_CWR = status_bits & (1 << 7) != 0
			self.tf_TCP_ECE = status_bits & (1 << 6) != 0
			self.tf_TCP_URG = status_bits & (1 << 5) != 0
			self.tf_TCP_ACK = status_bits & (1 << 4) != 0
			self.tf_TCP_PSH = status_bits & (1 << 3) != 0
			self.tf_TCP_RST = status_bits & (1 << 2) != 0
			self.tf_TCP_SYN = status_bits & (1 << 1) != 0
			self.tf_TCP_FIN = status_bits & (1 << 0) != 0
			self.tf_TCP_window_size = int(hex_data[48]+hex_data[49], 16)
		if self.net_protocol == 17:
			self.tf_UDP_length = int(hex_data[38]+hex_data[39], 16)
		
    def output(self):
		print self.num
		print self.link_destination_mac
		print self.link_source_mac
		print 'link_protocol_type', self.link_protocol_type
		print self.net_version
		print self.net_IHL
		print self.net_total_length
		print 'net_identification', self.net_identification
		print 'net_DF', self.net_DF
		print 'net_MF', self.net_MF
		print 'net_fragment_offset', self.net_fragment_offset
		print 'net_TTL', self.net_TTL
		print 'net_protocol', self.net_protocol
		print self.net_destination_IP
		print self.net_source_IP
		print self.tf_destination_port
		print self.tf_source_port
		
		if self.net_protocol == 6:
			print 'tf_TCP_header_length', self.tf_TCP_header_length
			print 'tf_TCP_NS', self.tf_TCP_NS
			print 'tf_TCP_CWR', self.tf_TCP_CWR
			print 'tf_TCP_ECE', self.tf_TCP_ECE
			print 'tf_TCP_URG', self.tf_TCP_URG
			print 'tf_TCP_ACK', self.tf_TCP_ACK
			print 'tf_TCP_PSH', self.tf_TCP_PSH
			print 'tf_TCP_RST', self.tf_TCP_RST
			print 'tf_TCP_SYN', self.tf_TCP_SYN
			print 'tf_TCP_FIN', self.tf_TCP_FIN
			print 'tf_TCP_window_size', self.tf_TCP_window_size
		if self.net_protocol == 17:
			print 'tf_UDP_length', self.tf_UDP_length
