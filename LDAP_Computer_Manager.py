from tkinter import *
import ldap

root = Tk()
root.title("LDAP Computer Manager")

##root.iconbitmap(r'/') Setzen des Fenster Icons mit ICO Bitmap

def crVLAN():
    ip = var1.get()
    if ip == '192.168.0.0':
        var0 = "ADMIN"
    
    return var0

def fillin():
    
    vlan = crVLAN()
   
    macnocomma = inputmac.get()
    macnocomma = macnocomma.replace('-', '')

    macdoppelp = inputmac.get()
    macdoppelp = macdoppelp.replace('-', ':')

    hostname = inputhst.get()
    hostname = hostname.upper()

    f = open("Import."+ hostname +"."+ var1.get() +"." + vlan +".ldif","w+")
    f.write("\ndn: cn="+ hostname + ",cn="+ inputfunc.get() + ",cn="+ var1.get()+ ",cn=SUBNET,cn=DHCP Config,dc=firma,dc=de\n")
    f.write("objectClass: radiusprofile\nbjectClass: dhcpHost\nobjectClass: top\ncn: "+ hostname)
    f.write("\ncn: "+ inputmac.get() + "\ncn: "+ macnocomma + "\ndhcpHWAddress: ethernet "+ macdoppelp)
    f.write("\ndhcpStatements: fixed-address "+ inputip.get()+ "\nradiusCallingStationId: "+ inputmac.get()+ "\nradiusProfileDn: cn="+ vlan + ",ou=VLAN,ou=profiles,ou=radius,dc=firma,dc=de\n")
    f.write("radiusReplyMessage: Hello "+ hostname + "\n\n")
    f.close()
    done = Label(root, text="Config created").grid(row=5, column=1)

hst = Label(root, text= "Enter the hostname:").grid(row=1, column=0)
inputhst = Entry(root, width=30)
inputhst.grid(row=3, column= 0)

mac = Label(root, text="MAC-Adresse:").grid(row=4, column=0)
inputmac = Entry(root, width=30)
inputmac.grid(row=5, column=0)

##inputmac.insert(END, 'XX-XX-XX-XX-XX-XX')

ip = Label(root, text="IP-Adresse:").grid(row=6, column=0)
inputip = Entry(root, width=30)
inputip.grid(row=7, column=0)

usrfunc = Label(root, text="Rubrik/Funktionsgruppe:").grid(row=8, column=0)
inputfunc = Entry(root, width=30)
inputfunc.grid(row=9, column=0)



##var0 = StringVar(root)
##vlanvar = { 'INTRA','WKS','ADMIN','INET','PROD','GAST'}
##var0.set('INTRA')
##VLANMENU = OptionMenu(root, var0, *vlanvar).grid(row=13, column=1)
##VLAN = Label(root, text="VLAN:").grid(row=12, column=1)


var1 = StringVar(root)
subvar = { '192.168.0.0', '192.168.5.0'}
var1.set('192.168.0.0')

SUBMENU = OptionMenu(root, var1, *subvar).grid(row=13, column=0)

SUB = Label(root, text="Subnet:").grid(row=12, column=0)


dspsub = Label(root, text = crVLAN()).grid(row=13, column=1)

e1 = Button(root, text="OK!", command=fillin)
e1.grid(row=3, column= 1)



root.mainloop()



## Missing: Zsmlegen von IP und VLANs, EXE Conversion
