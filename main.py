import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import Canvas
from PIL import Image, ImageGrab



fen = Tk()
fen.title("Business card generator")
fen.geometry("1080x500")
fen.minsize(1080, 500)
fen.config(background="white")

#creation parametre image
height=400
width = 500
frameAcc = Frame(fen, bg="#a94220")
frameAcc.place(x=250, y=3)
imageAcc=PhotoImage(file="accIMG.png").zoom(5).subsample(10)

# creation dictionnaire couleur et caractere_police
carct = {"lbl": "Helvetica", "titre": "Verdana"}
color = {"terre": '#795548', "soleil": '#ffeb3b', "arbre":'#1b5e20', "herbe": '#8bc34a', "ciel":'#4fc3f7',
         "neutre":"white", "carte":"#232b2b", "carte1":"#3d2022"}

#creation liste longeur_btn_acc
btnLong = [14]

#creation image carte recto
widthVR = 80
heightVR = 80
imageRect = PhotoImage(file="accIMG.png").zoom(5).subsample(80)
imageRect2 =PhotoImage(file="logoel1.png").zoom(5).subsample(80)
imagePers = PhotoImage(file="DG_EL.png").zoom(5).subsample(40)
imagePers = PhotoImage(file="DG_EL.png").zoom(5).subsample(40)
#hauteur et largeur de la photo personne
heightPerso = 100
widthPerso = 100

#hauteur et largeur about us
imageAbs=PhotoImage(file="LOGO EL2.png").zoom(5).subsample(8)
widthAbts = 350
heightAbts = 350

