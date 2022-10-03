while True:
    l=0
    ip={"192.165.0.32":"00_A4_00_40_8E_FS","192.168.0.37":"00_16_17_31_8e_21","192.168.0.26":"00_16_13_31_8E_F7","132.142.3.36":"00_16_12_31_8E_08"}
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
