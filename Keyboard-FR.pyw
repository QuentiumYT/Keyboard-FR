import os, sys, urllib.request
from tkinter import *
from tkinter.messagebox import *

__version__ = 2
__filename__ = "Keyboard-FR"
__basename__ = os.path.basename(sys.argv[0])
__savepath__ = os.path.join(os.environ['APPDATA'], "QuentiumPrograms")
__iconpath__ = __savepath__ + "/{}.ico".format(__filename__)

try:urllib.request.urlopen("https://www.google.fr/", timeout=1); connection = True
except:connection = False
if not os.path.exists(__iconpath__):
    try:os.mkdir(__savepath__)
    except:pass
    if connection == True:
        try:urllib.request.urlretrieve("https://quentium.fr/+++PythonDL/{}.ico".format(__filename__), __iconpath__)
        except:pass

if connection == True:
    try:script_version = int(urllib.request.urlopen("https://quentium.fr/programs/index.php").read().decode().split(__filename__ + "<!-- Version: ")[1].split(" --></h2>")[0])
    except:script_version = __version__
    if script_version > __version__:
        if os.path.exists(__iconpath__):popup = Tk(); popup.attributes("-topmost", 1); popup.iconbitmap(__iconpath__); popup.withdraw()
        ask_update = askquestion(__filename__ + " V" + str(script_version), "Une mise à jour à été trouvée, souhaitez vous la télécharger puis l'éxécuter ?", icon="question")
        if ask_update == "yes":
            try:os.rename(__basename__, __filename__ + "-old.exe")
            except:os.remove(__filename__ + "-old.exe"); os.rename(__basename__, __filename__ + "-old.exe")
            if "-32" in str(__basename__):urllib.request.urlretrieve("https://quentium.fr/download.php?file={}-32.exe".format(__filename__), __filename__ + ".exe")
            else:urllib.request.urlretrieve("https://quentium.fr/download.php?file={}.exe".format(__filename__), __filename__ + ".exe")
            showwarning(__filename__, "Le programme va redémarrer pour fonctionner sous la nouvelle version.", icon="warning")
            os.system("start " + __filename__ + ".exe"); os._exit(1)

__filename__ = __filename__ + " V" + str(__version__)

majuscule = True
verr_maj_true = "Verr.Maj ► Activé !"
verr_maj_false = "Verr.Maj ► Désactivé !"

keys =[ 
[
    [
        ("Touches de Fonction"),
        ({"side":"top","expand":"yes","fill":"both"}),
        [
            ("Ech","nothing", "F1", "F2","F3","F4","nothing","F5","F6","F7","F8","nothing","F9","F10","F11","F12")
        ]
    ],

    [
        ("Touches de Caractère"),
        ({"side":"top","expand":"yes","fill":"both"}),
        [
            ("²","1\n&","2\né",'3\n"',"4\n'","5\n(","6\n-","7\nè","8\n_","9\nç","0\nà","°\n)","+\n=","Retour"),
            ("Tab","A","Z","E","R","T","Y","U","I","O","P","¨\n^","£\n$","Entrée"),
            ("Verr.Maj","Q","S","D","F","G","H","J","K","L","M","%\nù","µ" + "\n*","Entrée"),
            ("Maj",">\n<","W","X","C","V","B","N","?\n,",".\n;","/\n:","§\n!","Maj"),
            ("Ctrl", "©","Alt","Espace","Alt","©","▓","Ctrl")
        ]
    ]
],

[
    [
        ("Touches de Système"),
        ({"side":"top","expand":"yes","fill":"both"}),
        [
            (
            "Imp écr\nSyst",
            "Verr.\ndéf",
            "Pause\nAttn"
            )
        ]
    ],

    [
        ("Touches d'édition"),
        ({"side":"top","expand":"yes","fill":"both"}),
        [
            (
            "Inser",
            "Orig",
            "Pg.Préc"
            ),
            (
            "Suppr",
            "Fin",
            "Pg.Suiv"
            ),
        ]
    ],

    [
        ("Touches de Navigation"),
        ({"side":"top","expand":"yes","fill":"both"}),
        [
            (
            "↑",
            ),
            ( "←",
            "↓",
            "→"
            ),
        ]
    ],

],

[
    [
        ("Touches Numériques"),
        ({"side":"top","expand":"yes","fill":"both"}),
        [
            ("Verr.\nNum","/","*","-"),
            ("7","8","9","+"),
            ("4","5","6","+"),
            ("1","2","3","Entrée"),
            ("0",".","Entrée")
        ]
    ],
]
]

