"""Merge multiple PDFs
"""
from PyPDF2 import PdfFileMerger, PdfFileReader
from tkinter import *
from tkinter.filedialog import askopenfilenames, asksaveasfilename


def merge():
    '''Merge function'''
    def move_up(listbox):
        '''move file up'''
        print(listbox.curselection())
        items = listbox.curselection()
        for item in items:
            item.index()

    def move_down(listbox):
        '''move file down'''

    def execute(listbox):
        output_file = asksaveasfilename(parent=mergewindow, filetypes=[('PDF Files', '.pdf')])
        merger = PdfFileMerger(strict=FALSE)
        for file_name in enumerate(listbox.get(0, END)):
            print(file_name[1])
            merger.append(PdfFileReader(open(file_name[1], 'rb')))
        merger.write(output_file)


    mergewindow = Tk()
    maxlength = 0
    mergewindow.geometry('500x300')
    files = askopenfilenames(parent=mergewindow, filetypes=[("PDF Files", ".pdf")])
    button_up = Button(mergewindow, text='Move Up', command=lambda: move_up(listbox))
    button_down = Button(mergewindow, text='Move Down', command=lambda: move_down(listbox))
    button_merge = Button(mergewindow, text='Merge', command=lambda: execute(listbox))
    listbox = Listbox(mergewindow, selectmode=EXTENDED)
    for item in files:
        listbox.insert(END, item)
        if len(item) > maxlength:
            maxlength = len(item)
    listbox.config(height=len(files), width=maxlength)
    listbox.pack()
    button_up.pack()
    button_down.pack()
    button_merge.pack()
    mergewindow.mainloop()


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
