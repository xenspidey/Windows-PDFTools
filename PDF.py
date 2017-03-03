"""Merge multiple PDFs
"""
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
from tkinter import *
from tkinter.filedialog import askopenfilenames, askopenfilename, asksaveasfilename


def merge():
    '''Merge function'''
    def move_up(listbox):
        '''move file up'''
        poslist = listbox.curselection()
        if not poslist:
            return
        for pos in poslist:
            if pos == 0:
                return
            text = listbox.get(pos)
            listbox.delete(pos)
            listbox.insert(pos-1, text)
            listbox.selection_set(pos-1)

    def move_down(listbox):
        '''move file down'''
        poslist = listbox.curselection()
        if not poslist:
            return
        for pos in reversed(poslist):
            print(pos, len(listbox.get(0, END)))
            if pos+1 == len(listbox.get(0, END)):
                return
            text = listbox.get(pos)
            listbox.delete(pos)
            listbox.insert(pos+1, text)
            listbox.selection_set(pos+1)


    def execute_merge(listbox):
        '''begin the mergeing process'''
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
    listbox = Listbox(mergewindow, selectmode=EXTENDED)
    button_up = Button(mergewindow, text='Move Up', command=lambda: move_up(listbox))
    button_down = Button(mergewindow, text='Move Down', command=lambda: move_down(listbox))
    button_merge = Button(mergewindow, text='Merge', command=lambda: execute_merge(listbox))
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

    def execute_split(file, pages):
        '''begin splitting process'''
        fileout = asksaveasfilename(parent=splitwindow, filetypes=[('PDF Files', '.pdf')])
        inputfile = PdfFileReader(open(file, 'rb'))
        for i in pages:
            outputfile = PdfFileWriter()
            outputfile.addPage(inputfile.getPage(pages[i]))
            outputfilename = (fileout
            with open()

    splitwindow = Tk()
    splitwindow.geometry('500x300')
    file = askopenfilename(parent=splitwindow, filetypes=[("PDF Files", ".pdf")])
    listbox = Listbox(splitwindow, selectmode=EXTENDED)
    pages = []
    button_split = Button(splitwindow, text='Merge', command=lambda: execute_split(file, lambda: pages))
    button_selectall = Button(splitwindow, text='Merge', \
                                command=lambda: listbox.selection_set(0, END))
    button_selectnone = Button(splitwindow, text='Merge', \
                                command=lambda: listbox.selection_clear(0, END))
    button_split.pack()
    button_selectall.pack()
    button_selectnone.pack()
    splitwindow.mainloop()


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
