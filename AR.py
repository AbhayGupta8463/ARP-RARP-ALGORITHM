while True:
    l=0
    ip={"192.168.0.64":"00_A8_00_40_8E_FS","192.168.0.60":"00_16_17_31_8e_22","192.168.0.68":"00_16_17_31_8E_F7","132.147.3.3":"00_16_17_31_8E_08"}
    ch=int(input("1.ARP\n2.EXIT\nEnter your choice"))
    if ch==1:
        s=input("ENTER IP ADDRESS")
        if s in ip.keys():
            print("MAC ADDRESS IS:-"+ip[s])
        else:
            print("INVALID IP ADDRESS")
    if ch==2:
        s=input("ENTER MAC ADDRESS")
        if l==len(ip):
            l=0
        print("IP ADDRESS ASSIGNED:-"+ip.values()[l])
        l+=1
    if ch==3:
        break
