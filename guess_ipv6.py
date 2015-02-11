#!/usr/bin/env python

ip4 = "82.226.61.252".split(".")
ip6 = []
index = 1

for _ in "2a010e3"+"".join(hex(int(i))[2:] for i in ip4):
    ip6.append(_)
    if index % 4 == 0:
        ip6.append(':')
    index += 1

print ''.join(ip6)+"/64"
print "^"*18 + " " + "^"*18
print "\tnetwork\t\thost"
