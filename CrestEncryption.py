# python module to create GUI
from tkinter import *
import pyperclip

#configure tkinter
root = Tk()
root.title("CAESAR CIPHER DECODER")
root.geometry("420x435")
root.configure(bg='gray13')
photo = PhotoImage(file = "padlock.png")
root.iconphoto(False, photo)

#function for paste button
def paste():
    ciphertextEntry.insert(0, pyperclip.paste())

#algorithm to decrypt the cipher
def brute_force_output():
    OutputText.delete(1.0, END)
    message = (ciphertextEntry.get()).upper()  # encrypted message
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    #if no shift is entered
    if ShiftEntry.get() == '':
        for key in range(len(LETTERS)):
             translated = ''
             for symbol in message:
                 if symbol in LETTERS:
                    num = LETTERS.find(symbol)
                    num = num - key
                    if num < 0:
                        num = num + len(LETTERS)
                        translated = translated + LETTERS[num]
                    else:
                        translated = translated + symbol
             OutputString = str('SHIFT -%s: %s \n' % (key, translated))
             OutputText.insert(END, OutputString)

    #if a shift is entered
    else:
        translated = ''
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                key = int(ShiftEntry.get())
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                    translated = translated + LETTERS[num]
                else:
                    translated = translated + symbol
        OutputString = str('SHIFT -%s: %s \n' % (key, translated))
        OutputText.insert(END, OutputString)


#allow user to enter the cipher text
ciphertext_label = Label(root, text='ENTER CIPHER TEXT:', bg="gray13", fg="green2")
ciphertext_label.grid(row=1, column=1, pady=(10, 0), padx=(20, 0), sticky="W")
ciphertextEntry = Entry(root, bg="gray25", fg="green2", width="30")
ciphertextEntry.grid(row=2, column=1, pady=(0, 0), padx=(20, 0))

#allow user to enter the shift if they know it
shiftlabel = Label(root, text='NEGATIVE SHIFT (IF KNOWN):', bg="gray13", fg="green2")
shiftlabel.grid(row=4, column=1, pady=(10, 0), padx=(20, 0), sticky="W")
ShiftEntry = Entry(root, bg="gray25", fg="green2", width="30")
ShiftEntry.grid(row=5, column=1, padx=(20, 0))

# creating decrypt button to produce the output
decrypt = Button(root, text="DECRYPT", bg="red", fg="white", width="15", command=brute_force_output)
decrypt.grid(row=3, column=1, pady=(10, 0), padx=(20, 0), sticky = "W")
# creating paste button to paste from clipboard
paste = Button(root, text="PASTE", bg="blue", fg="white", width="8", command=paste)
paste.grid(row=3, column=1, pady=(10, 0), padx=(20, 0), sticky = "E")


#instructions
Inst = Label(root, text=""
                                    "Instructions:"
                                    "\n\n1. Enter or paste cipher text \nabove"
                        "\n\n2. If you know the shift\nenter it. If not, leave blank"
                        "\n\n3. Press the decrypt button"
                        "\n\n4. Your decrypted text will\nappear on the right", bg="gray13", fg="light blue")
Inst.grid(row=6, column=1, pady=(10, 0))

#Output
OutputText = Text(root, width=23, height=26, bg="gray13", fg="green2")
OutputText.grid(row=1, column=2, rowspan=20, pady=(5, 0), padx=(20, 0))

root.mainloop()