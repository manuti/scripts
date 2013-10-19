import commands,re,socket,os

#A generator that returns stripped lines of output from "ip address show"
iplines=(line.strip() for line in commands.getoutput("ip address show").split('\n'))
#Turn that into a list of IPv4 and IPv6 address/mask strings
addresses1=reduce(lambda a,v:a+v,(re.findall(r"inet ([\d.]+/\d+)",line)+re.findall(r"inet6 ([\:\da-f]+/\d+)",line) for line in iplines))
#addresses1 now looks like ['127.0.0.1/8', '::1/128', '10.160.114.60/23', 'fe80::1031:3fff:fe00:6dce/64']
#Get a list of IPv4 addresses as (IPstring,subnetsize) tuples
ipv4s=[(ip,int(subnet)) for ip,subnet in (addr.split('/') for addr in addresses1 if '.' in addr)]
#ipv4s now looks like [('127.0.0.1', 8), ('10.160.114.60', 23)]
#Get IPv6 addresses
ipv6s=[(ip,int(subnet)) for ip,subnet in (addr.split('/') for addr in addresses1 if ':' in addr)]

#print our address
direccion = ipv4s[1]
print "RPi address:"
print direccion

#we have ip and mask, build an array with network IP
from netaddr import IPNetwork
for ip in IPNetwork(direccion[0] + "/" + str(direccion[1])):
 response = os.system("ping -c 1 -w2 " + str(ip) + " >/dev/null 2>&1")
 if response == 0:
  print ip, 'is up!'
 else:
  print ip, 'is down!'

#ref:http://stackoverflow.com/questions/2953462/pinging-servers-in-python
#ref:http://stackoverflow.com/questions/1942160/python-3-create-a-list-of-possible-ip-addresses-from-a-cidr-notation/1942178
#ref:http://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib/5111878