class design():

    def __init__(self):
        pass

    def Acceuil(self):
        fen.config(background=color["neutre"])
        canAcc= Canvas(frameAcc, height=height, width=width, bg=color["neutre"], bd=0, highlightthickness=0)
        canAcc.create_image(width/2,height/2, image=imageAcc)
        canAcc.grid(row=0, column=0, sticky=W)

        lblAcc = Label(fen, text="BUSINESS CARD GENERATOR BEST CARD DESIGN",bg=color["neutre"],fg=color["herbe"], font=(carct["titre"], 15))
        lblAcc.place(x=250, y=390)

        accbtn = Button(fen,text="BEGIN NOW", bd=0, fg=color["terre"],bg=color["soleil"],  width=20, height=2,
                        font=(carct["titre"], 12), command=self.Princi)
        accbtn.place(x=390, y=440)



    def Princi(self):
        frameNav = Frame(fen, bg=color["herbe"], height=50, width=1080)
        frameNav.place(x=0, y=0)

        frameLat = Frame(fen, bg=color["arbre"], height=450, width=200)
        frameLat.place(x=0, y=50)

        self.frameCent = Frame(fen, bg=color["terre"], height=450, width=960)
        self.frameCent.place(x=120, y=50)

        # texte principale il doit etre la meme chose avec le frame home
        position_home = [5, 55, 105, 155, 205, 255, 305, 355]
        position_home_X = [20]

        bienvenu = Label(self.frameCent, text="BUSINESS CARD DESIGN", bg=color["terre"],fg=color["soleil"],
                         font=(carct["titre"], 30, "bold"))
        bienvenu.place(x= 150, y=position_home[1])

        p1 = Label(self.frameCent, text="A business card is an essential communication in the business world and networking\n"
                                        "A business card can serve as a communication tool to promote your business\n"
                                        "products, or seervices. It can contain key information about what you offer", bg=color["terre"], fg=color["soleil"],
                                                font=(carct["lbl"], 15, "bold"))
        p1.place(x=position_home_X[0], y=position_home[3])

        blbcreate = Label(self.frameCent, text="CREATE YOUR BUSINESS CARD NOW", bg=color["terre"], fg=color["ciel"],
                         font=(carct["titre"], 20, "bold"))
        blbcreate.place(x=150, y=position_home[5])


        #CONTENU DE LA FENETRE DE L'ACCEUIL DE L'APLI

        nom = Label(frameNav, text="ELITE243+", fg=color["arbre"], bg=color["herbe"], font=(carct["titre"], 14))
        nom.place(x=950, y=5)
        enter_nom = Label(frameNav, text="BUSINESS CARD DESIGN", fg=color["arbre"], bg=color["herbe"], font=(carct["lbl"], 12))
        enter_nom.place(x=5, y=5)

        btnLat1 = Button(frameLat, text="Home",bg=color["soleil"],fg=color["terre"], width=btnLong[0],
                            font=(carct["lbl"], 9),command=self.Home)
        btnLat1.place(x=5, y=5)

        btnLat2 = Button(frameLat, text="Formulary recto",bg=color["soleil"],fg=color["terre"], width=btnLong[0],
                         font=(carct["lbl"], 9), command=self.FormulaireV)
        btnLat2.place(x=5, y=55)

        btnLat3 = Button(frameLat, text="Formulary verso",bg=color["soleil"],fg=color["terre"], width=btnLong[0],
                         font=(carct["lbl"], 9), command=self.FormulaireR)
        btnLat3.place(x=5, y=105)

        btnLat4 = Button(frameLat, text="Card",bg=color["soleil"],fg=color["terre"], width=btnLong[0],
                         font=(carct["lbl"], 9), command=self.Card)
        btnLat4.place(x=5, y=155)

        btnLat5 = Button(frameLat, text="About As",bg=color["soleil"],fg=color["terre"], width=btnLong[0],
                         font=(carct["lbl"], 9), command=self.About_US)
        btnLat5.place(x=5, y=205)

        btnLat6 = Button(frameLat, text="Close",bg=color["soleil"],fg=color["terre"], width=btnLong[0],
                         font=(carct["lbl"], 9), command=fen.quit)
        btnLat6.place(x=5, y=255)

    def Home(self):
        self.formulaire = Frame(self.frameCent, bg=color["terre"], height=450, width=980)
        self.formulaire.place(x=0, y=0)

        position_home = [5, 55, 105, 155, 205, 255, 305, 355]
        position_home_X = [20]

        bienvenu = Label(self.frameCent, text="BUSINESS CARD DESIGN", bg=color["terre"], fg=color["soleil"],
                         font=(carct["titre"], 30, "bold"))
        bienvenu.place(x=150, y=position_home[1])

        p1 = Label(self.frameCent,
                   text="A business card is an essential communication in the business world and networking\n"
                        "A business card can serve as a communication tool to promote your business\n"
                        "products, or seervices. It can contain key information about what you offer",
                   bg=color["terre"], fg=color["soleil"],
                   font=(carct["lbl"], 15, "bold"))
        p1.place(x=position_home_X[0], y=position_home[3])

        blbcreate = Label(self.frameCent, text="CREATE YOUR BUSINESS CARD NOW", bg=color["terre"], fg=color["ciel"],
                          font=(carct["titre"], 20, "bold"))
        blbcreate.place(x=150, y=position_home[5])

    def FormulaireV(self):
        self.formulaire = Frame(self.frameCent, bg=color["terre"], height=450, width=980)
        self.formulaire.place(x=0, y=0)

        #FORMULAIRE DE LA CARTE DE VISITE

        position_label = [55, 105, 155, 205, 255, 305, 5, 355, 400]
        position_labelX = [20]
        position_txtX = [150]

        self.lblfrom = Label(self.formulaire, text="FORMULARY FOR THE RECTO OF THE SERVICE CARD", bg=color["terre"], fg=color["soleil"],
                   font=(carct["lbl"], 15, "bold"))
        self.lblfrom.place(x=150, y=position_label[6])

        self.lblnom = Label(self.formulaire, text="Nom", bg=color["terre"], fg=color["soleil"],
                            font=(carct["lbl"], 12, "bold"))
        self.lblnom.place(x=position_labelX[0], y=position_label[0])
        self.txtNom = Entry(self.formulaire, bg=color["arbre"], fg=color["ciel"],
                            font=(carct["lbl"], 12, "bold"), width=60, bd=0)
        self.txtNom.place(x=position_txtX[0], y=position_label[0])

        self.lblPostNom = Label(self.formulaire, text="Post-nom ",bg=color["terre"], fg=color["soleil"],
                            font=(carct["lbl"], 12, "bold"))
        self.lblPostNom.place(x=position_labelX[0], y=position_label[1])
        self.txtPostNom = Entry(self.formulaire, bg=color["arbre"], fg=color["ciel"],
                            font=(carct["lbl"], 12, "bold"), width=60, bd=0)
        self.txtPostNom.place(x=position_txtX[0], y=position_label[1])

        self.lblPrenom = Label(self.formulaire, text="Prenom ", bg=color["terre"], fg=color["soleil"],
                            font=(carct["lbl"], 12, "bold"))
        self.lblPrenom.place(x=position_labelX[0], y=position_label[2])
        self.txtPrenom = Entry(self.formulaire, bg=color["arbre"], fg=color["ciel"],
                            font=(carct["lbl"], 12, "bold"), width=60, bd=0)
        self.txtPrenom.place(x=position_txtX[0], y=position_label[2])

        self.lblProfession = Label(self.formulaire, text="Profession ",bg=color["terre"], fg=color["soleil"],
                            font=(carct["lbl"], 12, "bold"))
        self.lblProfession.place(x=position_labelX[0], y=position_label[3])
        self.txtProfession = Entry(self.formulaire, bg=color["arbre"], fg=color["ciel"],
                            font=(carct["lbl"], 12, "bold"), width=60, bd=0)
        self.txtProfession.place(x=position_txtX[0], y=position_label[3])


        self.lblTel = Label(self.formulaire, text="Tel ",bg=color["terre"], fg=color["soleil"],
                            font=(carct["lbl"], 12, "bold"))
        self.lblTel.place(x=position_labelX[0], y=position_label[4])
        self.txtTel = Entry(self.formulaire,bg=color["arbre"], fg=color["ciel"],
                            font=(carct["lbl"], 12, "bold"), width=60, bd=0)
        self.txtTel.place(x=position_txtX[0], y=position_label[4])

        self.lblMail = Label(self.formulaire, text="E-mail adress ", bg=color["terre"], fg=color["soleil"],
                            font=(carct["lbl"], 12, "bold"))
        self.lblMail.place(x=position_labelX[0], y=position_label[5])
        self.txtMail = Entry(self.formulaire, bg=color["arbre"], fg=color["ciel"],
                            font=(carct["lbl"], 12, "bold"), width=60, bd=0)
        self.txtMail.place(x=position_txtX[0], y=position_label[5])

        self.lblAddpy = Label(self.formulaire, text="Adress Physic ", bg=color["terre"], fg=color["soleil"],
                               font=(carct["lbl"], 11, "bold"))
        self.lblAddpy.place(x=position_labelX[0], y=position_label[7])
        self.txtAddpy = Entry(self.formulaire, bg=color["arbre"], fg=color["ciel"],
                               font=(carct["lbl"], 12, "bold"), width=60, bd=0)
        self.txtAddpy.place(x=position_txtX[0], y=position_label[7])

        self.lblAcadem = Label(self.formulaire, text="Academic title ",bg=color["terre"], fg=color["soleil"],
                            font=(carct["lbl"], 11, "bold"))
        self.lblAcadem.place(x=position_labelX[0], y=position_label[8])
        self.txtAcadem = Entry(self.formulaire, bg=color["arbre"], fg=color["ciel"],
                             font=(carct["lbl"], 12, "bold"), width=60, bd=0)
        self.txtAcadem.place(x=position_txtX[0], y=position_label[8])




        # bouton validation et effacement du formulaire
        """
        btnValider = Button(self.formulaire, text="Valider", bg=color["arbre"], fg=color["ciel"],
                            font=(carct["lbl"], 11, "bold"), width=10)
        btnValider.place(x=150, y=420)
        btnValider = Button(self.formulaire, text="Delite", bg=color["arbre"], fg=color["ciel"],
                            font=(carct["lbl"], 11, "bold"), width=10)
        btnValider.place(x=580, y=420)
        """
    def FormulaireR(self):
        self.formulaire = Frame(self.frameCent, bg=color["terre"], height=450, width=980)
        self.formulaire.place(x=0, y=0)

        #FORMULAIRE DE LA CARTE DE VISITE AU VERSO
        position_label = [5, 55, 105, 155, 205, 255, 305]
        position_labelX = [20]
        position_txtX = [150]

        self.lblForm2 = Label(self.formulaire, text="FORMULARY FOR THE RECTO OF THE SERVICE CARD", bg=color["terre"], fg=color["soleil"],
                   font=(carct["lbl"], 15, "bold"))
        self.lblForm2.place(x=150, y=position_label[0])

        self.lblcompot1 = Label(self.formulaire, text="COMPETENCE 1", bg=color["terre"], fg=color["soleil"],
                            font=(carct["lbl"], 12, "bold"))
        self.lblcompot1.place(x=position_labelX[0], y=position_label[1])
        self.txtcompot1 = Entry(self.formulaire,  bg=color["arbre"], fg=color["ciel"],
                            font=(carct["lbl"], 12, "bold"), width=60, bd=0)
        self.txtcompot1.place(x=position_txtX[0], y=position_label[1])

        self.lblcompot2 = Label(self.formulaire, text="COMPETENCE 2",bg=color["terre"], fg=color["soleil"],
                            font=(carct["lbl"], 12, "bold"))
        self.lblcompot2.place(x=position_labelX[0], y=position_label[2])
        self.txtcompot2 = Entry(self.formulaire, bg=color["arbre"], fg=color["ciel"],
                            font=(carct["lbl"], 12, "bold"), width=60, bd=0)
        self.txtcompot2.place(x=position_txtX[0], y=position_label[2])

        self.lblcompot3 = Label(self.formulaire, text="COMPETENCE 3",bg=color["terre"], fg=color["soleil"],
                            font=(carct["lbl"], 12, "bold"))
        self.lblcompot3.place(x=position_labelX[0], y=position_label[3])
        self.txtcompot3 = Entry(self.formulaire, bg=color["arbre"], fg=color["ciel"],
                            font=(carct["lbl"], 12, "bold"), width=60, bd=0)
        self.txtcompot3.place(x=position_txtX[0], y=position_label[3])

        self.lblcompot4 = Label(self.formulaire, text="COMPETENCE 4",bg=color["terre"], fg=color["soleil"],
                            font=(carct["lbl"], 11, "bold"))
        self.lblcompot4.place(x=position_labelX[0], y=position_label[4])
        self.txtcompot4 = Entry(self.formulaire, bg=color["arbre"], fg=color["ciel"],
                            font=(carct["lbl"], 12, "bold"), width=60, bd=0)
        self.txtcompot4.place(x=position_txtX[0], y=position_label[4])

        self.lblcompot5 = Label(self.formulaire, text="COMPETENCE 5", bg=color["terre"], fg=color["soleil"],
                            font=(carct["lbl"], 11, "bold"))
        self.lblcompot5.place(x=position_labelX[0], y=position_label[5])
        self.txtcompot5 = Entry(self.formulaire, bg=color["arbre"], fg=color["ciel"],
                            font=(carct["lbl"], 12, "bold"), width=60, bd=0)
        self.txtcompot5.place(x=position_txtX[0], y=position_label[5])


        #bouton validation et effacement du formulaire

    def About_US(self):
        self.About = Frame(self.frameCent, bg=color["terre"], height=450, width=980)
        self.About.place(x=0, y=0)

        lblAb = Label(self.About, text="About us",bg=color["terre"], fg=color["ciel"],
                   font=(carct["lbl"], 20, "bold"))
        lblAb.place(x=400, y=5)

        #texte dans about us
        frameAboutTxt = Frame(self.About, width=550, height=350, bg=color["terre"])
        frameAboutTxt.place(x=400, y=60)
        lblapropos = Label(frameAboutTxt, text="Elite243+ s'engage à fournir des produits\n"
                                               "de haute qualité et des services commerciaux\n"
                                               "exceptionnels. Que vous ayez besoin de matières\n"
                                               "premières, de produits finis ou de solutions\n"
                                               "logistiques, nous sommes là pour répondre à vos\n"
                                               "besoins. Notre réseau de partenaires commerciaux\n"
                                               "et notre engagement envers l'excellence opérationnelle\n"
                                               "nous permettent de garantir des résultats exceptionnels\n"
                                               "pour nos clients à chaque étape. Si vous Êtes A la recherche\n"
                                               "d'une entreprise diversifiée pouvant répondre\n "
                                               "à un large éventail de besoins avec professionnalisme\n"
                                               " et expertise ? Ne cherchez pas plus loin car \nvous êtes au bon endroit.",
                                            bg=color["terre"], fg=color["soleil"],font=(carct["lbl"], 14, "italic"))
        lblapropos.place(x=0, y=0)

        #image dans about us
        frameAboutImg = Frame(self.About, width=350, height=350,)
        frameAboutImg.place(x=10, y=60)
        canIMG = Canvas(frameAboutImg, width=widthAbts, height=heightAbts, bd=0, highlightthickness=0,bg=color["terre"])
        canIMG.create_image(widthAbts / 2, heightAbts / 2, image=imageAbs)
        canIMG.place(x=0, y=0)

        #flooter about us
        frameFlooter = Frame(self.About, width=960, height=40, bg=color["carte"])
        frameFlooter.place(x=0, y=412)
        flooter = Label(frameFlooter, text="elite243+ all right reserved 2024",bg=color["carte"], fg=color["ciel"],
                   font=(carct["lbl"], 11, "bold"))
        flooter.place(x=350, y=10)


    def Card(self):
        self.rectFrame = Frame(self.frameCent, bg=color["terre"], height=450, width=980)
        self.rectFrame.place(x=0, y=0)
        lblCard = Label(self.rectFrame, text="YOUR BUSINESS CARD DESIGN", bg=color["terre"], fg=color["soleil"],
                   font=(carct["lbl"], 15, "bold"))
        lblCard.place(x=100, y=3)

        #RECTO DE LA CARTE
        frameRecto = Frame(self.rectFrame, width=450, height=280, bg=color["carte1"])
        frameRecto.place(x=10, y=50)

        #LE TITRE
        lblcard1 = Label(frameRecto, text="CARTE DE VISITE / BUSINESS CARD",  bg=color["carte1"], fg=color["soleil"],
                   font=(carct["titre"], 10, "bold"))
        lblcard1.place(x=80, y=30)

        # LE CONTENU DE LA CARTE
        lblposY = [0, 40,80, 120,160, 200,240,280]
        lblposX = [0, 80, 160, 200,240, 300]

        place1 = Frame(frameRecto, width=335, height=300,bg=color["carte1"])
        place1.place(x=10, y=85)

        lblnon = Label(place1, text=self.txtNom.get(),bg=color["carte1"], fg=color["ciel"],
                   font=(carct["lbl"], 10, "bold"))
        lblnon.place(x=lblposX[0], y=lblposY[0])


        lblPn = Label(place1, text=self.txtPostNom.get(), bg=color["carte1"], fg=color["ciel"],
                       font=(carct["lbl"], 10, "bold"))
        lblPn.place(x=lblposX[1], y=lblposY[0])
        #reponse

        lblPrn = Label(place1, text=self.txtPrenom.get(), bg=color["carte1"], fg=color["ciel"],
                       font=(carct["lbl"], 10, "bold"))
        lblPrn.place(x=lblposX[3], y=lblposY[0])
        #reponse

        lblPf = Label(place1, text=f"Profession {self.txtProfession.get()}", bg=color["carte1"], fg=color["soleil"],
                       font=(carct["lbl"], 10, "bold"))
        lblPf.place(x=lblposX[0], y=lblposY[1])
        #reponse

        lblTel = Label(place1, text=f"Tel {self.txtTel.get()}", bg=color["carte1"], fg=color["ciel"],
                       font=(carct["lbl"], 10, "bold"))
        lblTel.place(x=lblposX[0], y=lblposY[2])

        lblEm = Label(place1, text=f"E-Mail {self.txtMail.get()}", bg=color["carte1"], fg=color["soleil"],
                       font=(carct["lbl"], 10, "bold"))
        lblEm.place(x=lblposX[0], y=lblposY[3])

        lblAdressP = Label(place1, text=f"Adress {self.txtAddpy.get()}", bg=color["carte1"], fg=color["ciel"],
                       font=(carct["lbl"], 10, "bold"))
        lblAdressP.place(x=lblposX[0], y=lblposY[4])

        lblTitreA = Label(frameRecto, text=self.txtAcadem.get(), bg=color["carte1"], fg=color["ciel"],
                       font=(carct["lbl"], 10, "bold"))
        lblTitreA.place(x=330, y=250)

        # LES IMAGE ET LES ICONES
        canIMG = Canvas(frameRecto, width=widthVR, height=heightVR,  bd=0, highlightthickness=0, bg=color["carte1"])
        canIMG.create_image(widthVR/2,heightVR/2, image=imageRect)
        canIMG.place(x=0, y=2)

        canIMG2 = Canvas(frameRecto, width=widthVR, height=heightVR, bd=0, highlightthickness=0, bg=color["carte1"])
        canIMG2.create_image(widthVR / 2, heightVR / 2, image=imageRect2)
        canIMG2.place(x=350, y=2)

        canIMG3 = Canvas(frameRecto, width=widthPerso, height=heightPerso, bd=0, highlightthickness=0, bg=color["neutre"])
        canIMG3.create_image(widthVR / 2, heightVR / 2, image=imagePers)
        canIMG3.place(x=335, y=150)

        #---VERSO------------------------------------
        cardV = Frame(self.rectFrame, width=450, height=280, bg=color["carte"])
        cardV.place(x=500, y=50)
        labelElite = Label(cardV,text="ELITE243+ SERVICES",bg=color["carte"], fg=color["ciel"],
                       font=(carct["lbl"], 24, "bold"))
        labelElite.place(x=35, y=25)

        positVx = [50]
        positVy = [100,130,160,190]
        lblcompt1 = Label(cardV, text=f"{self.txtcompot1.get()}", bg=color["carte"], fg=color["soleil"],
                           font=(carct["titre"], 12, "bold"))
        lblcompt1.place(x=positVx[0], y=positVy[0])

        lblcompt2 = Label(cardV, text=f"{self.txtcompot2.get()}", bg=color["carte"], fg=color["soleil"],
                          font=(carct["titre"], 12, "bold"))
        lblcompt2.place(x=positVx[0], y=positVy[1])

        lblcompt3 = Label(cardV, text=f"{self.txtcompot3.get()}", bg=color["carte"], fg=color["soleil"],
                          font=(carct["titre"], 12, "bold"))
        lblcompt3.place(x=positVx[0], y=positVy[2])

        lblcompt4 = Label(cardV, text=f"{self.txtcompot4.get()}", bg=color["carte"], fg=color["soleil"],
                          font=(carct["titre"], 12, "bold"))
        lblcompt4.place(x=positVx[0], y=positVy[3])

        canIMGver = Canvas(cardV, width=widthVR, height=heightVR, bd=0, highlightthickness=0, bg=color["carte"])
        canIMGver.create_image(widthVR / 2, heightVR / 2, image=imageRect)
        canIMGver.place(x=350, y=200)


        #BOUTON IMPRIMER
        self.btnPrint = Button(self.rectFrame,text="Print Card", command=self.imprimer, bg=color["carte1"], fg=color["ciel"],
                       font=(carct["lbl"], 12, "bold"),width=50, )
        self.btnPrint.place(x=200, y=400)
    def imprimer(self):
        self.rectFrame.update()
        #xo=self.frameCent.winfo_rootx() + self.rectFrame.winfo_rootx()
        #yo=self.frameCent.winfo_rooty() + self.rectFrame.winfo_y()
        x1=500 + self.rectFrame.winfo_width()
        y1=500+self.rectFrame.winfo_height()

        ImageGrab.grab().crop((500,500,x1,y1)).save("frame_capture.png")



design1 = design()
design1.Acceuil()


fen.mainloop()