import tkinter, tkinter.messagebox
from tkinter import ttk
import tkinter .font as f
from tkinter import filedialog

import json
import os
import subprocess

root = tkinter.Tk()
root.title("Aviutl Auto Setup")
root.geometry('500x500')

Select_version_lavel = tkinter.Label(
    root,
    text="1.ソフトウェアの選択",
    font=(
        "",
        "10",
        "bold"
    )
)
Select_version_lavel.place(x=10,y=10)

Aviutl_exe_ckb = tkinter.BooleanVar()
Aviutl_exe_ckb.set(True)
Aviutl_exe_checkbox = tkinter.Checkbutton(
    root,
    variable=Aviutl_exe_ckb
)
Aviutl_exe_checkbox.place(x=30,y=50)

Aviutl_exe_checkbox = tkinter.Checkbutton(
    root,
    variable=Aviutl_exe_ckb
)
Aviutl_exe_checkbox.place(x=30,y=50)

Aviutl_exe_List = (
    "Aviutl Version1.10",
)

Aviutl_exe_Combobox = ttk.Combobox(
    root,
    values=Aviutl_exe_List,
    height=5,
    width=30,
    state="readonly",
    textvariable= tkinter.StringVar()
)
Aviutl_exe_Combobox.set(Aviutl_exe_List[0])
Aviutl_exe_Combobox.place(x=60,y=50)

Extend_Editor_ckb = tkinter.BooleanVar()
Extend_Editor_ckb.set(True)
Extend_Editor_checkbox = tkinter.Checkbutton(
    root,
    variable=Extend_Editor_ckb
)
Extend_Editor_checkbox.place(x=30,y=80)

Extend_Editor_List = (
    "拡張編集プラグイン Version0.92",
)

Extend_Editor_Combbox = ttk.Combobox(
    root,
    values=Extend_Editor_List,
    height=10,
    width=30,
    state="readonly",
    textvariable=tkinter.StringVar()
)
Extend_Editor_Combbox.set(Extend_Editor_List[0])
Extend_Editor_Combbox.place(x=60,y=80)

LSMASH_ckb = tkinter.BooleanVar()
LSMASH_ckb.set(True)
LSMASH_checkbox = tkinter.Checkbutton(
    root,
    variable=LSMASH_ckb,
)
LSMASH_checkbox.place(x=30,y=110)

LSMASH_List = (
    "L-SMASH-Works_Rev1100",
)

LSMASH_combobox = ttk.Combobox(
    root,
    values=LSMASH_List,
    height=10,
    width=30,
    state="readonly",
    textvariable=tkinter.StringVar()
)
LSMASH_combobox.set(LSMASH_List[0])
LSMASH_combobox.place(x=60,y=110)

Encoder_ckb = tkinter.BooleanVar()
Encoder_ckb.set(True)
Encoder_checkbox = tkinter.Checkbutton(
    root,
    variable=Encoder_ckb
)
Encoder_checkbox.place(x=30,y=140)

Encoder_List = (
    "X264guiEx",
    "easymp4"
)

Encoder_combobox = ttk.Combobox(
    root,
    values=Encoder_List,
    height=10,
    width=30,
    state="readonly",
    textvariable=tkinter.StringVar()
)
Encoder_combobox.set(Encoder_List[0])
Encoder_combobox.place(x=60,y=140)

Setup_folder_path_lavel = tkinter.Label(
    root,
    text="2.構築先フォルダを選択",
    font=(
        "",
        "10",
        "bold"
    )
)
Setup_folder_path_lavel.place(x=10,y=170)

Setup_folder_path_textbox = tkinter.Entry(
    root,
    font=(
        "",
        12
    )
)
Setup_folder_path_textbox.place(
    x=30,
    y=200,
    width=180,
    height=30
)

def Select_Setup_folder_path():
    Setup_folder_path = (filedialog.askdirectory())

    if not Setup_folder_path == "":

        if not Setup_folder_path_textbox.get() == "":
            Setup_folder_path_textbox.delete("0","end")
        else:
            pass

        Setup_folder_path_textbox.insert(
            0,
            Setup_folder_path.replace("/","\\") + "\\"
        )
    else:
        pass

def Execute():
    path = Setup_folder_path_textbox.get()
    if path =="":
        tkinter.messagebox.showerror("エラー", "構築先を選択してください。")
    else:
        if os.path.exists("Cache") == True:
            tkinter.messagebox.showerror("エラー", "一時フォルダがすでに存在します")
            return
        else:
            subprocess.run("mkdir Cache",shell=True)

        if Aviutl_exe_ckb.get() == True:
            try:
                print("Downloading...")
                subprocess.run(
                    "powershell -Command \"(New-Object Net.WebClient).DownloadFile('http://spring-fragrance.mints.ne.jp/aviutl/aviutl110.zip', 'Cache\\Aviutl110.zip')\"",
                    shell=True
                )

                print("Unzip...")
                subprocess.run(
                    "powershell -command \"Expand-Archive Cache\\Aviutl110.zip Cache\\Aviutl110\"",
                    shell=True)

                print("Moving...")
                subprocess.run(
                    "move /Y Cache\\aviutl110\\* " + path,
                    shell=True
                )
                if os.path.exists(path+"Aviutl.exe") == True:
                    pass
                else:
                    tkinter.messagebox.showerror("エラー","Aviutl.exeの取得に失敗しました")
                    return

            except:
                print("Filled")

        else:
            print("NOT Check")


Setup_folder_path_button = tkinter.Button(
    root,
    text="参照",
    command=Select_Setup_folder_path,
    width=6,
    height=2
)
Setup_folder_path_button.place(x=220,y=196)

Exceute_button = tkinter.Button(
    root,
    text="実行",
    command=Execute,
    width=20,
    height=3
)
Exceute_button.place(x=60,y=250)
root.mainloop()
