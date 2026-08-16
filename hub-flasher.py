import urllib.request
import os
directory = os.path.dirname(os.path.abspath(__file__))

print(directory)
os.putenv('COMSPEC', r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe')
hitdown = [['https://github.com/pybricks/pybricks-micropython/releases/download/v4.0.1/pybricks-cityhub-v4.0.1.zip',"cityhub.zip"],     
['https://github.com/pybricks/pybricks-micropython/releases/download/v4.0.1/pybricks-essentialhub-v4.0.1.zip', "essentialhub.zip"],
['https://github.com/pybricks/pybricks-micropython/releases/download/v4.0.1/pybricks-ev3-v4.0.1.zip',"ev3.zip"],
['https://github.com/pybricks/pybricks-micropython/releases/download/v4.0.1/pybricks-movehub-v4.0.1.zip',"boosthub.zip"],
['https://github.com/pybricks/pybricks-micropython/releases/download/v4.0.1/pybricks-nxt-v4.0.1.zip', "nxthub.zip"],
['https://github.com/pybricks/pybricks-micropython/releases/download/v4.0.1/pybricks-primehub-v4.0.1.zip',"primehub.zip"],
['https://github.com/pybricks/pybricks-micropython/releases/download/v4.0.1/pybricks-technichub-v4.0.1.zip',"technichub.zip"]]


def downget():
    for i in range(len(hitdown)):



        output = os.path.join(directory, hitdown[i][1])

        urllib.request.urlretrieve(hitdown[i][0], output)


def install():
    os.system("pip install pybricks pybricksdev customtkinter bleak")
    downget()

def update():
    #os.system("git pull")
    os.system("pip install -U pybricks pybricksdev customtkinter bleak")

#install()
#update()
import pybricks
import pybricksdev
import customtkinter as ctk
import customtkinter as cutsomtkinter
import bleak



def insrun(type):
    path = os.path.join( "'"+ directory , f"{type}" + "'")
    run = ("pybricksdev flash path " + path)
    os.system(f"pybricksdev flash {path}")
    os.kill(os.getpid(),9)


def prep():
    # Create the new top-level window
    boost = ctk.CTkToplevel(app)
    boost.geometry("1000x400")
    boost.title("installation window")
    
    # Ensure the new window stays on top of the main window
    boost.after(100, lambda: boost.focus_force())
    
    # Add widgets inside the new window
    label = ctk.CTkLabel(boost, text="boost hub fw install window!")
    label.pack(pady=20)

    guide = ctk.CTkTextbox(boost, width=900, height=150)
    guide.pack(padx= 50, pady=5)
    instructions = (
        "1. For hubs with a USB port: press and hold the Bluetooth button and then "
        "connect the hub to the computer.\n\n"
        "2. For port-less hubs, you may skip these steps but before pressing install \n\n" 
        "you must press and hold the main button until it turns purple"
        "3. Press Win + X and select 'Device Manager'.\n\n"
        "⚠ If you get a warning saying that you aren't an administrator, "
        "please sign in with an administrator account.\n\n"
        "4. Find your hub under 'Ports (COM & LPT)'.\n\n"
        "5. Right-click it and select 'Properties' > 'Driver' > 'Update Driver'.\n\n"
        "6. Select 'Browse my computer for drivers' (or 'Search manually').\n\n"
        "7. Select 'Let me pick from a list of available drivers on my computer'.\n\n"
        "8. Select 'Universal Serial Bus devices' and click 'Next'.\n\n"
        "9. Select 'WinUSB Device' under Manufacturer and again under Model.\n\n"
        "10. Click 'Next' and accept the warning. You will then be able to "
        "continue using this tool.\n\n"

        "12. Find the hub in Device Manager. It should now be in DFU mode.\n\n"
    )

    guide.insert("1.0", instructions)
    next = ctk.CTkButton(boost, text="next")
    next.pack(padx = 50, pady = 5)


app = ctk.CTk()
app.geometry("400x400")

banner = ctk.CTkLabel(app,text="please select you hub")
cityhub = ctk.CTkButton(app,text="city hub")
essentialhub = ctk.CTkButton(app,text="essential hub")
ev3hub = ctk.CTkButton(app,text="ev3 hub")
boosthub = ctk.CTkButton(app,text="boost hub",command=lambda:insrun("boosthub.zip"))
nxthub = ctk.CTkButton(app,text="nxt hub")
primehub = ctk.CTkButton(app,text="prime hub", command=lambda:insrun("primehub.zip"))
technichub = ctk.CTkButton(app,text="technic hub")
ins = ctk.CTkButton(app,text="before install", command=prep)

banner.pack(padx = 50)
cityhub.pack(padx = 50,pady = 5)
essentialhub.pack(padx = 50,pady = 5)
ev3hub.pack(padx = 50,pady = 5)
boosthub.pack(padx = 50,pady = 5)
nxthub.pack(padx = 50,pady = 5)
primehub.pack(padx = 50,pady = 5)
technichub.pack(padx = 50,pady = 5)
ins.pack(padx=  50, pady=5)
app.mainloop()


