from tkinter import *
import ldap

root = Tk()
root.title("LDAP Computer Manager")

##root.iconbitmap(r'/') Setzen des Fenster Icons mit ICO Bitmap

def crVLAN():
    ip = var1.get()
    if ip == '':
    var0 = ""
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

ip = Label(root, text="IP-Adresse:").grid(row=6, column=0)
inputip = Entry(root, width=30)
inputip.grid(row=7, column=0)

usrfunc = Label(root, text="Rubrik/Funktionsgruppe:").grid(row=8, column=0)
inputfunc = Entry(root, width=30)
inputfunc.grid(row=9, column=0)


var1 = StringVar(root)
subvar = { ''}

SUBMENU = OptionMenu(root, var1, *subvar).grid(row=13, column=0)

SUB = Label(root, text="Subnet:").grid(row=12, column=0)

def update_dsp():
    newtext = tk.textvariable()
    newtext.set(crVLAN())
    dspsub = Label(root, textvariable = newtext).grid(row=13, column=1)
    dspsub.label.after(1000, update_dsp)

update_dsp()

e1 = Button(root, text="OK!", command=fillin)
e1.grid(row=3, column= 1)



root.mainloop()


##https://medium.com/@alpolishchuk/a-little-python-ldap-tutorial-4a6a79676157
##https://www.youtube.com/watch?v=YXPyB4XeYLA

## Missing: Zsmlegen von IP und VLANs, EXE Conversion
