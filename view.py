import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import tkinter.ttk
import model
import player

AUDIO_PLAYER_NAME="Audio Player"

class View:
    def __init__(self,rot,model,player):
        self.root=root
        self.model=model
        self.player=player
        self.create_gui()
    
    def create_gui(self):
        self.root.title(AUDIO_PLAYER_NAME)
        self.create_top_player()
        self.create_button_frame()
        self.create_list_box()
        self.create_bottom_frame()
        
    


if __name__=='__main__':
    root=Tk()
    root.resizable(width=False,height=False)
    player=player()
    model=model.Model()
    app=View(roor,model,player)
    root.mainloop()
    