#!/usr/bin/env python

__author__ = 'Will Dennis'
__email__ = 'willard.dennis@gmail.com'

# A script written to help me learn EIGRP's (default) DUAL calc and Python at the same time!
# I'm sure the code below sucks (pls help make it better!) but it works...

print "This script will calculate the metric of an EIGRP path using the default EIGRP K-val weights."
print "(i.e. K1=1, K2=0, K3=1, K4=0, K5=0)"
print

try:
    numlinks = int(raw_input("How many links are in the path? "))
except ValueError:
    # not an integer
    print "Bzzzzt! Next time enter a (whole) number!"
    exit()

print
print "Now go look at each interface in the path, and figure out the minimum bandwidth (look at BW value in 'sh int' output)"
try:
    minbw = int(raw_input("What is the minimum bandwidth link value of the path in Kbps? "))
except ValueError:
    # not an integer
    print "Bzzzzt! Next time enter a (whole) number!"
    exit()

print
print "Now we need to add up the delay values of all the links... Please list the delay value of each link (look at DLY value in 'sh int' output)"
dictlinkdly = {}
for i in range(1, (numlinks + 1)):
    try:
        temp = int(raw_input("What is the delay value of link %d in usec? " % i))
        temp = temp / 10
        dictlinkdly["delay{0}".format(i)] = temp
    except ValueError:
        # not an integer
        print "Bzzzzt! Next time enter a (whole) number!"
        exit()
delaysum = sum(dictlinkdly.itervalues())
print
print "OK, the sum of all the delay values (in 10's of usec) is: %d" % delaysum

bwscaler = ((10**7) * 256)
leftaddend = (bwscaler / minbw)
rightaddend = (delaysum * 256)
metric = (bwscaler / minbw) + (delaysum * 256)

print
print "Now then: we'll now calculate the metric using the following (simplified) default EIGRP metric formula:"
print "((( 10**7 ) * 256) / <path_minbw> ) + ( <sum_of_delays_in_10s_of_usec> * 256 ) = metric"
print "...therefore, in this case..."
print "( %d / %d ) + ( %d * 256 ) = metric" % (bwscaler, minbw, delaysum)
print "%d + %d = metric" % (leftaddend, rightaddend)
print "***********************************"
print "Your metric should then be: %d" % metric
print "***********************************"


