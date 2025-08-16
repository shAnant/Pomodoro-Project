from tkinter import *
import pygame
pygame.mixer.init()

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK = "✓"
reps = 0
work_done = 0
timer = None

#----------------------------- PLAY SOUND ---------------------------------#

def play_sound(path):
    sound = pygame.mixer.Sound(path)
    sound.play()

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps,work_done,timer
    
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    
    reps = 0
    work_done = 0
    timer = None
    
    tick_label.config(text="")
    timer_label.config(text="TIMER",fg=GREEN)
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    
    global reps
    global work_done
    
    reps += 1
    # work_sec = 10
    # short_break_sec = 2
    # long_break_sec = 5
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        timer_label.config(text="LONG BREAK",fg=RED)
        count_down(long_break_sec)
        play_sound("day 28/pomodoro-start/sounds/thud-sound-effect-319090.mp3")
        
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="SHORT BREAK",fg=PINK)
        play_sound("day 28/pomodoro-start/sounds/thud-sound-effect-319090.mp3")
        
    else:
        timer_label.config(text="WORK",fg=GREEN)
        count_down(work_sec)
        work_done+=1
        play_sound("day 28/pomodoro-start/sounds/air-horn-sound-effect-372453.mp3")
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    mins = count // 60
    secs = count % 60
    
    global reps
    global work_done
    
    if secs < 10:
        secs = f"0{secs}"
    canvas.itemconfig(timer_text,text=f"{mins}:{secs}")
    
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
        
    else:
        tick_label.config(text=f"{TICK*work_done}")
        start_timer()
        
# ---------------------------- UI SETUP ------------------------------- #
window  = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW )


canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomoto_img = PhotoImage(file="day 28/pomodoro-start/tomato.png")
canvas.create_image(100,112,image=tomoto_img)

timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

timer_label = Label(text="Timer",font=(FONT_NAME,30,"bold"),bg=YELLOW,fg=GREEN)
timer_label.grid(row=0,column=1)

start_button = Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(row=2,column=2)


tick_label = Label(text=f"{TICK*work_done}",font=(FONT_NAME,15,"bold"),bg=YELLOW,fg=GREEN)
tick_label.grid(row=3,column=1)

window.mainloop()