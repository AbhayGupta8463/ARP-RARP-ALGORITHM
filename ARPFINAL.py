rarp = {"192.68.0.1":0,
       "192.68.0.2":0,
       "192.68.0.3":0,
       "192.68.0.4":0,
       "192.68.0.5":0,
       "192.68.0.6":0,
       "192.68.0.8":0,
       "192.68.0.9":0,
       "192.68.0.10":0,
       "192.68.0.11":0,
       "192.68.0.12":0,
       "192.68.0.22":0,
       "192.68.0.32":0,
       "192.68.0.42":0,
       "192.68.0.52":0
       }

arp = {"192.68.0.1":"00:0a:95:9d:68:16",
       "192.68.0.2":"00:0a:95:9d:68:17",
       "192.68.0.3":"00:0a:95:9d:68:18",
       "192.68.0.4":"00:0a:95:9d:68:19",
       "192.68.0.5":"00:0a:95:9d:68:20",
       "192.68.0.6":"00:0a:95:9d:68:21",
       "192.68.0.7":"00:0a:95:9d:68:22",
       "192.68.0.8":"00:0a:95:9d:68:23",
       "192.68.0.9":"00:0a:95:9d:68:24",
       "192.68.0.10":"00:0a:95:9d:68:25",
       "192.68.0.52":"00:0a:95:9d:68:20",
       "192.68.0.62":"00:0a:95:9d:68:21",
       "192.68.0.72":"00:0a:95:9d:68:22",
       "192.68.0.82":"00:0a:95:9d:68:23",
      }
i=0
choice="k"
while(choice.upper()!="E"):
    choice = input("enter \nA for ARP search \nR for RARP insert\nE to exit\n") #TAKING CHOICES FROM USER
    if choice.upper() == "A":
        tempIP = input("enter ip add to search ") #TAKING IP ADDRESS AS INPUT
        if tempIP in arp:
            print("ip found, mac add: ", arp[tempIP]) #DISPLAYING CORRESPODING MAC ADDRESS
        else:
            print("not found")

    elif choice.upper() == "R":
        tempMA = input("enter mac add to be added ") #TAKING MAC ADDRESS AS INPUT
        for key in rarp:
            if rarp[key]==0:
                rarp[key]=tempMA
                print(key, "is alloted to the ",tempMA)  #DISPLAYING CORRESPODING IP ADDRESS
                break
        else:
            print("No IP Address REMAINING")

    elif choice.upper() == "E":
        print("bye")

    else:
        print("invalid")
