
import ifcfg
print("1 - ipv4 address")
print("2 - ipv6 address")
print("3 - MAC address")
invoer = input("kies een optie")

try:
   val = int(invoer)
   print("Input is an integer number. Number = ", val)
except ValueError:
    print("OOF! dat is geen nummer")


if (val) == 1:
    for name, interface in ifcfg.interfaces().items():
        print(interface['device'])
        print(interface['inet4'])
elif (val) == 2:
    for name, interface in ifcfg.interfaces().items():
        print(interface['device'])
        print(interface['inet6'])
elif (val) == 3:
    for name, interface in ifcfg.interfaces().items():
        print(interface['device'])
        print(interface['ether'])
else:
    print("geen geldige waarde ingevoerd")

