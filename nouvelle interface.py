# -*- coding: utf-8 -*-
import os
import wx
import wx.adv

ID_Menu_Connexion   = 5000
ID_Menu_Open  = 5001
ID_Menu_Exit  = 5002

wildcard = "Bitmap files (*.bmp)|*.bmp|"              \
           "JPEG files (*.jpg, *jpeg)|*.jpg, *.jpeg|" \
           "PNG files (*.png)|*.png|"                 \
           "GIF files (*.gif)|*.gif|"                 \
           "Icon files (*.ico)|*.ico|"                \
           "Targa files (*.tga)|*.tga|"               \
           "TIFF files (*.tif,*tiff)|*.tif,*tiff|"    \
           "All files (*.*)|*.*"


def Connect(self,events):
    self.Close( True )

def action(self,events):
        self.Close( True )



class MyParentFrame( wx.MDIParentFrame ):

    def __init__( self ):
        wx.MDIParentFrame.__init__( self,
                                    None,
                                    -1,
                                    "Outils de creation RDS Microsoft Azur",
                                    size  = (900,700),
                                    style = wx.DEFAULT_FRAME_STYLE | wx.HSCROLL | wx.VSCROLL )
        self.create_menu_bar()
        self.create_toolbar()



    def create_menu_bar( self ):
        # create the "File" menu
        menuFile = wx.Menu()
        menuFile.Append( ID_Menu_Connexion,  "&Connexion" )
        menuFile.Append( ID_Menu_Open, "&Nouveau client" )
        menuFile.AppendSeparator()
        menuFile.Append( ID_Menu_Exit, "E&xit" )

        # create the menu bar
        menubar = wx.MenuBar()
        menubar.Append( menuFile, "&File" )
        self.SetMenuBar( menubar )

        # bind the events
        self.Bind( wx.EVT_MENU, self.OnNewWindow, id = ID_Menu_Connexion )
        self.Bind( wx.EVT_MENU, self.OnOpenFile,  id = ID_Menu_Open )
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
                    "Long help for 'New'",
                    None )

        # open file
        open_bmp = wx.ArtProvider.GetBitmap( wx.ART_FILE_OPEN, wx.ART_TOOLBAR, tsize )
        tb.AddTool( ID_Menu_Open,
                    "Open",
                    open_bmp,
                    wx.NullBitmap,
                    wx.ITEM_NORMAL,
                    "Open",
                    "Long help for 'Open'",
                    None )

        # display the toolbar
        tb.Realize()

        # bind the events
        self.Bind( wx.EVT_TOOL, self.OnNewWindow, id = ID_Menu_Connexion )
        self.Bind( wx.EVT_TOOL, self.OnOpenFile,  id = ID_Menu_Open )




    #def OnNewWindow( self, event ):
    #win    = wx.MDIChildFrame( self, -1, "Fenetre de connexion")
    #canvas = wx.ScrolledWindow( win )
    #win.SetSize(700, 300)


class MyFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, size = (700 , 700), title='Authentification Connexion SSH')
        self.Centre()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    #frame.SetBackgroundColour = "Bleue"
    panel=wx.Panel(frame)

        def OnNewWindow( self, event ):
        win    = wx.MDIChildFrame( self, -1, "Fenetre de connexion")
        canvas = wx.ScrolledWindow( win )
        win.SetSize(700, 300)

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

        #win.Show( True )







class MyApp( wx.App ):
    def OnInit( self ):
        frame = MyParentFrame()
        frame.Show( True )
        self.SetTopWindow( frame )
        return True


if __name__ == '__main__':
    app = MyApp( False )
    app.MainLoop()
