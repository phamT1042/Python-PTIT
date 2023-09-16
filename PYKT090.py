f = open("CONTACT.in", "r")

list_email = set()
for i in f:
    list_email.add(i.rstrip('\n').lower())
list_email = sorted(list_email)
for i in list_email: print(i)
