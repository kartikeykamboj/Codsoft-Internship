import tkinter as t
from tkinter import ttk
import random
import string
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
class P:
 def __init__(s,r):
  s.r=r
  r.title("Password Generator")
  r.geometry("500x550")
  r.resizable(1,1)
  s.dk=1
  s.fs=0
  s.st=ttk.Style(r)
  s.st.theme_use('clam')
  s.pl=t.IntVar(value=12)
  s.u=t.BooleanVar(value=1)
  s.lc=t.BooleanVar(value=1)
  s.n=t.BooleanVar(value=1)
  s.sy=t.BooleanVar(value=1)
  s.pw=t.StringVar()
  s._w()
  s._cfg("dark")
  r.bind("<F11>",s.fs_t)
  r.bind("<Escape>",s.fs_e)
 def _cfg(s,m):
  if m=='dark':
   bg="#1a1a2e";bf="#1a1a2e";fg="#e0e0e0";fs="#abb2bf";hf="#0f4c75";shf="#3282b8";mf="#6a737d";be="#2e2e4a";bb="#3282b8";bab="#0f4c75";bfgg="#fff";cbg="#1a1a2e";cfg="#e0e0e0";cibg="#3282b8";ciabg="#0f4c75";tb="#5a3a5a";tf="#e0e0e0";tab="#6a4a6a";pgbg="#2e2e4a";pgfg="#98c379"
  else:
   bg="#f0f0f0";bf="#f0f0f0";fg="#333";fs="#555";hf="#1a1a1a";shf="#4a4a4a";mf="#777";be="#fff";bb="#a0d9f5";bab="#72bcd4";bfgg="#333";cbg="#f0f0f0";cfg="#333";cibg="#a0d9f5";ciabg="#72bcd4";tb="#d0d0d0";tf="#333";tab="#b0b0b0";pgbg="#fff";pgfg="#2e8b57"
  s.r.configure(bg=bg)
  s.st.configure("TFrame",background=bf)
  s.st.configure("TLabel",background=bf,foreground=fg)
  s.st.configure("Header.TLabel",foreground=hf,background=bf)
  s.st.configure("SubHeader.TLabel",foreground=shf,background=bf)
  s.st.configure("TEntry",fieldbackground=be,foreground=fg,insertcolor=fg,font=("Segoe UI",11),borderwidth=1,relief="flat",bordercolor=bb)
  s.st.configure("GeneratedPassword.TEntry",fieldbackground=pgbg,foreground=pgfg,insertcolor=pgfg,font=("Segoe UI",14,"bold"),borderwidth=1,relief="solid",bordercolor=bb)
  s.st.configure("TButton",font=("Segoe UI",10,"bold"),background=bb,foreground=bfgg,borderwidth=0,focusthickness=0,relief="flat",padding=[10,5],bordercolor=bb)
  s.st.map("TButton",background=[('active',bab)],foreground=[('active',bfgg)])
  s.st.configure("TCheckbutton",background=cbg,foreground=cfg,font=("Segoe UI",11),indicatorbackground=cibg)
  s.st.map("TCheckbutton",background=[('active',cbg)],indicatorbackground=[('active',ciabg)])
  s.st.configure("ThemeToggle.TButton",font=("Segoe UI",10,"bold"),borderwidth=0,focusthickness=0,relief="flat",padding=[5,3])
  s.ttb.configure(background=tb,foreground=tf)
  s.st.map("ThemeToggle.TButton",background=[('active',tab)])
  s.ttb.config(text="Light Mode" if s.dk else "Dark Mode")
  s.mbl.configure(foreground=mf,background=bf)
  s.kbl.configure(foreground=mf,background=bf)
 def _w(s):
  hf=ttk.Frame(s.r,padding="15 10");hf.pack(fill=t.X)
  hf.grid_columnconfigure(0,weight=1)
  hf.grid_columnconfigure(1,weight=3)
  hf.grid_columnconfigure(2,weight=1)
  s.mbl=ttk.Label(hf,text="Made by:",font=("Segoe UI",9))
  s.mbl.grid(row=0,column=0,sticky="nw",padx=5,pady=(0,0))
  s.kbl=ttk.Label(hf,text="Kartikey Kamboj",font=("Segoe UI",10,"bold"))
  s.kbl.grid(row=1,column=0,sticky="nw",padx=5,pady=(0,5))
  ttk.Label(hf,text="Password Generator",style="Header.TLabel",font=("Segoe UI",24,"bold")).grid(row=0,column=1,rowspan=2,pady=(0,0),sticky="nsew")
  ttk.Label(hf,text="Codsoft Task 3",style="SubHeader.TLabel",font=("Segoe UI",12,"italic")).grid(row=2,column=1,pady=(0,10),sticky="n")
  s.ttb=ttk.Button(hf,text="Light Mode",command=s.theme,style="ThemeToggle.TButton")
  s.ttb.grid(row=0,column=2,sticky="ne",padx=5,pady=5)
  of=ttk.Frame(s.r,padding="20 15");of.pack(fill=t.X,pady=10)
  ttk.Label(of,text="Password Length:").grid(row=0,column=0,sticky="w",pady=5,padx=5)
  ttk.Spinbox(of,from_=6,to=32,textvariable=s.pl,width=5,style="TEntry").grid(row=0,column=1,sticky="w",pady=5,padx=5)
  ttk.Label(of,text="Include Characters:").grid(row=1,column=0,sticky="nw",pady=10,padx=5)
  cf=ttk.Frame(of);cf.grid(row=1,column=1,columnspan=2,sticky="w",pady=10,padx=5)
  ttk.Checkbutton(cf,text="Uppercase (A-Z)",variable=s.u,style="TCheckbutton").pack(anchor="w")
  ttk.Checkbutton(cf,text="Lowercase (a-z)",variable=s.lc,style="TCheckbutton").pack(anchor="w")
  ttk.Checkbutton(cf,text="Numbers (0-9)",variable=s.n,style="TCheckbutton").pack(anchor="w")
  ttk.Checkbutton(cf,text="Symbols (!@#$)",variable=s.sy,style="TCheckbutton").pack(anchor="w")
  of.grid_columnconfigure(1,weight=1)
  ttk.Button(s.r,text="Generate Password",command=s.gen,style="TButton").pack(pady=15,padx=20,fill=t.X)
  df=ttk.Frame(s.r,padding="15 10");df.pack(fill=t.X,pady=(0,10))
  ttk.Label(df,text="Generated Password:").pack(anchor="w",padx=5,pady=(0,5))
  s.pe=ttk.Entry(df,textvariable=s.pw,state='readonly',style="GeneratedPassword.TEntry")
  s.pe.pack(fill=t.X,padx=5,ipady=5)
  ttk.Button(s.r,text="Copy to Clipboard",command=s.c2c,style="TButton").pack(pady=(0,20),padx=20,fill=t.X)
 def gen(s):
  l=s.pl.get()
  c=""
  if s.u.get():c+=string.ascii_uppercase
  if s.lc.get():c+=string.ascii_lowercase
  if s.n.get():c+=string.digits
  if s.sy.get():c+=string.punctuation
  if not c:
   M.w(s.r,"Input Error","Please select at least one character type.")
   s.pw.set("")
   return
  if l<=0:
   M.w(s.r,"Input Error","Password length must be greater than 0.")
   s.pw.set("")
   return
  p="".join(random.choice(c)for _ in range(l))
  s.pw.set(p)
 def c2c(s):
  p=s.pw.get()
  if p:
   s.r.clipboard_clear()
   s.r.clipboard_append(p)
   M.i(s.r,"Copied!","Password copied to clipboard.")
  else:
   M.w(s.r,"No Password","No password to copy.")
 def fs_t(s,e=None):
  s.fs=not s.fs
  s.r.attributes("-fullscreen",s.fs)
 def fs_e(s,e=None):
  if s.fs:
   s.fs=0
   s.r.attributes("-fullscreen",0)
 def theme(s):
  s.dk=not s.dk
  s._cfg("dark" if s.dk else "light")
if __name__=="__main__":
 r=t.Tk()
 a=P(r)
 r.mainloop()
