import random  # random er modulen vi må bruke for å få programmet / input'en til å gi oss tilfeldige verdier på terningene
from tkinter import *  # tkinter er modulen som gir oss muligheten til å åpne et vindu / program

# import random // fordi terningene blir ikke trillet til en bestemt verdi men tilfeldig iht. linje 14

root = Tk()
# en command en bruker i begynnesen av tkinter loopen for å åpne programmet
root.title(
    "                                                                                     Random Dice Roller"
)
# bruker mange spaces her for å få teksten av root.title i midten av vinduet
root.geometry("700x450")
# Dette er størrelsen på tk programmet/ vinduet

l1 = Label(root, font=("times", 200), background="deeppink", fg="black")
# background gir bakgrunnen bak terningene en farge og fg = back er selve terningen


def roll():  # Nr1       Nr2         Nr3     Nr4     Nr5         Nr6
    number = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]
    # Disse verdiene er egenskapen til tallene 1 - 6
    l1.config(text=f"{random.choice(number)}{random.choice(number)}")
    # Bruker 2x {random.choice(number)} fordi det skal være 2 terninger
    l1.pack()


b1 = Button(root, text="Roll The Dices!", command=roll)
# Dette er hva knappen sier / hva som står på knappen
b1.place(x=310, y=0)
# Dette blir plasseringen på b1 = knappen "Roll The Dices!"

root.mainloop()
# En command en bruker når en skal åpne et vindu i tkinter
