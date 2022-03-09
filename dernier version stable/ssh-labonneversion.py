# -*- coding: utf-8 -*-
import os
import wx
import wx.adv
import paramiko


#------------------------------------------------------------------------------
#variable !!
host = "128.127.130.18"
port = 22
username = ""
password = ""
command = "ls"
command2 = "cp cfao.key Musique/"
mypassword= ""
#-------------------------------------------------------------------------------
ID_Menu_Connexion   = 5000
ID_Menu_Open  = 5001
ID_Menu_Exit  = 5002
ID_Menu_Appversion = 5003
ID_Menu_Newuser = 5004

wildcard = "Bitmap files (*.bmp)|*.bmp|"              \
           "JPEG files (*.jpg, *jpeg)|*.jpg, *.jpeg|" \
           "PNG files (*.png)|*.png|"                 \
           "GIF files (*.gif)|*.gif|"                 \
           "Icon files (*.ico)|*.ico|"                \
           "Targa files (*.tga)|*.tga|"               \
           "TIFF files (*.tif,*tiff)|*.tif,*tiff|"    \
           "All files (*.*)|*.*"

#------------------------------------------------------------------------------
class MyParentFrame( wx.MDIParentFrame ):

    def __init__( self ):
        wx.MDIParentFrame.__init__( self,
                                    None,
                                    -1,
                                    "Outils de creation RDS Microsoft Azur",
                                    size  = (1600,900),
                                    style = wx.DEFAULT_FRAME_STYLE | wx.HSCROLL | wx.VSCROLL )
        self.create_menu_bar()
        self.create_toolbar()



    def create_menu_bar( self ):
        # create the "File" menu
        menuFile = wx.Menu()
        menuFile.Append( ID_Menu_Connexion,  "&Connexion" )
        menuFile.Append( ID_Menu_Open, "&Nouveau Client" )
        menuFile.Append( ID_Menu_Appversion, "&Nouvelle Version Applicative" )
        menuFile.Append( ID_Menu_Newuser, "&Nouveau Utilisateur" )
        menuFile.AppendSeparator()
        menuFile.Append( ID_Menu_Exit, "E&xit" )

        # Create the "Action" menu
        #menu2.file =

        # create the menu bar
        menubar = wx.MenuBar()
        menubar.Append( menuFile, "&File" )
        self.SetMenuBar( menubar )

        # bind the events
        self.Bind( wx.EVT_MENU, self.OnNewWindow, id = ID_Menu_Connexion )
        self.Bind( wx.EVT_MENU, self.OnOpenFile,  id = ID_Menu_Open )
        self.Bind( wx.EVT_MENU, self.OnOpenFile ,  id = ID_Menu_Appversion )
        self.Bind( wx.EVT_MENU, self.OnOpenFile ,  id = ID_Menu_Newuser )
        self.Bind( wx.EVT_MENU, self.OnExit,      id = ID_Menu_Exit )



    def create_toolbar( self ):
        # create the toolbar
        tsize = ( 32, 32 )
        tb    = self.CreateToolBar( True )
        tb.SetToolBitmapSize( tsize )

        # new window
        new_bmp =  wx.ArtProvider.GetBitmap( wx.ART_NEW, wx.ART_TOOLBAR, tsize )
        tb.AddTool( ID_Menu_Connexion,
                    "Connexion",
                    new_bmp,
                    wx.NullBitmap,
                    wx.ITEM_NORMAL,
                    "Connexion",
                    "Long help for 'Connexion'",
                    None )

        # open file
        open_bmp = wx.ArtProvider.GetBitmap( wx.ART_REDO, wx.ART_TOOLBAR, tsize )
        tb.AddTool( ID_Menu_Open,
                    "Nouveau Client",
                    open_bmp,
                    wx.NullBitmap,
                    wx.ITEM_NORMAL,
                    "Nouveau Client",
                    "Long help for 'Nouveau Client'",
                    None )

        # Versionapp
        Versionapp_bmp = wx.ArtProvider.GetBitmap( wx.ART_PLUS, wx.ART_TOOLBAR, tsize )
        tb.AddTool( ID_Menu_Appversion,
                            "Nouvelle Version Applicative",
                            Versionapp_bmp,
                            wx.NullBitmap,
                            wx.ITEM_NORMAL,
                            "Nouvelle App",
                            "Long help for 'Nouvelle App'",
                            None )

        #Nouveau Utilisateurs RDS Azure
        Newuser_bmp = wx.ArtProvider.GetBitmap( wx.ART_DELETE, wx.ART_TOOLBAR, tsize )
        tb.AddTool( ID_Menu_Newuser,
                            "Nouveau Utilisateurs",
                            Newuser_bmp,
                            wx.NullBitmap,
                            wx.ITEM_NORMAL,
                            "Nouveau Utilisateur",
                            "Long help for 'Nouveau Utilisateur'",
                            None )



        # display the toolbar
        tb.Realize()

        # bind the events
        self.Bind( wx.EVT_TOOL, self.OnNewWindow, id = ID_Menu_Connexion )
        self.Bind( wx.EVT_TOOL, self.OnOpenFile,  id = ID_Menu_Open )
        self.Bind( wx.EVT_TOOL, self.OnOpenFile,  id = ID_Menu_Appversion )
        self.Bind( wx.EVT_TOOL, self.OnOpenFile,  id = ID_Menu_Newuser )




    def OnNewWindow( self, event ):
        win    = wx.MDIChildFrame( self, -1, "Fenetre de connexion")
        win.SetSize(700, 300)


        panel = wx.Panel(win)
        panel.SetSize( 0 , 0 , 900 , 700 )
        panel.SetBackgroundColour('Grey')


        #Definition de l'action du bouton Quitter!
        def action(event):
            win.Close()
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
#-------------------------------------------------------------------------------
        #champs text pour saisie login et mot de passe.
        mylogin = wx.TextCtrl(panel, -1 , "Utilisateur")
        mylogin.SetSize(25, 25 , 150 , 30)
        mypassword = wx.TextCtrl(panel, -1 , "Mot de passe" , style = wx.TE_PASSWORD)
        mypassword.SetSize(250, 25 , 150 , 30)

        #Bouton connexion.
        myBconnexion = wx.Button(panel, label ="Connexion")
        myBconnexion.SetSize(25, 120 , 150 , 30)
        myBconnexion.Bind(wx.EVT_BUTTON , Connect)

        #Bouton Quitter.
        myBDeconnexion = wx.Button(panel, label ="Quitter")
        myBDeconnexion.SetSize(250, 120 , 150 , 30)
        myBDeconnexion.Bind(wx.EVT_BUTTON , action)

        win.Show( True )

