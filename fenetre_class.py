import wx
import paramiko
import wx.adv

#def de variable !!
host = "128.127.130.18"
port = 22
username = ""
password = ""
command = "ls"
command2 = "cp cfao.key Musique/"


#Definition de l'action du bouton Quitter!
def action(event):
    frame.Close()
#definition de l'action de login en utilisant le bouton connecter!
def Connect(event):
    print(mypassword.GetValue())
    print(mylogin.GetValue())
    password = mypassword.GetValue()
    username = mylogin.GetValue()

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #etablissement de la connexion!
    ssh.connect(host, port, username, password)
    #print ("vous etes bien connecté")
    wx.MessageBox("Vous etes bien connecté", "Validation de la connexion" ,wx.OK | wx.ICON_INFORMATION)


    stdin, stdout, stderr = ssh.exec_command(command)
    lines = stdout.readlines()
    print(lines)

    stdin, stdout, stderr = ssh.exec_command(command2)
    lines2 = stdout.readlines()
    print(lines2)
    ssh.close()


class MyFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, size = (700 , 700), title='Authentification Connexion SSH')
        self.Centre()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    #frame.SetBackgroundColour = "Bleue"
    panel=wx.Panel(frame)

class Mydial(wx.Dialog):

    def __init__(self, parent, title):
        wx.Dialog.__init__(parent, title = "Connexion", size = (250,150))

#champs text pour saisie login et mot de passe.
mylogin = wx.TextCtrl(panel, 0 , "Utilisateur")
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


frame.Show()

app.MainLoop()
