from scapy.all import *


def tcp_port_scan(target, min_port, max_port):
    pkt = IP(dst = target)/TCP(flags = "S", dport = (int(min_port), int(max_port)))
    try:
        ret = sr(pkt)
        rl = ret[0].res
        for i in range(0, len(rl)):
            if rl[i][1].haslayer(TCP):
                if rl[i][1].getlayer(TCP).fields["seq"]:
                    print("the port", rl[i][1].getlayer(TCP).fields["sport"], "is open for connection")




## min_port -> max_port (the range of port for scan)      
    
