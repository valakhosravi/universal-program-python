from tkinter.filedialog import askopenfilename

if __name__ == "__main__":
    filename = askopenfilename()
    f = open(filename, "r")
    print(f.read())
