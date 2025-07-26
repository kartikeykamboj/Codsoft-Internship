import tkinter as t
from tkinter import ttk
import json
import os
from datetime import datetime as d
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
  mw=320
  mh=160
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
class A:
 def __init__(s,r):
  s.r=r
  s.t=[]
  s.f="tasks.json"
  s.fi="All"
  s.so="Creation Date"
  r.title("Codesoft To-Do List")
  r.geometry("850x700")
  r.minsize(750,650)
  r.configure(bg="#1a1a2e")
  st=ttk.Style(r)
  st.theme_use('clam')
  st.configure("TFrame",background="#1a1a2e")
  st.configure("TLabel",background="#1a1a2e",foreground="#e0e0e0",font=("Segoe UI",11))
  st.configure("Header.TLabel",font=("Segoe UI",32,"bold"),foreground="#0f4c75")
  st.configure("SubHeader.TLabel",font=("Segoe UI",14,"italic"),foreground="#3282b8")
  st.configure("TaskLabel.TLabel",font=("Segoe UI",12,"bold"),foreground="#98c379")
  st.configure("TButton",font=("Segoe UI",10,"bold"),background="#3282b8",foreground="#fff",borderwidth=0,focusthickness=0,relief="flat",padding=[10,5],bordercolor="#3282b8")
  st.map("TButton",background=[('active','#0f4c75')],foreground=[('active','#fff')],relief=[('pressed','groove')])
  st.configure("TEntry",fieldbackground="#2e2e4a",foreground="#e0e0e0",insertcolor="#3282b8",font=("Segoe UI",11),borderwidth=1,relief="flat",bordercolor="#3282b8")
  st.configure("TCombobox",fieldbackground="#2e2e4a",background="#3282b8",foreground="#e0e0e0",selectbackground="#0f4c75",selectforeground="#fff",font=("Segoe UI",11),borderwidth=1,relief="flat",bordercolor="#3282b8")
  st.map('TCombobox',fieldbackground=[('readonly','#2e2e4a')],selectbackground=[('readonly','#0f4c75')],selectforeground=[('readonly','#fff')])
  st.map('TCombobox',background=[('active','#0f4c75')],foreground=[('active','#fff')])
  st.configure("Treeview",background="#2e2e4a",foreground="#e0e0e0",fieldbackground="#2e2e4a",font=("Segoe UI",11),borderwidth=0,rowheight=30)
  st.configure("Treeview.Heading",font=("Segoe UI",12,"bold"),background="#0f4c75",foreground="#fff",relief="flat")
  st.map("Treeview",background=[('selected','#3282b8')],foreground=[('selected','#fff')])
  s._tags()
  st.configure("Vertical.TScrollbar",background="#0f4c75",troughcolor="#1a1a2e",bordercolor="#0f4c75",arrowcolor="#e0e0e0",relief="flat")
  st.map("Vertical.TScrollbar",background=[('active','#3282b8')])
  st.configure("TCheckbutton",background="#2e2e4a",foreground="#e0e0e0",font=("Segoe UI",11))
  st.map("TCheckbutton",background=[('active','#2e2e4a')])
  s._w()
  s.load()
  s.afs()
  s.updt()
 def _tags(s):
  ttk.Style().configure("completed.Treeview",foreground="#7f8c8d",font=("Segoe UI",11,"overstrike"))
  ttk.Style().configure("high_priority.Treeview",foreground="#e74c3c",font=("Segoe UI",11,"bold"))
  ttk.Style().configure("medium_priority.Treeview",foreground="#f39c12")
  ttk.Style().configure("low_priority.Treeview",foreground="#2ecc71")
  ttk.Style().configure("overdue.Treeview",foreground="#ff6b6b",font=("Segoe UI",11,"italic","bold"))

 def _w(s):
  s.c=t.Canvas(s.r,bg="#1a1a2e",highlightthickness=0)
  s.sb=ttk.Scrollbar(s.r,orient="vertical",command=s.c.yview,style="Vertical.TScrollbar")
  s.sf=ttk.Frame(s.c,style="TFrame")
  s.cf=s.c.create_window((0,0),window=s.sf,anchor="nw")
  s.c.configure(yscrollcommand=s.sb.set)
  s.c.pack(side="left",fill="both",expand=1)
  s.sb.pack(side="right",fill="y")
  s.c.bind("<Configure>",s._cr)
  s.sf.bind("<Configure>",s._fc)
  s.c.bind_all("<MouseWheel>",s._mw)
  hf=ttk.Frame(s.sf,padding="25 20")
  hf.pack(fill=t.X)
  hf.grid_columnconfigure(0,weight=1)
  hf.grid_columnconfigure(1,weight=3)
  hf.grid_columnconfigure(2,weight=1)
  ttk.Label(hf,text="Made by:",font=("Segoe UI",9),foreground="#6a737d").grid(row=0,column=0,sticky="nw",padx=10,pady=(0,0))
  ttk.Label(hf,text="Kartikey Kamboj",font=("Segoe UI",10,"bold"),foreground="#6a737d").grid(row=1,column=0,sticky="nw",padx=10,pady=(0,10))
  s.dl=ttk.Label(hf,text="",font=("Segoe UI",9),foreground="#6a737d")
  s.dl.grid(row=0,column=2,sticky="ne",padx=10,pady=(0,0))
  s.tl=ttk.Label(hf,text="",font=("Segoe UI",10,"bold"),foreground="#6a737d")
  s.tl.grid(row=1,column=2,sticky="ne",padx=10,pady=(0,10))
  ttk.Label(hf,text="TaskFlow",style="Header.TLabel").grid(row=2,column=0,columnspan=3,pady=(0,0))
  ttk.Label(hf,text="Your personal productivity companion.",style="SubHeader.TLabel").grid(row=3,column=0,columnspan=3,pady=(0,0))
  ttk.Label(hf,text="Codsoft Internship Task 1",style="TaskLabel.TLabel").grid(row=4,column=0,columnspan=3,pady=(0,15))
  i_f=ttk.Frame(s.sf,padding="20 15")
  i_f.pack(fill=t.X)
  ttk.Label(i_f,text="Task Description:").grid(row=0,column=0,sticky="w",pady=5,padx=5)
  s.te=ttk.Entry(i_f,width=50,style="TEntry")
  s.te.grid(row=0,column=1,columnspan=3,sticky="ew",pady=5,padx=5)
  s.te.bind("<Return>",s.add)
  ttk.Label(i_f,text="Due Date (YYYY-MM-DD):").grid(row=1,column=0,sticky="w",pady=5,padx=5)
  s.de=ttk.Entry(i_f,width=20,style="TEntry")
  s.de.grid(row=1,column=1,sticky="ew",pady=5,padx=5)
  ttk.Label(i_f,text="Priority:").grid(row=1,column=2,sticky="w",pady=5,padx=5)
  s.popts=["Low","Medium","High"]
  s.pc=ttk.Combobox(i_f,values=s.popts,state="readonly",style="TCombobox")
  s.pc.set("Low")
  s.pc.grid(row=1,column=3,sticky="ew",pady=5,padx=5)
  i_f.grid_columnconfigure(1,weight=1)
  i_f.grid_columnconfigure(3,weight=1)
  ttk.Button(i_f,text="Add Task",command=s.add,style="TButton").grid(row=2,column=0,columnspan=4,pady=15,sticky="ew",padx=5)
  lf=ttk.Frame(s.sf,padding="20 15")
  lf.pack(fill=t.BOTH,expand=1)
  cols=("#1","#2","#3","#4")
  s.tt=ttk.Treeview(lf,columns=cols,show="headings",style="Treeview")
  s.tt.heading("#1",text="Task",anchor=t.W)
  s.tt.heading("#2",text="Due Date",anchor=t.W)
  s.tt.heading("#3",text="Priority",anchor=t.W)
  s.tt.heading("#4",text="Status",anchor=t.W)
  s.tt.column("#1",width=350,minwidth=250,stretch=t.YES)
  s.tt.column("#2",width=120,minwidth=100,stretch=t.NO)
  s.tt.column("#3",width=90,minwidth=70,stretch=t.NO)
  s.tt.column("#4",width=90,minwidth=70,stretch=t.NO)
  s.tt.pack(side=t.LEFT,fill=t.BOTH,expand=1)
  ttsb=ttk.Scrollbar(lf,orient=t.VERTICAL,command=s.tt.yview,style="Vertical.TScrollbar")
  ttsb.pack(side=t.RIGHT,fill=t.Y)
  s.tt.config(yscrollcommand=ttsb.set)
  cf=ttk.Frame(s.sf,padding="20 15")
  cf.pack(fill=t.X)
  ttk.Button(cf,text="Edit Task",command=s.edit,style="TButton").pack(side=t.LEFT,expand=1,padx=7)
  ttk.Button(cf,text="Toggle Done",command=s.tg,style="TButton").pack(side=t.LEFT,expand=1,padx=7)
  ttk.Button(cf,text="Delete Task",command=s.rem,style="TButton").pack(side=t.LEFT,expand=1,padx=7)
  ttk.Button(cf,text="Clear Completed",command=s.clr,style="TButton").pack(side=t.LEFT,expand=1,padx=7)
  fsf=ttk.Frame(s.sf,padding="20 15")
  fsf.pack(fill=t.X)
  ttk.Label(fsf,text="Filter By:").pack(side=t.LEFT,padx=5)
  s.fopts=["All","Active","Completed","Overdue"]
  s.fcb=ttk.Combobox(fsf,values=s.fopts,state="readonly",style="TCombobox")
  s.fcb.set(s.fi)
  s.fcb.bind("<<ComboboxSelected>>",s.afs)
  s.fcb.pack(side=t.LEFT,padx=5,expand=1,fill=t.X)
  ttk.Label(fsf,text="Sort By:").pack(side=t.LEFT,padx=5)
  s.sopts=["Creation Date","Due Date","Priority"]
  s.scb=ttk.Combobox(fsf,values=s.sopts,state="readonly",style="TCombobox")
  s.scb.set(s.so)
  s.scb.bind("<<ComboboxSelected>>",s.afs)
  s.scb.pack(side=t.LEFT,padx=5,expand=1,fill=t.X)
 def _cr(s,e):s.c.itemconfig(s.cf,width=e.width);s.c.configure(scrollregion=s.c.bbox("all"))
 def _fc(s,e):s.c.configure(scrollregion=s.c.bbox("all"))
 def _mw(s,e):s.c.yview_scroll(int(-1*(e.delta/120)),"units")
 def updt(s):
  now=d.now()
  s.dl.config(text=now.strftime("%Y-%m-%d"))
  s.tl.config(text=now.strftime("%H:%M:%S"))
  s.r.after(1000,s.updt)
 def utv(s,ts):
  for i in s.tt.get_children():s.tt.delete(i)
  for tk in ts:
   st="Done" if tk['completed'] else "Active"
   tg=[]
   if tk['completed']:
    tg.append("completed")
   else:
    if tk['priority']=="High":tg.append("high_priority")
    elif tk['priority']=="Medium":tg.append("medium_priority")
    elif tk['priority']=="Low":tg.append("low_priority")
    if tk['due_date']:
     try:
      ddt=d.strptime(tk['due_date'],"%Y-%m-%d").date()
      if not tk['completed'] and ddt<d.now().date():tg.append("overdue")
     except:pass
   s.tt.insert("",t.END,iid=tk['id'],values=(tk['text'],tk['due_date'],tk['priority'],st),tags=tuple(tg))
 def add(s,e=None):
  tt=s.te.get().strip()
  dd=s.de.get().strip()
  pr=s.pc.get()
  if not tt:
   M.w(s.r,"Input Error","Task description cannot be empty.")
   return
  if dd and not s._vd(dd):
   M.w(s.r,"Input Error","Due date must be in YYYY-MM-DD format.")
   return
  nt={"id":str(uuid.uuid4()),"text":tt,"completed":0,"due_date":dd,"priority":pr}
  s.t.append(nt)
  s.afs()
  s.te.delete(0,t.END)
  s.de.delete(0,t.END)
  s.pc.set("Low")
  s.save()
 def edit(s):
  si=s.tt.focus()
  if not si:
   M.w(s.r,"Selection Error","You must select a task to edit.")
   return
  tk=next((k for k in s.t if k['id']==si),None)
  if not tk:
   M.w(s.r,"Error","Selected task not found.")
   return
  ew=t.Toplevel(s.r)
  ew.title("Edit Task")
  ew.transient(s.r)
  ew.grab_set()
  ew.configure(bg="#2d2d2d")
  ew.geometry("400x280")
  s.r.update_idletasks()
  x=s.r.winfo_x()+(s.r.winfo_width()//2)-(ew.winfo_width()//2)
  y=s.r.winfo_y()+(s.r.winfo_height()//2)-(ew.winfo_height()//2)
  ew.geometry(f"+{x}+{y}")
  ef=ttk.Frame(ew,padding=20,style="TFrame")
  ef.pack(fill=t.BOTH,expand=1)
  ttk.Label(ef,text="Task Description:").grid(row=0,column=0,sticky="w",pady=5,padx=5)
  ete=ttk.Entry(ef,width=40,style="TEntry")
  ete.insert(0,tk['text'])
  ete.grid(row=0,column=1,sticky="ew",pady=5,padx=5)
  ttk.Label(ef,text="Due Date (YYYY-MM-DD):").grid(row=1,column=0,sticky="w",pady=5,padx=5)
  ede=ttk.Entry(ef,width=20,style="TEntry")
  ede.insert(0,tk['due_date'])
  ede.grid(row=1,column=1,sticky="ew",pady=5,padx=5)
  ttk.Label(ef,text="Priority:").grid(row=2,column=0,sticky="w",pady=5,padx=5)
  epc=ttk.Combobox(ef,values=s.popts,state="readonly",style="TCombobox")
  epc.set(tk['priority'])
  epc.grid(row=2,column=1,sticky="ew",pady=5,padx=5)
  ttk.Label(ef,text="Completed:").grid(row=3,column=0,sticky="w",pady=5,padx=5)
  iv=t.BooleanVar(value=tk['completed'])
  ecc=ttk.Checkbutton(ef,text="",variable=iv,style="TCheckbutton")
  ecc.grid(row=3,column=1,sticky="w",pady=5,padx=5)
  ef.grid_columnconfigure(1,weight=1)
  def sv():
   nt=ete.get().strip()
   nd=ede.get().strip()
   np=epc.get()
   nc=iv.get()
   if not nt:
    M.w(ew,"Input Error","Task description cannot be empty.");return
   if nd and not s._vd(nd):
    M.w(ew,"Input Error","Due date must be in YYYY-MM-DD format.");return
   tk['text']=nt;tk['due_date']=nd;tk['priority']=np;tk['completed']=nc
   s.afs()
   s.save()
   ew.destroy()
  ttk.Button(ef,text="Save Changes",command=sv,style="TButton").grid(row=4,column=0,columnspan=2,pady=15,sticky="ew",padx=5)
  ew.protocol("WM_DELETE_WINDOW",ew.destroy)
  ew.wait_window(ew)
 def tg(s):
  si=s.tt.focus()
  if not si:
   M.w(s.r,"Selection Error","You must select a task to toggle its status.")
   return
  for k in s.t:
   if k['id']==si:k['completed']=not k['completed'];break
  s.afs()
  s.save()
 def rem(s):
  si=s.tt.focus()
  if not si:
   M.w(s.r,"Selection Error","You must select a task to delete.");return
  if M.y(s.r,"Confirm Delete","Are you sure you want to delete this task?"):
   s.t=[k for k in s.t if k['id']!=si]
   s.afs()
   s.save()
 def clr(s):
  if M.y(s.r,"Confirm Clear","Are you sure you want to clear all completed tasks?"):
   s.t=[k for k in s.t if not k['completed']]
   s.afs()
   s.save()
 def afs(s,e=None):
  s.fi=s.fcb.get()
  s.so=s.scb.get()
  ft=[]
  for tk in s.t:
   od=0
   if tk['due_date'] and not tk['completed']:
    try:
     dd=d.strptime(tk['due_date'],"%Y-%m-%d").date()
     if dd<d.now().date():od=1
    except:pass
   if s.fi=="All":ft.append(tk)
   elif s.fi=="Active" and not tk['completed']:ft.append(tk)
   elif s.fi=="Completed" and tk['completed']:ft.append(tk)
   elif s.fi=="Overdue" and od:ft.append(tk)
  if s.so=="Due Date":
   ft.sort(key=lambda t:(t['due_date']=='',d.strptime(t['due_date'],'%Y-%m-%d') if t['due_date'] else d.max))
  elif s.so=="Priority":
   po={"High":0,"Medium":1,"Low":2}
   ft.sort(key=lambda t:po.get(t['priority'],99))
  s.utv(ft)
 def load(s):
  if os.path.exists(s.f):
   try:
    with open(s.f,'r') as f:s.t=json.load(f)
    for tk in s.t:
     if 'id' not in tk:tk['id']=str(uuid.uuid4())
     if 'due_date' not in tk:tk['due_date']=""
     if 'priority' not in tk:tk['priority']="Low"
    s.afs()
   except:(s.t.clear())
 def save(s):
  try:
   with open(s.f,'w') as f:json.dump(s.t,f,indent=4)
  except:pass
 def _vd(s,ds):
  if not ds:return 1
  try:d.strptime(ds,"%Y-%m-%d");return 1
  except:return 0
if __name__=="__main__":
 r=t.Tk()
 a=A(r)
 r.mainloop()
