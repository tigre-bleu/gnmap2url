#!/usr/bin/env python3
import sys
import argparse

parser = argparse.ArgumentParser(description='Generates a list of URL from a gnmap output from NMAP. \
        Example: gnmap2url.py --protocol http,https file.gnmap')
parser.add_argument('file', help='NMAP .gnmap input file', nargs=1)
parser.add_argument('-p', '--protocol', type=str, action='append', help='Protocols to include in the results. Default is \"--protocol http --protocol  https\"')

args = parser.parse_args()

gnmap = args.file[0]
if args.protocol == None:
    args.protocol=['http', 'https']
target_protocols = args.protocol

f = open(gnmap, 'r')

urls = []

for line in f.readlines():
    #print(line)

    split = line.split("Ports:")
    if len(split) == 2:

        (host_str, ports_str) = line.split("Ports:")
        host_str = host_str.rstrip()
        hosts = []
    
        split = host_str.split()
    
        # IP
        hosts.append(split[1])
    
        # Hostname
        if len(split) > 1 and split[2] != "()":
            hosts.append(split[2][1:-1])
    
        for host in hosts:
    
            # Ports
            split = ports_str.split()
            for port_str in split:
                split = port_str.split("/")
    
                if len(split) > 3:
    
                    if split[1] == "open" and split[4] in target_protocols: 
                        port = split[0]
        
                        # Protocol
                        for prefix in ['http://', 'https://']:
                            url = prefix + host + ":" + port
                            if url not in urls:
                                urls.append(url)
                                print(url)
