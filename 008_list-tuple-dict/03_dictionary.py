# Like a map or hash table in other languages
captains = {}
captains["Enterprise"] = "Kirk"
captains["Enterprise D"] = "Picard"
captains["Deep Space Nine"] = "Sisko"
captains["Voyager"] = "Janeway"

print('captains["Voyager"]:', captains["Voyager"])

print('captains.get("Enterprise"):', captains.get("Enterprise"))
print('captains.get("NX-01":"):', captains.get("NX-01"))

print ('\nfor ship in capitans:')
for ship in captains:
    print(ship + ": " + captains[ship])