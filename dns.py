import socket
import requests
import sys
import os.path

if (len(sys.argv) < 2):
	sys.exit('No domain passed in..')

api-key = 'API KEY GOES HERE'
domain = sys.argv[-1]

#Don't run if already created files for this domain
if '-skip' not in sys.argv:
	if os.path.isfile(domain + '.unique.dns'):
		sys.exit(domain + '.unique.dns already exists')
	if os.path.isfile(domain + '.live.dns'):
		sys.exit(domain + '.live.dns already exists')
	if os.path.isfile(domain + '.dns.ip.csv'):
		sys.exit(domain + '.dns.ip.csv already exists')

	request = requests.get('https://api.dnsdb.info/lookup/rrset/name/*.' + domain, headers={'X-API-Key': api-key})
	domains = []
	
	#Parse and save DNS we find to <domain>.unique.dns file
	dnsFile = open(domain + '.unique.dns', 'w')
	for line in request.text.replace(' ', '\n').split('\n'):
		if str(line).endswith('.'):
			line = str(line[0:-1])
		if domain in str(line) and str(line) not in domains:
			domains.append(str(line))
			dnsFile.write(str(line) + '\n')
	dnsFile.close()
	print str(len(domains)) + ' unique DNS addresses found, now let\'s find the live ones..'

#Resolve DNS and save to CSV with IP and nmap parsable TXT
numberOfLiveDns = 0
csvFile = open(domain + '.dns.ip.csv', 'w')
liveDns = open(domain + '.live.dns', 'w') #This one is the one you can use with nmap -iL <path to file>
with open(domain + '.unique.dns', 'r') as f:
	for line in f:
		line = line.rstrip('\n')
		try:
			ip = socket.gethostbyname(line)
			csvFile.write(str(line) + ',' + str(ip) + '\n')
			liveDns.write(str(line) + '\n')
			numberOfLiveDns += 1
		except Exception:
			next

print str(numberOfLiveDns) + ' live DNS addresses found'
