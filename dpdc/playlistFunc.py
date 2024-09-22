import PySimpleGUI as gui
import os
global playlistdir
playlistdir = "playlists"
def splitsong(song,sortmode):
    newsong=""
    if sortmode=="-TITLESORT-": # if title first
        newsong = newsong + song[0] + "***"
        newsong = newsong + song[1] + "***"
        newsong = newsong + song[2] + "***"
        newsong = newsong + song[3] + "***"
        newsong = newsong + song[4] + "***"
        newsong = newsong + song[5]
    elif sortmode=="-ARTISTSORT-":
        newsong = newsong + song[1] + "***"
        newsong = newsong + song[0] + "***"
        newsong = newsong + song[2] + "***"
        newsong = newsong + song[3] + "***"
        newsong = newsong + song[4] + "***"
        newsong = newsong + song[5]
    elif sortmode == "-ALBUMSORT-":
        newsong = newsong + song[1] + "***"
        newsong = newsong + song[2] + "***"
        newsong = newsong + song[0] + "***"
        newsong = newsong + song[3] + "***"
        newsong = newsong + song[4] + "***"
        newsong = newsong + song[5]
    return newsong

def getPlaylists():
    playlists = os.listdir(playlistdir)  # gets every file in playlistdir
    if len(playlists) > 0:
        for i in range(len(playlists)):
            playlists[i] = playlists[i][:-4]
    return playlists

def main(song,sortmode):
    origindir=os.getcwd()
    imagedir="images"
    logo=imagedir+"/bigicon.ico"

    logotheme = {'BACKGROUND': '#1f1f1f',
                    'TEXT': 'white',
                    'INPUT': '#ff7145',
                    'TEXT_INPUT': '#000000',
                    'SCROLL': '#480b9c',
                    'BUTTON': ('white', '#480b9c'),
                    'PROGRESS': ('#01826B', '#D0D0D0'),
                    'BORDER': 1,
                    'SLIDER_DEPTH': 0,
                    'PROGRESS_DEPTH': 0}

    gui.theme_add_new("LogoTheme",logotheme)
    gui.theme("LogoTheme")



    boxcolumn=[[gui.Text("Current Playlists"),gui.InputText(song,readonly=True,size=(20,None)),gui.Button("Refresh")],
            [gui.Listbox(values=[],key="-PLAYLISTS-",size=(50,10))]]
    buttoncolumn=[[gui.Button("Create New",key="-CREATE-")],
                  [gui.Button("Add to Selected",key="-ADD-")],
                  [gui.Button("Exit")],
                  [gui.Text("Playlist Title:",key="-TITLETEXT-",visible=False),gui.Input(key="-INPUT-",visible=False),gui.Button("Submit",key="-SUBMIT-",visible=False)]]

    layout=[[gui.Column(boxcolumn),gui.Column(buttoncolumn)]]
    playwindow=gui.Window(title="Playlist Manager",icon=logo,layout=layout)


    while True:
        try:
            event, values = playwindow.read()

            playwindow["-PLAYLISTS-"].update(values=getPlaylists())

            if event in (gui.WINDOW_CLOSED,"Exit",gui.WIN_CLOSED):
                playwindow.close()
                break
            if event=="-ADD-":

                file=values["-PLAYLISTS-"][0]+".txt"
                print(file,"file")
                os.chdir(playlistdir)
                f=open(file,"a")
                f.write(splitsong(song,sortmode)+"\n")
                f.close()
                os.chdir(origindir)

            if event=="-CREATE-":
                playwindow["-TITLETEXT-"].update(visible=True)
                playwindow["-INPUT-"].update(visible=True)
                playwindow["-SUBMIT-"].update(visible=True)

            if event == "-SUBMIT-":
                os.chdir(playlistdir)
                print(values["-INPUT-"]+".txt")
                f=open(values["-INPUT-"]+".txt","a+")
                f.close()
                os.chdir(origindir)
                playlists = os.listdir(playlistdir)
                if len(playlists) > 0:
                    for i in range(len(playlists)):
                        playlists[i] = playlists[i][:-4]
                playwindow["-PLAYLISTS-"].update(values=playlists)
                playwindow["-INPUT-"].update("")

            if event== "Refresh":
                playwindow["-PLAYLISTS-"].update(values=getPlaylists())
        except:
            break








