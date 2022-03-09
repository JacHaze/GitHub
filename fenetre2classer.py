
#Import du module Graphique wxpython.
import wx
import paramiko
#def de variable !!
host = "128.127.130.18"
port = 22
username = ""
password = ""
command = "ls"
command2 = "cp cfao.key Musique/"



def action(event):
    frame.Close()

def Connect(event):
    print(mypassword.GetValue())
    print(mylogin.GetValue())
    password = mypassword.GetValue()
    username = mylogin.GetValue()

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)

    stdin, stdout, stderr = ssh.exec_command(command)
    lines = stdout.readlines()
    print(lines)

    stdin, stdout, stderr = ssh.exec_command(command2)
    lines2 = stdout.readlines()
    print(lines2)
    ssh.close()




#config de la frame-1 de connexion
app = wx.App()
frame = wx.Frame(None)
frame.Title = "Authentification Connexion SSH"
frame.SetSize(400 , 300 , 500 , 200)
frame.BackgroundColour = "White"
panel = wx.Panel(frame)
panel.SetBackgroundColour('blue')
#champs text pour saisie login et mot de passe.
mylogin = wx.TextCtrl(panel, -1 , "Utilisateur")
mylogin.SetSize(25, 0 , 150 , 30)
mypassword = wx.TextCtrl(panel, -1 , "Mot de passe" , style = wx.TE_PASSWORD)
mypassword.SetSize(250, 0 , 150 , 30)



#Bouton connexion.
myBconnexion = wx.Button(panel, label ="Connexion")
myBconnexion.SetSize(25, 120 , 150 , 30)
myBconnexion.Bind(wx.EVT_BUTTON , Connect)

#Bouton Quitter.
myBDeconnexion = wx.Button(panel, label ="Quitter")
myBDeconnexion.SetSize(300, 120 , 150 , 30)
myBDeconnexion.Bind(wx.EVT_BUTTON , action)




#Affichage de la fenetre.
frame.Show()

app.MainLoop()
