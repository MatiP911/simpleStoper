import customtkinter as ctk
import time


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x300")
        self.title("Clock")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=2, uniform='a')

        self.textVar = ctk.StringVar(value="")

        self.clock = ctk.CTkLabel(self, textvariable=self.textVar)
        self.clock.grid(row=0, column=0, sticky="nswe")

        self.time()

        self.mainloop()

    def time(self):
        aktualny_czas = time.strftime("%H:%M:%S")
        self.textVar.set(aktualny_czas)

        self.after(1000, self.time)


if __name__ == '__main__':
    App()