#-------------------------------------------------------------------------------
    def OnOpenFile( self, event ):

        win2 = wx.MDIChildFrame( self, -1, "Creation nouveau client")
        win2.SetSize(1550, 800)
        panel2 = wx.Panel(win2)
        panel2.SetSize( 0 , 0 , 900 , 700 )
        panel2.SetBackgroundColour('Grey')
        win2.Show( True )


    def OnExit( self, event ):
        self.Close( True )



    def read_file( self, filename ):
        # read image if possible
        try:
            image = wx.Image( filename, wx.BITMAP_TYPE_ANY )
        except:
            return

        # create the window
        win     = wx.MDIChildFrame( self, -1, filename )
        canvas  = wx.ScrolledWindow( win )
        sizer   = wx.BoxSizer( wx.HORIZONTAL )
        statBmp = wx.StaticBitmap( canvas,
                                   wx.ID_ANY,
                                   image.ConvertToBitmap() )
        sizer.Add( statBmp, 1, wx.EXPAND )
        canvas.SetSizer( sizer )
        sizer.Fit( canvas )
        win.Show( True )


#------------------------------------------------------------------------------
class MyApp( wx.App ):
    def OnInit( self ):
        frame = MyParentFrame()
        frame.Show( True )
        self.SetTopWindow( frame )
        return True


if __name__ == '__main__':
    app = MyApp( False )
    app.MainLoop()
