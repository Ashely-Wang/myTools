from scapy.all import *

def udp_port_scan(target, min_port, max_port):
    pkt = IP(dst = target)/UDP(dport = (int(min_port), int(max_port)))
    try:
        ret = sr(pkt)
        result = ret[0].res
        for i in range(0, len(ret)):
            if result[i][1].haslayer(ICMP):
                print("the port", result[i][1][3].fields["dport"], "is on")

    except:
        print("there is something wrong!!!")




                
