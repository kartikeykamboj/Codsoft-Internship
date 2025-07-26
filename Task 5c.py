import tkinter as t
from tkinter import ttk
import json
import os
import uuid
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
  r.title("Codsoft Contact Book")
  r.geometry("800x700")
  r.resizable(1,1)
  s.c=[]
  s.f="contacts.json"
  s.dk=1
  s.fs=0
  s.st=ttk.Style(r)
  s.st.theme_use('clam')
  s.sq=t.StringVar()
  s._w()
  s._cfg("dark")
  s.load()
  s.utv(s.c)
  r.bind("<F11>",s.fs_t)
  r.bind("<Escape>",s.fs_e)
 def _cfg(s,m):
  if m=='dark':
   bg="#1e1e2e";bf="#28283a";fg="#e0e0e0";fs="#abb2bf";hf="#FFD700";shf="#FFBF00";mf="#6a737d"
   be="#2a2a3e";bb="#4682B4";bab="#36648B";bfgg="#fff";tvbg="#2e2e4a";tvfg="#e0e0e0";tvsbg="#5F9EA0";tvsfg="#fff"
   tvhbg="#0f4c75";tvhfg="#fff";sbbg="#0f4c75";sbtrbg="#1a1a2e";sbarfg="#e0e0e0";tb="#5a3a5a";tf="#e0e0e0";tab="#6a4a6a"
  else:
   bg="#FFFACD";bf="#F0E68C";fg="#000";fs="#333";hf="#000";shf="#333";mf="#555"
   be="#fff";bb="#FFD700";bab="#DAA520";bfgg="#000";tvbg="#fff";tvfg="#000";tvsbg="#FFBF00";tvsfg="#000";tvhbg="#FFD700";tvhfg="#000"
   sbbg="#DAA520";sbtrbg="#FFFACD";sbarfg="#000";tb="#FFD700";tf="#000";tab="#DAA520"
  s.r.configure(bg=bg)
  s.canvas.configure(bg=bg)
  s.scrollable_frame.configure(style="TFrame")
  s.st.configure("TFrame",background=bf)
  s.st.configure("TLabel",background=bf,foreground=fg)
  s.st.configure("Header.TLabel",foreground=hf,background=bf)
  s.st.configure("SubHeader.TLabel",foreground=shf,background=bf)
  s.st.configure("TEntry",fieldbackground=be,foreground=fg,insertcolor=fg,font=("Segoe UI",11),borderwidth=1,relief="flat",bordercolor=bb)
  s.st.configure("TButton",font=("Segoe UI",10,"bold"),background=bb,foreground=bfgg,borderwidth=0,focusthickness=0,relief="flat",padding=[10,5],bordercolor=bb)
  s.st.map("TButton",background=[('active',bab)],foreground=[('active',bfgg)])
  s.st.configure("Treeview",background=tvbg,foreground=tvfg,fieldbackground=tvbg,font=("Segoe UI",11),borderwidth=0,rowheight=30)
  s.st.configure("Treeview.Heading",font=("Segoe UI",12,"bold"),background=tvhbg,foreground=tvhfg,relief="flat")
  s.st.map("Treeview",background=[('selected',tvsbg)],foreground=[('selected',tvsfg)])
  s.st.configure("Vertical.TScrollbar",background=sbbg,troughcolor=sbtrbg,bordercolor=sbbg,arrowcolor=sbarfg,relief="flat")
  s.st.map("Vertical.TScrollbar",background=[('active',bab)])
  s.st.configure("ThemeToggle.TButton",font=("Segoe UI",10,"bold"),borderwidth=0,focusthickness=0,relief="flat",padding=[5,3])
  s.theme_toggle_button.configure(background=tb,foreground=tf)
  s.st.map("ThemeToggle.TButton",background=[('active',tab)])
  s.theme_toggle_button.config(text="Light Mode" if s.dk else "Dark Mode")
  s.mbl.configure(foreground=mf,background=bf)
  s.kbl.configure(foreground=mf,background=bf)
 def _w(s):
  s.canvas=t.Canvas(s.r,highlightthickness=0)
  s.scrollbar=ttk.Scrollbar(s.r,orient="vertical",command=s.canvas.yview,style="Vertical.TScrollbar")
  s.scrollable_frame=ttk.Frame(s.canvas)
  s.cf=s.canvas.create_window((0,0),window=s.scrollable_frame,anchor="nw")
  s.canvas.configure(yscrollcommand=s.scrollbar.set)
  s.canvas.pack(side="left",fill="both",expand=1)
  s.scrollbar.pack(side="right",fill="y")
  s.canvas.bind("<Configure>",s._cr)
  s.scrollable_frame.bind("<Configure>",s._fc)
  s.canvas.bind_all("<MouseWheel>",s._mw)
  hf=ttk.Frame(s.scrollable_frame,padding="25 20",relief="raised",borderwidth=2)
  hf.pack(fill=t.X,padx=15,pady=10)
  hf.grid_columnconfigure(0,weight=1)
  hf.grid_columnconfigure(1,weight=3)
  hf.grid_columnconfigure(2,weight=1)
  s.mbl=ttk.Label(hf,text="Made by:",font=("Segoe UI",9))
  s.mbl.grid(row=0,column=0,sticky="nw",padx=10,pady=(0,0))
  s.kbl=ttk.Label(hf,text="Kartikey Kamboj",font=("Segoe UI",10,"bold"))
  s.kbl.grid(row=1,column=0,sticky="nw",padx=10,pady=(0,5))
  ttk.Label(hf,text="Contact Book",style="Header.TLabel",font=("Segoe UI",32,"bold")).grid(row=0,column=1,rowspan=2,pady=(0,0),sticky="nsew")
  ttk.Label(hf,text="Codsoft Task 5",style="SubHeader.TLabel",font=("Segoe UI",14,"italic")).grid(row=2,column=1,pady=(0,10),sticky="n")
  s.theme_toggle_button=ttk.Button(hf,text="Light Mode",command=s.theme,style="ThemeToggle.TButton")
  s.theme_toggle_button.grid(row=0,column=2,sticky="ne",padx=10,pady=5)
  if_=ttk.Frame(s.scrollable_frame,padding="25 20",relief="groove",borderwidth=2)
  if_.pack(fill=t.X,padx=15,pady=10)
  ttk.Label(if_,text="Name:").grid(row=0,column=0,sticky="w",pady=7,padx=10)
  s.ne=ttk.Entry(if_,width=40,style="TEntry")
  s.ne.grid(row=0,column=1,sticky="ew",pady=7,padx=10)
  ttk.Label(if_,text="Phone:").grid(row=1,column=0,sticky="w",pady=7,padx=10)
  s.pe=ttk.Entry(if_,width=40,style="TEntry")
  s.pe.grid(row=1,column=1,sticky="ew",pady=7,padx=10)
  ttk.Label(if_,text="Email:").grid(row=2,column=0,sticky="w",pady=7,padx=10)
  s.ee=ttk.Entry(if_,width=40,style="TEntry")
  s.ee.grid(row=2,column=1,sticky="ew",pady=7,padx=10)
  ttk.Label(if_,text="Address:").grid(row=3,column=0,sticky="w",pady=7,padx=10)
  s.ade=ttk.Entry(if_,width=40,style="TEntry")
  s.ade.grid(row=3,column=1,sticky="ew",pady=7,padx=10)
  if_.grid_columnconfigure(1,weight=1)
  ttk.Button(if_,text="Add Contact",command=s.addc,style="TButton").grid(row=4,column=0,columnspan=2,pady=20,sticky="ew",padx=10)
  sf=ttk.Frame(s.scrollable_frame,padding="20 15",relief="ridge",borderwidth=2)
  sf.pack(fill=t.X,padx=15,pady=10)
  ttk.Label(sf,text="Search:").pack(side=t.LEFT,padx=10,pady=5)
  s.se=ttk.Entry(sf,textvariable=s.sq,width=40,style="TEntry")
  s.se.pack(side=t.LEFT,fill=t.X,expand=1,padx=10,pady=5)
  s.se.bind("<KeyRelease>",s.search)
  lf=ttk.Frame(s.scrollable_frame,padding="20 15",relief="sunken",borderwidth=2)
  lf.pack(fill=t.BOTH,expand=1,padx=15,pady=10)
  cols=("#1","#2","#3","#4","#5")
  s.ct=ttk.Treeview(lf,columns=cols,show="headings",style="Treeview")
  s.ct.heading("#1",text="Name",anchor=t.W)
  s.ct.heading("#2",text="Phone",anchor=t.W)
  s.ct.heading("#3",text="Email",anchor=t.W)
  s.ct.heading("#4",text="Address",anchor=t.W)
  s.ct.heading("#5",text="ID",anchor=t.W)
  s.ct.column("#1",width=150,minwidth=100,stretch=t.YES)
  s.ct.column("#2",width=120,minwidth=100,stretch=t.NO)
  s.ct.column("#3",width=150,minwidth=100,stretch=t.YES)
  s.ct.column("#4",width=200,minwidth=150,stretch=t.YES)
  s.ct.column("#5",width=0,minwidth=0,stretch=t.NO)
  s.ct.pack(side=t.LEFT,fill=t.BOTH,expand=1)
  ttsb=ttk.Scrollbar(lf,orient=t.VERTICAL,command=s.ct.yview,style="Vertical.TScrollbar")
  ttsb.pack(side=t.RIGHT,fill=t.Y)
  s.ct.config(yscrollcommand=ttsb.set)
  cf=ttk.Frame(s.scrollable_frame,padding="20 15",relief="raised",borderwidth=2)
  cf.pack(fill=t.X,pady=10,padx=15)
  ttk.Button(cf,text="Edit Contact",command=s.edit,style="TButton").pack(side=t.LEFT,expand=1,padx=10)
  ttk.Button(cf,text="Delete Contact",command=s.delete,style="TButton").pack(side=t.LEFT,expand=1,padx=10)
 def _cr(s,e):
  s.canvas.itemconfig(s.cf,width=e.width)
  s.canvas.configure(scrollregion=s.canvas.bbox("all"))
 def _fc(s,e):
  s.canvas.configure(scrollregion=s.canvas.bbox("all"))
 def _mw(s,e):
  s.canvas.yview_scroll(int(-1*(e.delta/120)),"units")
 def addc(s):
  n=s.ne.get().strip()
  p=s.pe.get().strip()
  e=s.ee.get().strip()
  a=s.ade.get().strip()
  if not n or not p:
   M.w(s.r,"Input Error","Name and Phone Number are required.")
   return
  nc={"id":str(uuid.uuid4()),"name":n,"phone":p,"email":e,"address":a}
  s.c.append(nc)
  s.utv(s.c)
  s.save()
  s.ne.delete(0,t.END)
  s.pe.delete(0,t.END)
  s.ee.delete(0,t.END)
  s.ade.delete(0,t.END)
  M.i(s.r,"Success","Contact added successfully!")
 def edit(s):
  si=s.ct.focus()
  if not si:
   M.w(s.r,"Selection Error","You must select a contact to edit.")
   return
  sc=next((x for x in s.c if x['id']==si),None)
  if not sc:
   M.w(s.r,"Error","Selected contact not found.")
   return
  ew=t.Toplevel(s.r)
  ew.title("Edit Contact")
  ew.transient(s.r)
  ew.grab_set()
  ew.configure(bg="#2d2d2d")
  ew.geometry("450x350")
  s.r.update_idletasks()
  x=s.r.winfo_x()+(s.r.winfo_width()//2)-(ew.winfo_width()//2)
  y=s.r.winfo_y()+(s.r.winfo_height()//2)-(ew.winfo_height()//2)
  ew.geometry(f"+{x}+{y}")
  ef=ttk.Frame(ew,padding=20,style="TFrame")
  ef.pack(fill=t.BOTH,expand=1)
  ttk.Label(ef,text="Name:").grid(row=0,column=0,sticky="w",pady=5,padx=5)
  ne=ttk.Entry(ef,width=40,style="TEntry")
  ne.insert(0,sc['name'])
  ne.grid(row=0,column=1,sticky="ew",pady=5,padx=5)
  ttk.Label(ef,text="Phone:").grid(row=1,column=0,sticky="w",pady=5,padx=5)
  pe=ttk.Entry(ef,width=40,style="TEntry")
  pe.insert(0,sc['phone'])
  pe.grid(row=1,column=1,sticky="ew",pady=5,padx=5)
  ttk.Label(ef,text="Email:").grid(row=2,column=0,sticky="w",pady=5,padx=5)
  ee=ttk.Entry(ef,width=40,style="TEntry")
  ee.insert(0,sc['email'])
  ee.grid(row=2,column=1,sticky="ew",pady=5,padx=5)
  ttk.Label(ef,text="Address:").grid(row=3,column=0,sticky="w",pady=5,padx=5)
  ade=ttk.Entry(ef,width=40,style="TEntry")
  ade.insert(0,sc['address'])
  ade.grid(row=3,column=1,sticky="ew",pady=5,padx=5)
  ef.grid_columnconfigure(1,weight=1)
  def sv():
   nn=ne.get().strip()
   np=pe.get().strip()
   ne_=ee.get().strip()
   na=ade.get().strip()
   if not nn or not np:
    M.w(ew,"Input Error","Name and Phone Number are required.")
    return
   sc['name']=nn
   sc['phone']=np
   sc['email']=ne_
   sc['address']=na
   s.utv(s.c)
   s.save()
   ew.destroy()
   M.i(s.r,"Success","Contact updated successfully!")
  ttk.Button(ef,text="Save Changes",command=sv,style="TButton").grid(row=4,column=0,columnspan=2,pady=15,sticky="ew",padx=5)
  ew.protocol("WM_DELETE_WINDOW",ew.destroy)
  ew.wait_window(ew)
 def delete(s):
  si=s.ct.focus()
  if not si:
   M.w(s.r,"Selection Error","You must select a contact to delete.")
   return
  if M.y(s.r,"Confirm Delete","Are you sure you want to delete this contact?"):
   s.c=[x for x in s.c if x['id']!=si]
   s.utv(s.c)
   s.save()
   M.i(s.r,"Success","Contact deleted successfully!")
 def search(s,e=None):
  q=s.sq.get().strip().lower()
  if not q:
   s.utv(s.c)
   return
  f=[]
  for x in s.c:
   if q in x['name'].lower() or q in x['phone'].lower():f.append(x)
  s.utv(f)
 def utv(s,cl):
  for i in s.ct.get_children():s.ct.delete(i)
  for x in cl:s.ct.insert("",t.END,iid=x['id'],values=(x['name'],x['phone'],x['email'],x['address'],x['id']))
 def load(s):
  if os.path.exists(s.f):
   try:
    with open(s.f,'r')as f:s.c=json.load(f)
    for x in s.c:
     if 'id' not in x:x['id']=str(uuid.uuid4())
   except:
    s.c=[]
 def save(s):
  try:
   with open(s.f,'w')as f:json.dump(s.c,f,indent=4)
  except:pass
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
 a=C(r)
 r.mainloop()
