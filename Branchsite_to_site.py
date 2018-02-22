import json
from pyntc import ntc_device as NTC
site2 = NTC(host='102.1.1.100', username='Branch', password='shiva', device_type='cisco_ios_ssh')
site2.open()
site2_output = site2.facts
print (json.dumps(site2_output, indent=4))
site2.config_list(['crypto isakmp policy 1',
                   'authentication pre-share',
                   'encryption aes',
                   'hash sha',
                   'group 5',
                   'lifetime 1800',
                   'exit',
                   'crypto isakmp key shiva address 101.1.1.100',
                   'crypto ipsec transform-set t-set esp-aes esp-sha-hmac',
                   'mode tunnel',
                   'exit',
                   'crypto ipsec security-association lifetime seconds 1800',
                   'access-list 101 permit ip 192.168.102.0 0.0.0.255 192.168.122.0 0.0.0.255', 
                   'crypto map test 10 ipsec-isakmp',
                   'set transform-set t-set',
                   'set peer 101.1.1.100',
                   'match address 101',
                   'int g0/0',
                   'crypto map test',
                   'ip access-list extended natacl',
                   '1 deny ip 192.168.102.0 0.0.0.255 192.168.122.0 0.0.0.255',
                   'exit'])
site2.close()
