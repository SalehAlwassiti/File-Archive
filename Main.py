import customtkinter as ctk
from tkinter import messagebox, filedialog
import datetime, os, shutil

def File_manager():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    path = "D:\\test"
    original_path = path
    Files = os.listdir(path)

    def logout():
        app.destroy()

    def confirm():
        messagebox.askyesno("Warning", "Are you sure you wish to delete this file?")
    
    def add_file(path):
        local_file = filedialog.askopenfilename()
        if os.path.isfile(local_file):
            shutil.copy(local_file, path)

    # def search(path, searched):
    #     if searched == '':
    #         Files_new = os.listdir(path)
    #         nonlocal Files
    #         Files = Files_new
        
    #     else:
    #         string = ''
    #         dir = ''
    #         dir_list = []
            
    #         list = os.listdir(path)
    #         for items in list:
    #             string += items
            
    #         find = re.findall(searched, string)
            
    #         for items in find:
    #             dir = path + '\\' + items
    #             dir_list.append(dir)
            
    #         Files = dir_list
    #         print(Files)

    def create_file(path):
        create = ctk.CTk()
        create.title("Create New Folder")
        create_entery = ctk.CTkEntry(create, placeholder_text='Folder Name')
        create_entery.grid(row = 0,column = 0 ,pady = 17, padx = 50,ipadx = 30)
       
        def buffer(path):
            inputed = create_entery.get()
            
            level = level_option.get()
            
            if check_A.get() != '':
                A = check_A.get()
            else:
                A = ''
            
            if check_B.get() != '':
                B = check_B.get()
            else:
                B = ''

            if check_C.get() != '':
                C = check_C.get()
            else:
                C = ''

            if check_D.get() != '':
                D = check_D.get()
            else:
                D = ''

            if check_E.get() != '':
                E = check_E.get()
            else:
                E = ''

            try:
                code = level + A + B + C + D + E
                # hashed = hashlib.sha256(code.encode()).hexdigest()
                final = inputed + ' (' + code + ')'
                path = os.path.join(path, final)
                os.mkdir(path)
                create.destroy()
            
            except FileExistsError:
                create_error = ctk.CTkToplevel(create)
                create_error.lift()
                create_error.attributes("-topmost", True)
                create_error_label = ctk.CTkLabel(create_error, text='Folder Already exists!')
                create_error_label.grid(row=0, column=0, pady=2, padx=20)
                create_error_button = ctk.CTkButton(create_error, text='OK', command=create_error.destroy)
                create_error_button.grid(pady=5)

        create_button = ctk.CTkButton(create, text='Done', command=lambda:buffer(path))
        create_button.grid(row=7, column=0, pady = 8)

        level_option = ctk.CTkOptionMenu(create, values=['0', '1','2','3'])
        level_option.grid(row=1, column=0, pady=2, padx=20)

        check_A = ctk.CTkCheckBox(create, text='A', onvalue='A', offvalue='')
        check_A.grid(row=2, column=0, pady=2, padx=20)

        check_B = ctk.CTkCheckBox(create, text='B', onvalue='B', offvalue='')
        check_B.grid(row=3, column=0, pady=2, padx=20)
        
        check_C = ctk.CTkCheckBox(create, text='C', onvalue='C', offvalue='')
        check_C.grid(row=4, column=0, pady=2, padx=20)
        
        check_D = ctk.CTkCheckBox(create, text='D', onvalue='D', offvalue='')
        check_D.grid(row=5, column=0, pady=2, padx=20)

        check_E = ctk.CTkCheckBox(create, text='E', onvalue='E', offvalue='')
        check_E.grid(row=6, column=0, pady=2, padx=20)

        create.mainloop()

    class SideFrame(ctk.CTkFrame):
        def __init__(self, master, **kwargs):
            super().__init__(master, **kwargs)

            self.Welcome_label = ctk.CTkLabel(self, text="Logged in as", font=("DaunPenh", 20))
            self.Welcome_label.grid(row=0, column=0, padx=30, pady=0)

            self.grid_columnconfigure(1, weight=1)

            self.Welcome_label2_back = ctk.CTkLabel(self, text="USER", font=("DaunPenh", 20), text_color="#001cff")
            self.Welcome_label2_back.grid(row=1, column=0, padx=2, pady=0)

            self.Search_label = ctk.CTkLabel(self, text="Search for Items and Files: ")
            self.Search_label.grid(row=2, column=0, padx=10, pady=0)

            self.Search = ctk.CTkEntry(self, placeholder_text="Search[WIP]")
            self.Search.grid(row=3, column=0, padx=10, pady=0, ipadx=40)

            self.srch_btn = ctk.CTkButton(self, text="Search[WIP]")
            self.srch_btn.grid(row=4, column=0, padx=20, pady=5)

            self.rfrsh = ctk.CTkButton(self, text="Refresh[WIP]", state="False", fg_color="#58585e", text_color="#95959b")
            self.rfrsh.grid(row=5, column=0, pady=5)

            self.add = ctk.CTkButton(self, text="Add Files +",command=lambda:add_file(path))
            self.add.grid(row=6,column=0,pady=5 )

            self.create = ctk.CTkButton(self, text = "Create New Folder +", command=lambda:create_file(path))
            self.create.grid(row = 7, column = 0 , pady = 5)

            self.rowconfigure(8, minsize=380)

            self.button_logout = ctk.CTkButton(self, text="Logout", fg_color="#ff1700", hover_color='#8a0c00', command=logout)
            self.button_logout.grid(row=9, column=0, padx=2, pady=0)

    class MainFrame(ctk.CTkScrollableFrame):
        def __init__(self, master, **kwargs):
            super().__init__(master, **kwargs)

            def rename(to_rename):
                os.chdir(path)
                ext = os.path.splitext(to_rename)[-1]
                dirname = os.path.dirname(to_rename)

                def buffer():
                    get = Rename_entery.get()
                    if get != '':
                        rename = os.path.join(dirname, get+ext)
                        os.rename(to_rename, rename)
                        Rename_toplevel.destroy()

                Rename_toplevel = ctk.CTkToplevel(self.master)
                Rename_toplevel.lift()
                Rename_toplevel.attributes("-topmost", True)
                Rename_toplevel.title("Rename")
                Rename_entery = ctk.CTkEntry(Rename_toplevel, placeholder_text='Enter new name')
                Rename_entery.grid(row = 0,column = 0 ,pady = 17, padx = 50,ipadx = 30)
                Rename_button = ctk.CTkButton(Rename_toplevel, text='Done', command=buffer)
                Rename_button.grid(pady = 8)

            self.columnconfigure(5, minsize=100)

            self.bck_button = ctk.CTkButton(self, text="Back", state="disabled", fg_color="#58585e")
            self.bck_button.grid(row=0, column=0, sticky='w')

            # self.label1 = ctk.CTkLabel(self, text="Files", font=("DaunPenh", 15))
            # self.label1.grid(row=0,column=0,sticky = "w")

            # self.label2 = ctk.CTkLabel(self, text="Access Level", font=("DaunPenh", 15))
            # self.label1.grid(row=0,column = 1)

            count = 1
            for i in Files:
                self.Item = ctk.CTkLabel(self, text='- ' +i)
                self.Item.grid(row=count, column=0,
                               padx=15, pady=5, sticky="w")
                count += 1
            self.columnconfigure(1, minsize=150)

            count = 1
            for i in Files:
                self.button = ctk.CTkButton(self, text="Open", command=lambda i=i: open(i, path))
                self.button.grid(row=count, column=2, padx=3)

                self.button2 = ctk.CTkButton(self, text="Rename", command=lambda i=i: rename(i))
                self.button2.grid(row=count, column=3, padx=3, ipadx=1)

                self.button3 = ctk.CTkButton(self, text="Delete", fg_color="#b51000", hover_color="#7b0b00", command=confirm)
                self.button3.grid(row=count, column=4, padx=3, ipadx=1)
                count += 1

            def back():
                nonlocal path
                path = original_path

                for i in MainFrame.winfo_children(self):
                    i.destroy()

                    count = 1
                    Files_new = os.listdir(path)
                    Files = Files_new

                    for i in Files:
                        self.Item = ctk.CTkLabel(self, text="- "+i)
                        self.Item.grid(row=count, column=0,padx=15, pady=5, sticky="w")
                        count += 1

                    count = 1
                    for i in Files:
                        self.button = ctk.CTkButton(self, text="Open", command=lambda i=i: open(i, path))
                        self.button.grid(row=count, column=2, padx=3)

                        self.button2 = ctk.CTkButton(self, text="Rename", command=lambda i=i: rename(i))
                        self.button2.grid(row=count, column=3, padx=3, ipadx=1)

                        self.button3 = ctk.CTkButton(self, text="Delete", fg_color="#b51000", hover_color="#7b0b00", command=confirm)
                        self.button3.grid(row=count, column=4, padx=3, ipadx=1)
                        count += 1

                    self.button = ctk.CTkButton(self, text="Refresh", command=scan)
                    self.button.grid(row=0, column=6)

                    self.bck_button = ctk.CTkButton(self, text="Back", state="disabled", fg_color="#58585e")
                    self.bck_button.grid(row=0, column=0, sticky='w')

            def open(to_open, path1):
                ext = os.path.splitext(to_open)[-1]
                if ext == '':
                    nonlocal path
                    path = path1 + '\\' + to_open

                    for i in MainFrame.winfo_children(self):
                        i.destroy()

                    
                    if os.listdir(path) == []:
                        self._label = ctk.CTkLabel(self,text="This folder is empty.", font=("DaunPenh", 20))
                        self._label.grid(row = 1,column = 0 ,pady = 10)

                        self.bck_button = ctk.CTkButton(self, text='Back', command=back)
                        self.bck_button.grid(row=0, column=0, sticky='w')

                    else:
                        count = 1
                        Files_new = os.listdir(path)
                        Files = Files_new

                        for i in Files:
                            self.Item = ctk.CTkLabel(self, text="- "+i)
                            self.Item.grid(row=count, column=0,padx=15, pady=5, sticky="w")
                            count += 1

                        count = 1
                        for i in Files:
                            self.button = ctk.CTkButton(self, text="Open", command=lambda i=i: open(i, path))
                            self.button.grid(row=count, column=2, padx=3)

                            self.button2 = ctk.CTkButton(self, text="Rename", command=lambda i=i: rename(i))
                            self.button2.grid(row=count, column=3, padx=3, ipadx=1)

                            self.button3 = ctk.CTkButton(self, text="Delete", fg_color="#b51000", hover_color="#7b0b00", command=confirm)
                            self.button3.grid(row=count, column=4, padx=3, ipadx=1)
                            count += 1

                            self.button = ctk.CTkButton(self, text="Refresh", command=scan)
                            self.button.grid(row=0, column=6)

                            self.bck_button = ctk.CTkButton(self, text='Back', command=back)
                            self.bck_button.grid(row=0, column=0, sticky='w')

                else:
                    os.chdir(path)
                    os.startfile(to_open)



            def scan():

                for i in MainFrame.winfo_children(self):
                    i.destroy()
                
                count = 1
                Files_new = os.listdir(path)
                Files = Files_new

                for i in Files:
                    self.Item = ctk.CTkLabel(self, text="- "+i)
                    self.Item.grid(row=count, column=0,padx=15, pady=5, sticky="w")
                    count += 1

                count = 1
                for i in Files:
                    self.button = ctk.CTkButton(self, text="Open", command=lambda i=i: open(i, path))
                    self.button.grid(row=count, column=2, padx=3)

                    self.button2 = ctk.CTkButton(self, text="Rename", command=lambda i=i: rename(i))
                    self.button2.grid(row=count, column=3, padx=3, ipadx=1)

                    self.button3 = ctk.CTkButton(self, text="Delete", fg_color="#b51000", hover_color="#7b0b00", command=confirm)
                    self.button3.grid(row=count, column=4, padx=3, ipadx=1)
                    count += 1

                if original_path == path:
                    self.bck_button = ctk.CTkButton(self, text='Back', state="disabled", fg_color="#58585e")
                    self.bck_button.grid(row=0, column=0, sticky='w')
                else:
                    self.bck_button = ctk.CTkButton(self, text='Back',command=back)
                    self.bck_button.grid(row=0, column=0, sticky='w')

                self.button = ctk.CTkButton(self, text="Refresh", command=scan)
                self.button.grid(row=0, column=6)

                

            self.button = ctk.CTkButton(self, text="Refresh", command=scan)
            self.button.grid(row=0, column=6)

    class App(ctk.CTk):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.geometry("1280x720")
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)

            self.sideframe = SideFrame(master=self, fg_color="#353535")
            self.sideframe.grid(row=0, column=0, padx=2, pady=2, sticky="nsw")

            self.MainFrame = MainFrame(master=self)
            self.MainFrame.grid(row=0, column=1, padx=0, pady=0, sticky='nsew')

            def clock():
                time = datetime.datetime.now().strftime("Time: %H:%M:%S")
                self.Time.configure(text=time)

                self.Time.after(1000, clock)

            self.Time = ctk.CTkLabel(self, text="TIME[PLACEHOLDER]")
            self.Time.grid(row=2, column=0, padx=2, pady=2, sticky="nsw")

            clock()

    app = App()
    app.grid_columnconfigure(1, weight=300)
    app.mainloop()

File_manager()
