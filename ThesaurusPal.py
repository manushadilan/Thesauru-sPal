from tkinter import Tk, Text, BOTH, W, N, E, S
from tkinter.ttk import Frame, Button, Label, Style
import pyperclip
import requests
import json

#-------------------------------------------------------
#Thesaurus Pal v.0
#Created by P.D.M.Dilan
#2020/05/06



#-------------------------------------------------------
#GUI credits goes to
#Author: Jan Bodnar
#Website: www.zetcode.com
#-------------------------------------------------------

class MainGUI(Frame):

  def __init__(self):
    super().__init__()
    self.initUI()


  def initUI(self):

    self.master.title("Thesaurus Pal")
    self.pack(fill=BOTH, expand=True)

    self.columnconfigure(1, weight=1)
    self.columnconfigure(3, pad=7)
    self.rowconfigure(3, weight=1)
    self.rowconfigure(5, pad=7)

    lbl = Label(self, text="Thesaurus Pal")
    lbl.grid(sticky=W, pady=4, padx=5)

    self.area = Text(self)
    self.area.grid(row=1, column=0, columnspan=2, rowspan=4, padx=5, sticky=E+W+S+N)

    abtn = Button(self, text="Search",command=self.search_meaning)
    abtn.grid(row=1, column=3)

    cbtn = Button(self, text="Clear" ,command=self.clear_textArea)
    cbtn.grid(row=2, column=3, pady=4)

    obtn = Button(self, text="Close",command=self.quit)
    obtn.grid(row=5, column=3)

  
  def search_meaning(self):
    try:

      selectedText=pyperclip.paste()
      #Dictionary api - https://dictionaryapi.dev/
      url='https://api.dictionaryapi.dev/api/v1/entries/en/%s' % (selectedText)
      jData=requests.get(url)
      data=jData.json()

      result=[]
      for k in data:
          Odata={}
          Odata['meaning']=k.get('meaning')
          Odata['origin']=k.get('origin')
          Odata['phonetic']=k.get('phonetic')
          Odata['word']=k.get('word')
          result.append(Odata)

      for item in result:
        for k,v in item.items():
          if k=='word':
              self.area.insert('1.0','Word : ' +str(v) +'\n')
          elif k=='phonetic':
              self.area.insert('1.0','Phonetic : ' +str(v) +'\n')
          elif k=='origin':
              self.area.insert('1.0','Origin : ' +str(v) +'\n')
          elif k=='meaning':
            for r,s in v.items():
              self.area.insert('1.0',str(r) +str(s) +'\n')
            self.area.insert('1.0','Meaning : \n')
    except :
      self.area.insert('1.0','Something went wrong !\nCheck your internet connection or you have copied a valid word \n')

  def clear_textArea(self):
    self.area.delete('1.0','10.0')

def quit(self):
  self.root.destroy()


def main():
  root = Tk()
  root.geometry("350x300+300+300")
  MainGUI()
  root.mainloop()

if __name__ == '__main__':
  main()