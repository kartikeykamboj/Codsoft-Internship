import tkinter as t
from tkinter import ttk
import re
class M(t.Toplevel):
 def __init__(s,p,ti,m,mt="info"):
  super().__init__(p)
  s.title(ti)
  s.transient(p)
  s.grab_set()
  s.p=p
  s.r=None
  x=p.winfo_x()
  y=p.winfo_y()
  w=p.winfo_width()
  h=p.winfo_height()
  s.update_idletasks()
  mw=320;mh=160
  sx=x+(w//2)-(mw//2)
  sy=y+(h//2)-(mh//2)
  s.geometry(f"{mw}x{mh}+{sx}+{sy}")
  s.resizable(0,0)
  s.configure(bg="#2d2d2d")
  st=ttk.Style(s)
  st.configure("Msg.TFrame",background="#2d2d2d")
  st.configure("Msg.TLabel",background="#2d2d2d",foreground="#e0e0e0",font=("Segoe UI",10))
  st.configure("Msg.TButton",font=("Segoe UI",10,"bold"),background="#4b5263",foreground="#fff",borderwidth=0,focusthickness=0,relief="flat",padding=[10,5])
  st.map("Msg.TButton",background=[('active','#5c6370')],relief=[('pressed','groove')])
  f=ttk.Frame(s,style="Msg.TFrame",padding=15)
  f.pack(expand=1,fill=t.BOTH)
  l=ttk.Label(f,text=m,style="Msg.TLabel",wraplength=mw-30)
  l.pack(pady=10)
  bf=ttk.Frame(f,style="Msg.TFrame")
  bf.pack(pady=5)
  if mt=="confirm":
   ttk.Button(bf,text="Yes",command=s._y,style="Msg.TButton").pack(side=t.LEFT,padx=5)
   ttk.Button(bf,text="No",command=s._n,style="Msg.TButton").pack(side=t.LEFT,padx=5)
  else:
   ttk.Button(bf,text="OK",command=s._ok,style="Msg.TButton").pack(padx=5)
  s.protocol("WM_DELETE_WINDOW",s._c)
  s.wait_window(s)
 def _ok(s):s.r=1;s.destroy()
 def _y(s):s.r=1;s.destroy()
 def _n(s):s.r=0;s.destroy()
 def _c(s):s.r=0;s.destroy()
 @staticmethod
 def i(p,t,m):return M(p,t,m,"info").r
 @staticmethod
 def w(p,t,m):return M(p,t,m,"warning").r
 @staticmethod
 def y(p,t,m):return M(p,t,m,"confirm").r
class C:
 def __init__(s,r):
  s.r=r
  r.title("Simple Calculator")
  r.geometry("400x600")
  r.resizable(1,1)
  s.ce="";s.rd=0;s.fs=0;s.dk=1
  s.st=ttk.Style(r)
  s.st.theme_use('clam')
  s._w()
  s._cfg("dark")
  r.bind("<F11>",s.fs_t)
  r.bind("<Escape>",s.fs_e)
 def _cfg(s,m):
  if m=='dark':
   bg="#1e1e2e";bf="#1e1e2e";fg="#e0e0e0";fs="#abb2bf";far="#9a9aff";fh="#9a9aff";fsh="#aabbaa";fm="#6a737d";be="#2a2a3e";bc="#3a3a5a";bac="#4a4a6a"
   bop="#5a3a5a";boac="#6a4a6a";beq="#6a9a3a";feq="#1e1e2e";beqa="#7aab4a";bcd="#a03a3a";bcda="#b04a4a";btb="#5a3a5a";btf="#e0e0e0";btba="#6a4a6a"
  else:
   bg="#f0f0f0";bf="#f0f0f0";fg="#333";fs="#555";far="#222";fh="#222";fsh="#444";fm="#888";be="#fff";bc="#e8e8e8";bac="#d0d0d0"
   bop="#d0d0d0";boac="#b0b0b0";beq="#90ee90";feq="#333";beqa="#7fdd7f";bcd="#ff6666";bcda="#ee5555";btb="#d0d0d0";btf="#333";btba="#b0b0b0"
  s.r.configure(bg=bg)
  s.st.configure("TFrame",background=bf)
  s.st.configure("TLabel",background=bf,foreground=fg)
  s.st.configure("Header.TLabel",foreground=fh,background=bf)
  s.st.configure("SubHeader.TLabel",foreground=fsh,background=bf)
  s.st.configure("Expression.TEntry",fieldbackground=be,foreground=fg,insertcolor=fg)
  s.st.configure("Result.TEntry",fieldbackground=be,foreground=far,insertcolor=far)
  s.st.configure("Calc.TButton",background=bc,foreground=fg)
  s.st.map("Calc.TButton",background=[('active',bac)])
  s.st.configure("Operator.TButton",background=bop,foreground=fg)
  s.st.map("Operator.TButton",background=[('active',boac)])
  s.st.configure("Equals.TButton",background=beq,foreground=feq)
  s.st.map("Equals.TButton",background=[('active',beqa)])
  s.st.configure("ClearDel.TButton",background=bcd,foreground="#fff")
  s.st.map("ClearDel.TButton",background=[('active',bcda)])
  s.mbl.configure(foreground=fm,background=bf)
  s.kbl.configure(foreground=fm,background=bf)
  s.ttb.configure(background=btb,foreground=btf)
  s.st.map("ThemeToggle.TButton",background=[('active',btba)])
  s.ttb.config(text="Light Mode" if s.dk else "Dark Mode")
  s.st.configure("Expression.TEntry",font=("Segoe UI",36))
  s.st.configure("Result.TEntry",font=("Segoe UI",72,"bold"))
  s.st.configure("Header.TLabel",font=("Segoe UI",64,"bold"))
  s.st.configure("SubHeader.TLabel",font=("Segoe UI",36,"italic"))
  s.st.configure("Calc.TButton",font=("Segoe UI",36,"bold"))
  s.st.configure("Operator.TButton",font=("Segoe UI",36,"bold"))
  s.st.configure("Equals.TButton",font=("Segoe UI",36,"bold"))
  s.st.configure("ClearDel.TButton",font=("Segoe UI",36,"bold"))
 def _w(s):
  hf=ttk.Frame(s.r,padding="15 10");hf.pack(fill=t.X)
  hf.grid_columnconfigure(0,weight=1)
  hf.grid_columnconfigure(1,weight=3)
  hf.grid_columnconfigure(2,weight=1)
  s.mbl=ttk.Label(hf,text="Made by:",font=("Segoe UI",10))
  s.mbl.grid(row=0,column=0,sticky="nw",padx=5,pady=(0,0))
  s.kbl=ttk.Label(hf,text="Kartikey Kamboj",font=("Segoe UI",11,"bold"))
  s.kbl.grid(row=1,column=0,sticky="nw",padx=5,pady=(0,5))
  ttk.Label(hf,text="Simple Calculator",style="Header.TLabel").grid(row=0,column=0,columnspan=3,pady=(0,0),sticky="n")
  ttk.Label(hf,text="Codsoft Task 2",style="SubHeader.TLabel").grid(row=1,column=0,columnspan=3,pady=(0,10),sticky="n")
  s.ttb=ttk.Button(hf,text="Light Mode",command=s.theme,style="ThemeToggle.TButton")
  s.ttb.grid(row=0,column=2,sticky="ne",padx=5,pady=5)
  s.st.configure("ThemeToggle.TButton",font=("Segoe UI",10,"bold"),borderwidth=0,focusthickness=0,relief="flat",padding=[5,3])
  df=ttk.Frame(s.r,padding="10 5")
  df.pack(fill=t.X)
  s.evar=t.StringVar()
  s.rvar=t.StringVar()
  s.ee=ttk.Entry(df,textvariable=s.evar,justify='right',state='readonly',style="Expression.TEntry")
  s.ee.pack(fill=t.X,pady=(0,2),ipady=5)
  s.re=ttk.Entry(df,textvariable=s.rvar,justify='right',state='readonly',style="Result.TEntry")
  s.re.pack(fill=t.X,pady=(2,0),ipady=10)
  s.evar.set("")
  s.rvar.set("0")
  s.bf=ttk.Frame(s.r,padding=10)
  s.bf.pack(fill=t.BOTH,expand=1)
  bs=[('C',1,'ClearDel.TButton'),('DEL',1,'ClearDel.TButton'),('/',1,'Operator.TButton'),('*',1,'Operator.TButton'),('7',1,'Calc.TButton'),('8',1,'Calc.TButton'),('9',1,'Calc.TButton'),('-',1,'Operator.TButton'),('4',1,'Calc.TButton'),('5',1,'Calc.TButton'),('6',1,'Calc.TButton'),('+',1,'Operator.TButton'),('1',1,'Calc.TButton'),('2',1,'Calc.TButton'),('3',1,'Calc.TButton'),('=',2,'Equals.TButton'),('0',2,'Calc.TButton'),('.',1,'Calc.TButton')]
  row=col=0
  for txt,cs,sty in bs:
   b=ttk.Button(s.bf,text=txt,style=sty,command=lambda t=txt:s.btn(t))
   if txt=='=':
    b.grid(row=row,column=col,columnspan=cs,sticky="nsew",padx=5,pady=5,rowspan=2)
    col+=cs
   elif txt=='0':
    b.grid(row=row,column=col,columnspan=cs,sticky="nsew",padx=5,pady=5)
    col+=cs
   else:
    b.grid(row=row,column=col,columnspan=cs,sticky="nsew",padx=5,pady=5)
    col+=cs
   if col>=4:col=0;row+=1
  for i in range(4):s.bf.grid_columnconfigure(i,weight=1)
  for i in range(5):s.bf.grid_rowconfigure(i,weight=1)
 def fs_t(s,e=None):s.fs=not s.fs;s.r.attributes("-fullscreen",s.fs)
 def fs_e(s,e=None):
  if s.fs:s.fs=0;s.r.attributes("-fullscreen",0)
 def theme(s):
  s.dk=not s.dk
  s._cfg('dark' if s.dk else 'light')
 def btn(s,c):
  if c=='C':
   s.ce=""
   s.rvar.set("0")
   s.evar.set("")
   s.rd=0
  elif c=='DEL':
   if s.rd:
    s.ce="";s.rvar.set("0");s.evar.set("");s.rd=0
   else:
    s.ce=s.ce[:-1];s.evar.set(s.ce)
    if not s.ce:s.rvar.set("0")
  elif c=='=':
   s.calc()
  else:
   if s.rd and c not in ['+','-','*','/']:
    s.ce=c;s.rd=0
   elif s.rd and c in ['+','-','*','/']:
    s.ce=s.rvar.get()+c;s.rd=0
   else:
    if s.ce and s.ce[-1] in ['+','-','*','/'] and c in ['+','-','*','/']:
     s.ce=s.ce[:-1]+c
    elif c=='.' and s.ce and s.ce[-1]=='.':
     pass
    elif c=='.' and not s.ce:
     s.ce="0."
    elif c=='.' and s.ce and re.search(r'\d+\.$',s.ce):
     pass
    else:
     s.ce+=c
   s.evar.set(s.ce)
   s.rvar.set("")
 def calc(s):
  try:
   ce=s.ce.strip()
   if not ce:
    s.rvar.set("0")
    s.evar.set("")
    s.ce=""
    s.rd=1
    return
   if ce and ce[-1] in ['+','-','*','/','.']:
    ce=ce[:-1]
   se=re.sub(r'[^-+*/.0-9]','',ce)
   r=str(eval(se))
   s.rvar.set(r)
   s.evar.set(s.ce+" =")
   s.ce=r
   s.rd=1
  except ZeroDivisionError:
   M.w(s.r,"Error","Cannot divide by zero!")
   s.rvar.set("Error");s.evar.set("");s.ce="";s.rd=1
  except SyntaxError:
   M.w(s.r,"Error","Invalid expression!")
   s.rvar.set("Error");s.evar.set("");s.ce="";s.rd=1
  except Exception as e:
   M.i(s.r,"Error",f"An unexpected error occurred: {e}")
   s.rvar.set("Error");s.evar.set("");s.ce="";s.rd=1
if __name__=="__main__":
 r=t.Tk()
 a=C(r)
 r.mainloop()
