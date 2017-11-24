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
        
    def create_top_display(self):
        frame=tk.Frame(self.root)
        glass_frame_image=tk.PhotoImage(file='../icons/glass_frame.gif')
        self.canvas=tk.Canvas(frame,width=370,height=90)
        self.canvas.image=glass_frame_image
        self.canvas.grid(row=1)
        self.console=self.canvas.create_image(0,10,anchor=tk.NW,image=glass_frame_image)
        self.clock=self.canvas.create_text(125,68,anchor=tk.W,fill='#CBE4F6',text='00:00')
        self.track_lenght_text=self.canvas.create_text(167,68,anchor=tk.W,fill='#CBE4F6',text="of 00:00")
        self.track_name=self.canvas.create_text(50,35,anchor=tk.W,fill='#9CEDAC',text='\"Currently playing: none \"')
        frame.grid(row=1,pady=1,padx=0)
    
    def create_button_frame(self):
        pass


if __name__=='__main__':
    root=Tk()
    root.resizable(width=False,height=False)
    player=player()
    model=model.Model()
    app=View(roor,model,player)
    root.mainloop()
    