class Keyboard(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        global verr_maj
        verr_maj = StringVar()
        verr_maj.set(verr_maj_true)
        Entry(self, textvariable=verr_maj, width=17, state="disabled", font="impact 15").pack()
        self.create_frames_and_buttons()
    def create_frames_and_buttons(self):
        for key_section in keys:
            store_section = Frame(self)
            store_section.pack(side="left", expand="yes", fill="both", padx=10, pady=10, ipadx=10, ipady=10)
            for layer_name, layer_properties, layer_keys in key_section:
                store_layer = LabelFrame((store_section), text=layer_name)
                store_layer.pack(layer_properties)
                for key_bunch in layer_keys:
                    store_key_frame = Frame(store_layer)
                    store_key_frame.pack(side="top",expand="yes",fill="both")
                    for k in key_bunch:
                        if len(k)<=3:
                            store_button = Button(store_key_frame, text=k, width=6, height=2)
                        else:
                            store_button = Button(store_key_frame, text=k.center(5," "), width=6, height=2)
                        def simple_button(background, forground, command):
                            store_button["relief"]="groove"
                            store_button["bg"]=background
                            store_button["fg"]=forground
                            store_button["command"]=command
                            store_button.pack(side="left",fill="both",expand="yes")
                        if "nothing" in k:
                            store_button["state"]="disabled"
                            store_button["text"]=""
                        if k == "Espace":
                            store_button["width"]=53
                            simple_button("white", "red", lambda q=k: self.button_command(" "))
                        elif k == "Entrée":
                            simple_button("white", "red", lambda q=k: self.button_command("\n"))
                        elif k == "Retour":
                            simple_button("white", "red", lambda q=k: self.button_command_del())
                        elif k == "Tab":
                            simple_button("white", "red", lambda q=k: self.button_command("\t"))
                        elif k == "Verr.Maj":
                            simple_button("white", "red", lambda q=k: self.button_command_maj())
                        elif k == "Ech":
                            simple_button("white", "red", lambda q=k: os._exit(1))
                        elif k in ["Maj", "Ctrl", "Alt", "©", "▓", "Fin", "Inser", "Suppr", "Orig", "Pg.Préc", "Pg.Suiv", "Imp écr\nSyst", "Verr.\ndéf", "Pause\nAttn", "Verr.\nNum"]:
                            simple_button("lightgray", "red",  None)
                        elif k == " µ \n*":
                            simple_button("white", "blue", lambda q=k: self.button_command(q))
                        elif k == "0":
                            store_button["width"]=14
                            simple_button("white", "blue", lambda q=k: self.button_command(q))
                        else:
                            simple_button("white", "blue", lambda q=k: self.button_command(q))
        return

    def button_command(self, event):
        char = event
        if majuscule == True:
            if len(char) >= 3:
                if char == "F10":
                    txtBox.insert(INSERT, char)
                elif char == "F11":
                    txtBox.insert(INSERT, char)
                elif char == "F12":
                    txtBox.insert(INSERT, char)
                else:
                    fir = char[:1]
                    txtBox.insert(INSERT, fir)
            else:
                txtBox.insert(INSERT, char)
            return
        else:
            if len(char) >= 3:
                if char == "F10":
                    txtBox.insert(INSERT, char.lower())
                elif char == "F11":
                    txtBox.insert(INSERT, char.lower())
                elif char == "F12":
                    txtBox.insert(INSERT, char.lower())
                else:
                    fir = char[-1:]
                    txtBox.insert(INSERT, fir.lower())
            else:
                txtBox.insert(INSERT, char.lower())
            return

    def button_command_del(self):
        try:
            var = txtBox.get("1.0", END)
            liste = list(str(var))
            liste.pop()
            liste.pop()
            txtBox.delete("1.0", END)
            var = "".join(liste)
            txtBox.insert(INSERT, var)
            return
        except:
            showwarning("Clavier Virtuel Français V" + str(__version__), "Il n'y a plus de caractères à supprimer !")

    def button_command_maj(self):
        if majuscule == True:
            def replace_false():
                global majuscule
                majuscule = False
            replace_false()
            verr_maj.set(verr_maj_false)
        else:
            def replace_true():
                global majuscule
                majuscule = True
            replace_true()
            verr_maj.set(verr_maj_true)

keyboard = Tk()
width = 1330
height = 650
keyboard.update_idletasks()
x = (keyboard.winfo_screenwidth() - width) // 2
y = (keyboard.winfo_screenheight() - height) // 2
keyboard.geometry("{}x{}+{}+{}".format(width , height, int(x), int(y)))
keyboard.title("Clavier Virtuel Français V" + str(__version__))
if os.path.exists(__iconpath__):
    keyboard.iconbitmap(__iconpath__)
canvas = Canvas(keyboard, background="white")
canvas.pack()
txtBox = Text(canvas, width = 118, height = 12, wrap = WORD, font="impact 15")
txtBox.grid(row = 0, column = 0, sticky = W)
txtBox.pack()
Keyboard(keyboard).pack()
keyboard.mainloop()
