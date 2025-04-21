import customtkinter as ctk
import keyboard

windowSize = (300, 230)
stoperFontSize = 100
startStopButton = 'F5'
resetButton = 'F6'

BGCOL = "#2c2c2a"
TXTMAIN = "#fff3f3"
TXTSECOND = "#a07cff"


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f"{windowSize[0]}x{windowSize[1]}")
        self.title("Stoper")
        self.configure(fg_color=BGCOL)
        self.resizable(False, False)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=2, uniform='a')

        self.textVar = ctk.StringVar(value="")

        self.clock = ctk.CTkLabel(
            self, textvariable=self.textVar,
            font=ctk.CTkFont(size=stoperFontSize), text_color=TXTMAIN)
        self.clock.bind("<Button-1>", self.resetTime)
        self.clock.grid(row=0, column=0, sticky="nswe")

        self.stopped = True
        self.resetTime()
        self.stoperLogic()

        keyboard.add_hotkey(startStopButton, self.stopStart)
        keyboard.add_hotkey(resetButton, self.resetTime)

        self.mainloop()

    def resetTime(self, event=None):
        self.timeCount = 0
        self.textVar.set("00:00")

    def stopStart(self):
        self.stopped = not self.stopped

    def stoperLogic(self):
        if (self.stopped):
            self.after(1000, self.stoperLogic)
            return

        self.timeCount += 1

        if (self.timeCount % 60 == 0 or self.timeCount % 60 == 30):
            self.clock.configure(text_color=TXTSECOND)
        else:
            self.clock.configure(text_color=TXTMAIN)

        minutes = self.timeCount // 60
        seconds = self.timeCount % 60
        stoperString = f"{minutes:02}:{seconds:02}"
        self.textVar.set(stoperString)

        self.after(1000, self.stoperLogic)


if __name__ == '__main__':
    App()
