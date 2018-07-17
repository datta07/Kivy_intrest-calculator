from intrest1 import *
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
import android
import time

i=time.strftime('%d')
j=time.strftime('%m')
k=time.strftime('%Y')
p=time.strftime('%d-%m-%Y')

r=0
class intrestapp(GridLayout):
    def app(self,amount,date,month,year):
          global p,r
          android.vibrate(0.05)
          if  (self.item.state=='down'):
                r=0.03
          elif  (self.itema.state=='down'):
                r=0.04
                
          try:
               self.display1.text=time1(p,date,month,year,1)
               t=time1(p,date,month,year,2)
               self.ka.text=str(int(t))+' months'
               self.kb.text=str(int(t)+1)+' months'
               if self.ka.state=='down':
                   t=int(t)
               elif self.kb.state=='down':
                   t=int(t)+1
          except Exception:
                self.display1.text='Error'

          try:
               if  (self.item1.state=='down'):
                     self.display2.text=intrest(amount,t,r)
               else:
                     self.display2.text=intrest1(amount,t,r)
                 
              
          except Exception:
                self.display2.text='Error'
    def create(self):
          popu().open()
    def create1(self):
          popu1().open()
    def date(self):
           self.a1.text=i
           self.a2.text=j
           self.a3.text=k
    def clear(self):
           self.a1.text=''
           self.a2.text=''
           self.a3.text=''

class popu(Popup):
           def date(self,no):
                   global i,j,k
                   if (no==1):
                        return i
                   if (no==2):
                        return j
                   return k
                   
           def ok(self):
                  global i,j,k,p
                  i=self.i.text
                  j=self.j.text
                  k=self.k.text
                  p=i+'-'+j+'-'+k
                  self.dismiss()                 
                  
 
class popu1(Popup):
           def var(self):
                  global r
                  return str(r*100)
           def ok(self):
                  global r
                  r=float(self.i.text)
                  r=r*0.01
                  self.dismiss()          
         
         
class ramu(App):
    def build(self):
        return intrestapp()
    def on_pause(self):
        return True

ramu().run()