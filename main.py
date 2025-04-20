import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x300")
        self.title("Clock")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=2, uniform='a')

        self.textVar = ctk.StringVar(value="")

        self.clock = ctk.CTkLabel(
            self, textvariable=self.textVar)
        self.clock.bind("<Button-1>", self.resetTime)
        self.clock.grid(row=0, column=0, sticky="nswe")

        self.resetTime()
        self.time()

        self.mainloop()

    def resetTime(self, event=None):
        self.timeCount = 0

    def time(self):
        self.timeCount += 1

        minutes = self.timeCount // 60
        seconds = self.timeCount % 60
        stoperString = f"{minutes:02}:{seconds:02}"
        self.textVar.set(stoperString)

        self.after(1000, self.time)


if __name__ == '__main__':
    App()
