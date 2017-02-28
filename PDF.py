"""Merge multiple PDFs
"""
from PyPDF2 import PdfFileMerger
from tkinter import *
from tkinter.filedialog import askopenfilenames


def merge():
    '''Merge function'''
    mergewindow = Tk()
    mergewindow.geometry('500x300')
    files = askopenfilenames(parent=mergewindow, filetypes=[("PDF Files", ".pdf")])
    listbox = Listbox(mergewindow)
    listbox.pack()
    for item in files:
        listbox.insert(END, item)
    listbox.mainloop()


def split():
    '''Split function'''
    print("split")


def reorder():
    '''reorder function'''
    print("reorder")


def main():
    '''gui portion'''
    root = Tk()
    root.geometry('300x300+1000+500')
    button_compare = Button(root, text="Merge PDF's", command=lambda: merge())
    button_loadatt = Button(root, text="Split PDF's", command=lambda: split())
    button_reorder = Button(root, text="Reorder PDF's", command=lambda: reorder())
    button_compare.pack(pady=10, padx=10)
    button_loadatt.pack(pady=10, padx=10)
    button_reorder.pack(pady=10, padx=10)
    root.mainloop()

if __name__ == '__main__':
    main()
