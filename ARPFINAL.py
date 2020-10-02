rarp = {"192.68.0.1":0,
       "192.68.0.2":0,
       "192.68.0.3":0,
       "192.68.0.4":0,
       "192.68.0.5":0,
       "192.68.0.6":0,
       "192.68.0.8":0,
       "192.68.0.9":0,
       "192.68.0.10":0,
       "192.68.0.11":0}

arp = {"192.68.0.1":"00:0a:95:9d:68:16",
       "192.68.0.2":"00:0a:95:9d:68:17",
       "192.68.0.3":"00:0a:95:9d:68:18",
       "192.68.0.4":"00:0a:95:9d:68:19",
       "192.68.0.5":"00:0a:95:9d:68:20"}
i=0
choice="k"
while(choice.upper()!="E"):
    choice = input("enter \nA for ARP search \nR for RARP insert\nE to exit\n")
    if choice.upper() == "A":
        tempIP = input("enter ip add to search ")
        if tempIP in arp:
            print("ip found, mac add: ", arp[tempIP])
        else:
            print("not found")

    elif choice.upper() == "R":
        tempMA = input("enter mac add to be added ")
        for key in rarp:
            if rarp[key]==0:
                rarp[key]=tempMA
                print(key, "is alloted to the ",tempMA)
                break
        else:
            print("No IP Address REMAINING")

    elif choice.upper() == "E":
        print("bye")

    else:
        print("invalid")
