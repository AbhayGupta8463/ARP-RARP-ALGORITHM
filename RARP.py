IP_ADD={"192.68.0.1":0, "192.68.0.2":0, "192.68.0.3":0, "192.68.0.4":0,"192.68.0.5":0,"192.68.0.6":0, "192.68.0.7":0, "192.68.0.8":0, "192.68.0.9":0,"192.68.0.10":0}
context="c"
while(context=="C" or context=="c"):
    mac_address=input("Enter MAC address: ")
    for key in IP_ADD:
        if IP_ADD[key]==0:
            IP_ADD[key]=mac_address
            print(key, "is alloted to the ",mac_address)
            break
    else:
        print("No IP Address REMAINING")
    cont=input("If you want to continue press c or c : ")
