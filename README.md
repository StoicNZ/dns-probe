# dns-probe
DNSDB Lookup and Resolver Python Script

This script will look up a given domain name on DNSDB and then check for subdomains that are still alive. There will be some junk ones and some will be out-of-scope for your project (check is only if the domain is in the DNS, not that it belongs to the domain passed in) if you can only look at DNS's under parent domain.

##File Generated:

<domain>.live.dns: This file has a list of all DNS that resolve and can be passed into nmap using the -iL param.
<domain>.unique.dns: This is a file of unique past and present DNS, some will not be active
<domain>.dns.ip.csv: This is a CSV file of DNS and resolved IP
