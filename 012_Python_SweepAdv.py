import commands,re,socket,os,smtplib
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
i = 0
host_up = []
for ip in IPNetwork(direccion[0] + "/" + str(direccion[1])):
 response = os.system("ping -c 1 -w2 " + str(ip) + " >/dev/null 2>&1")
 if response == 0:
  print ip, 'is up!'
  i = i + 1
  host_up.append(str(ip))
 else:
  print ip, 'is down!'

#envio del correo
fromaddr = 'your_user@gmail.com'
toaddrs  = 'dest@gmail.com'
msg = 'Los siguientes nodos (' + str(i) + ') estan up:\n'

for idx, val in enumerate(host_up):
 msg += str(val) + '\n'

# Credentials (if needed)
username = 'your_user@gmail.com'
password = 'yourpass'
# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
