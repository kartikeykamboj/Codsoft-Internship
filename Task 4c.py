import tkinter as t
from tkinter import ttk
import random
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
  else:ttk.Button(bf,text="OK",command=s._ok,style="Msg.TButton").pack(padx=5)
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
class R:
 def __init__(s,r):
  s.r=r
  r.title("Rock-Paper-Scissors")
  r.geometry("600x650")
  r.resizable(1,1)
  s.us=0
  s.cs=0
  s.c=["Rock","Paper","Scissors"]
  s.dk=1
  s.fs=0
  s.st=ttk.Style(r)
  s.st.theme_use('clam')
  s.ucv=t.StringVar(value="Your Choice: -")
  s.ccv=t.StringVar(value="Computer's Choice: -")
  s.rv=t.StringVar(value="Result: -")
  s.sv=t.StringVar(value=f"Score: You {s.us} - {s.cs} Computer")
  s._w()
  s._cfg("dark")
  r.bind("<F11>",s.fs_t)
  r.bind("<Escape>",s.fs_e)
 def _cfg(s,m):
  if m=='dark':
   bg="#1a1a2e";bf="#1a1a2e";fg="#e0e0e0";fs="#abb2bf";hf="#0f4c75";shf="#3282b8";mf="#6a737d"
   bb="#3282b8";bab="#0f4c75";bfg="#fff";gbg="#4a4a6a";gba="#5c5c7c";gfg="#fff";tb="#5a3a5a";tf="#e0e0e0";tab="#6a4a6a";rfg="#98c379";sfg="#e0e0e0"
  else:
   bg="#f0f0f0";bf="#f0f0f0";fg="#333";fs="#555";hf="#1a1a1a";shf="#4a4a4a";mf="#777"
   bb="#a0d9f5";bab="#72bcd4";bfg="#333";gbg="#e8e8e8";gba="#d0d0d0";gfg="#333";tb="#d0d0d0";tf="#333";tab="#b0b0b0";rfg="#2e8b57";sfg="#333"
  s.r.configure(bg=bg)
  s.st.configure("TFrame",background=bf)
  s.st.configure("TLabel",background=bf,foreground=fg)
  s.st.configure("Header.TLabel",foreground=hf,background=bf)
  s.st.configure("SubHeader.TLabel",foreground=shf,background=bf)
  s.st.configure("Result.TLabel",foreground=rfg,background=bf)
  s.st.configure("Score.TLabel",foreground=sfg,background=bf)
  s.st.configure("TButton",font=("Segoe UI",10,"bold"),background=bb,foreground=bfg,borderwidth=0,focusthickness=0,relief="flat",padding=[10,5],bordercolor=bb)
  s.st.map("TButton",background=[('active',bab)],foreground=[('active',bfg)])
  s.st.configure("Game.TButton",font=("Segoe UI",14,"bold"),background=gbg,foreground=gfg,borderwidth=0,focusthickness=0,relief="flat",padding=[15,10])
  s.st.map("Game.TButton",background=[('active',gba)])
  s.st.configure("ThemeToggle.TButton",font=("Segoe UI",10,"bold"),borderwidth=0,focusthickness=0,relief="flat",padding=[5,3])
  s.ttb.configure(background=tb,foreground=tf)
  s.st.map("ThemeToggle.TButton",background=[('active',tab)])
  s.ttb.config(text="Light Mode" if s.dk else "Dark Mode")
  s.mbl.configure(foreground=mf,background=bf)
  s.kbl.configure(foreground=mf,background=bf)
 def _w(s):
  hf=ttk.Frame(s.r,padding="15 10")
  hf.pack(fill=t.X)
  hf.grid_columnconfigure(0,weight=1)
  hf.grid_columnconfigure(1,weight=3)
  hf.grid_columnconfigure(2,weight=1)
  s.mbl=ttk.Label(hf,text="Made by:",font=("Segoe UI",9))
  s.mbl.grid(row=0,column=0,sticky="nw",padx=5,pady=(0,0))
  s.kbl=ttk.Label(hf,text="Kartikey Kamboj",font=("Segoe UI",10,"bold"))
  s.kbl.grid(row=1,column=0,sticky="nw",padx=5,pady=(0,5))
  ttk.Label(hf,text="Rock-Paper-Scissors",style="Header.TLabel",font=("Segoe UI",24,"bold")).grid(row=0,column=1,rowspan=2,pady=(0,0),sticky="nsew")
  ttk.Label(hf,text="Codsoft Task 4",style="SubHeader.TLabel",font=("Segoe UI",12,"italic")).grid(row=2,column=1,pady=(0,10),sticky="n")
  s.ttb=ttk.Button(hf,text="Light Mode",command=s.theme,style="ThemeToggle.TButton")
  s.ttb.grid(row=0,column=2,sticky="ne",padx=5,pady=5)
  df=ttk.Frame(s.r,padding="20 15")
  df.pack(fill=t.X,pady=10)
  ttk.Label(df,textvariable=s.ucv,font=("Segoe UI",14)).pack(pady=5)
  ttk.Label(df,textvariable=s.ccv,font=("Segoe UI",14)).pack(pady=5)
  ttk.Label(df,textvariable=s.rv,style="Result.TLabel",font=("Segoe UI",18,"bold")).pack(pady=10)
  ttk.Label(df,textvariable=s.sv,style="Score.TLabel",font=("Segoe UI",16)).pack(pady=5)
  cbf=ttk.Frame(s.r,padding="20 15")
  cbf.pack(pady=10)
  ttk.Button(cbf,text="Rock",command=lambda:s.play("Rock"),style="Game.TButton").grid(row=0,column=0,padx=10,pady=10,sticky="nsew")
  ttk.Button(cbf,text="Paper",command=lambda:s.play("Paper"),style="Game.TButton").grid(row=0,column=1,padx=10,pady=10,sticky="nsew")
  ttk.Button(cbf,text="Scissors",command=lambda:s.play("Scissors"),style="Game.TButton").grid(row=0,column=2,padx=10,pady=10,sticky="nsew")
  for i in range(3):cbf.grid_columnconfigure(i,weight=1)
  cbf.grid_rowconfigure(0,weight=1)
  ctf=ttk.Frame(s.r,padding="20 15")
  ctf.pack(fill=t.X,pady=10)
  ttk.Button(ctf,text="Reset Scores",command=s.reset,style="TButton").pack(side=t.LEFT,expand=1,padx=10)
  ttk.Button(ctf,text="Play Again",command=s.reset_round,style="TButton").pack(side=t.RIGHT,expand=1,padx=10)
 def play(s,u):
  c=random.choice(s.c)
  s.ucv.set(f"Your Choice: {u}")
  s.ccv.set(f"Computer's Choice: {c}")
  r=s.winner(u,c)
  s.rv.set(f"Result: {r}")
  s.update_score(r)
 def winner(s,u,c):
  if u==c:return "It's a Tie!"
  if(u=="Rock"and c=="Scissors")or(u=="Scissors"and c=="Paper")or(u=="Paper"and c=="Rock"):return "You Win!"
  return "Computer Wins!"
 def update_score(s,r):
  if r=="You Win!":s.us+=1
  elif r=="Computer Wins!":s.cs+=1
  s.sv.set(f"Score: You {s.us} - {s.cs} Computer")
 def reset_round(s):
  s.ucv.set("Your Choice: -")
  s.ccv.set("Computer's Choice: -")
  s.rv.set("Result: -")
 def reset(s):
  if M.y(s.r,"Reset Game","Are you sure you want to reset all scores and start a new game?"):
   s.us=0
   s.cs=0
   s.sv.set(f"Score: You {s.us} - {s.cs} Computer")
   s.reset_round()
   M.i(s.r,"Game Reset","Game has been reset. Good luck!")
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
 a=R(r)
 r.mainloop()
