from tkinter import *
import tkinter.messagebox as tm
import requests
import os, struct
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES

URL = 'http://127.0.0.1:8000/fda/'
MEDIA = 'http://127.0.0.1:8000/media/'
user = ""
idn = ""
ind = ""

def getReportsList(username):
    r = requests.post(URL + 'getReportsList/', data={'username': username})
    reports = r.json().get('reports_list')
    return reports

def encrypt_file(file_name, sym_key):
    try:
        key = hashlib.sha256(sym_key).digest()
        mode = AES.MODE_CBC
        iv = 16*'a'
        chunk_size = 8192
        encryptor = AES.new(key, AES.MODE_CBC, iv)
        filesize = os.path.getsize(file_name)
        out_file = file_name + '.enc'
        with open(file_name, 'rb') as f:
            with open(out_file, 'wb') as outfile:
                outfile.write(struct.pack('<Q', filesize))
                outfile.write(str.encode(iv))
                while True:
                    chunk = f.read(chunk_size)
                    if len(chunk)==0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += str.encode(' ' * (16 - (len(chunk) % 16)))
                    outfile.write(encryptor.encrypt(chunk))
        return True
    except FileNotFoundError:
        return False

def decrypt_file(file_name, sym_key):
    try:
        if file_name.endswith('.enc'):
            new_name = file_name[:-4]
            new_name = 'DEC_' + new_name
            key = hashlib.sha256(sym_key).digest()
            mode = AES.MODE_CBC
            # iv = 16 * 'a'
            chunk_size = 8192

            with open(file_name, 'rb') as f:
                filesize = struct.unpack('<Q', f.read(struct.calcsize('<Q')))[0]
                iv = f.read(16).decode()
                if iv != (16*'a'):
                    return False
                decryptor = AES.new(key, mode, iv)

                with open(new_name, 'wb') as outfile:
                    while True:
                        chunk = f.read(chunk_size)
                        if len(chunk) == 0:
                            break
                        outfile.write(decryptor.decrypt(chunk))
                    outfile.truncate(filesize)
            return True
        return False
    except FileNotFoundError:
        return False

class Enc(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label_1 = Label(self, text="Encrypt File")
        self.label_1.grid(row=0, sticky=E)

        self.label_2 = Label(self, text="File Name")
        self.entry_1 = Entry(self)

        self.label_2.grid(row=1, sticky=E)
        self.entry_1.grid(row=1, column=1)

        self.encrypt = Button(self, text="Encrypt", command=self.encbut)
        self.encrypt.grid(columnspan=2)
        self.back = Button(self, text="Home", command=self.back)
        self.back.grid(columnspan=2)
        self.pack()

    def encbut(self):
        to_encrypt = self.entry_1.get()
        if encrypt_file(to_encrypt, str.encode("password")):
            tm.showinfo("Encrypting", "File successfully encrypted!")
        else:
            tm.showinfo("Encrypt Attempt", "ERROR: File Not Found")

    def back(self):
        self.destroy()
        LoggedIn(root)

class Dec(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_1 = Label(self, text="Decrypt File")
        self.label_1.grid(row=0, sticky=E)

        self.label_2 = Label(self, text="File Name")
        self.entry_1 = Entry(self)

        self.label_2.grid(row=1, sticky=E)
        self.entry_1.grid(row=1, column=1)

        self.encrypt = Button(self, text="Decrypt", command=self.decbut)
        self.encrypt.grid(columnspan=2)
        self.back = Button(self, text="Home", command=self.back)
        self.back.grid(columnspan=2)
        self.pack()

    def decbut(self):
        to_decrypt = self.entry_1.get()
        if decrypt_file(to_decrypt, str.encode("password")):
            tm.showinfo("Decrypting", "File successfully decrypted!")
        else:
            tm.showinfo("Decrypt Attempt", "ERROR: File Not Found")

    def back(self):
        self.destroy()
        LoggedIn(root)

class dlReports(Frame):
    def __init__(self, master):
        super().__init__(master)

        reports = getReportsList(user)
        report = reports[int(float(ind))]
        content_list = report['content']

        self.label_1 = Label(self, text="View Report " + idn)
        self.label_1.grid(row=0, sticky=E)

        self.back = Button(self, text="Back to All Reports", command=self._back_btn_clicked)
        self.back.grid(columnspan=2)
        self.button = []
        for i in range(len(content_list)):
            self.button.append(Button(self, text="Download " + content_list[i]['file_name'],
                                      command=(lambda i=i: self.download(content_list, i))))
            self.button[i].grid(column=4, row=i + 1, sticky=W)
        self.pack()

        global t
        t = Text(root, height=14+len(content_list), width=70, font='Helvetica')
        t.insert(INSERT, "REPORT ID: \t\t\t" + str(report['id']) + "\n")
        t.insert(INSERT, "Timestamp: \t\t\t" + report['timestamp'] + "\n")
        t.insert(INSERT, "Is Private: \t\t\t" + report['is_private'] + "\n")
        t.insert(INSERT, "Project: \t\t\t" + report['projects'] + "\n")
        t.insert(INSERT, "Group: \t\t\t" + report['group'] + "\n")
        t.insert(INSERT, "Company Name: \t\t\t" + report['company_name'] + "\n")
        t.insert(INSERT, "Industry: \t\t\t" + report['industry'] + "\n")
        t.insert(INSERT, "CEO Name: \t\t\t" + report['ceo_name'] + "\n")
        t.insert(INSERT, "Company Phone: \t\t\t" + report['company_phone'] + "\n")
        t.insert(INSERT, "Company Email: \t\t\t" + report['company_email'] + "\n")
        t.insert(INSERT, "Company Location: \t\t\t" + report['company_location'] + "\n")
        t.insert(INSERT, "Company Country: \t\t\t" + report['company_country'] + "\n")
        t.insert(INSERT, "Sector: \t\t\t" + report['sector'] + "\n")
        t.insert(INSERT, "Attached Files: \t" + "\n")
        for file in content_list:
            if file['file_status'] == 'N':
                t.insert(INSERT, "     " + file['file_name'] + "\n")
            else:
                t.insert(INSERT, "     " + file['file_name'])
            if file['file_status'] == 'Y':
                t.insert(INSERT, "[ENCRYPTED]" + "\n")
        t.config(state=DISABLED)
        t.pack()

    def download(self, content_list, i):
        current_file_name = content_list[i]['file_name']
        r = requests.get(MEDIA + current_file_name, stream=True)
        with open(current_file_name[8:], 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        f.close()
        tm.showinfo("Download", "SUCCESSFULLY DOWNLOADED '" + current_file_name[8:] + "'")
        if content_list[i]['file_status'] == 'Y':
            tm.showinfo("Encrypted File", "**Our records indicate that this file may be encrypted**")

    def _back_btn_clicked(self):
        t.destroy()
        self.destroy()
        ViewReports(root)

class ViewReports(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_1 = Label(self, text="View Reports")
        self.label_1.grid(row=0, sticky=E)
        self.button = []

        reports = getReportsList(user)
        for i in range(len(reports)):
            self.button.append(Button(self, text=str(i + 1) + ". " + "REPORT ID: " + str(reports[i]['id']) + "\n" +
                                      "Project: " + reports[i]['projects'] + "\n" + "Company: " +
                                      reports[i]['company_name'] + "\n" + "Sector: " + reports[i]['sector'], command=
                                      (lambda i=i: self.open_this(reports[i]))))  # self._login_btn_clickked))
            self.button[i].grid(column=4, row=i + 1, sticky=W)

        self.back = Button(self, text="Home", command = self.home)
        self.back.grid(columnspan=2)

        self.pack()

    def open_this(self, repo):
        global idn
        global ind
        idn = str(repo['id'])
        for i in range(len(getReportsList(user))):
            if str(getReportsList(user)[i]['id']) == idn:
                ind = i
        self.destroy()
        dlReports(root)
        global report
        report = repo

    def home(self):
        self.destroy()
        LoggedIn(root)

class LoggedIn(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_1 = Label(self, text="Welcome!")
        self.label_1.grid(row=0, sticky=E)

        self.report = Button(self, text="View Reports", command = self._report_btn_clickked)
        self.report.grid(columnspan=2)
        self.encr = Button(self, text="Encrypt File", command = self.encrbut)
        self.encr.grid(columnspan=2)
        self.decr = Button(self, text="Decrypt File", command = self.decrbut)
        self.decr.grid(columnspan=2)
        self.logbtn = Button(self, text="Logout", command = self._login_btn_clickked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _report_btn_clickked(self):
        self.destroy()
        ViewReports(root)

    def _login_btn_clickked(self):
        self.destroy()
        LoginFrame(root)

    def encrbut(self):
        self.destroy()
        Enc(root)

    def decrbut(self):
        self.destroy()
        Dec(root)

class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_1 = Label(self, text="Username")
        self.label_2 = Label(self, text="Password")

        self.entry_1 = Entry(self)
        self.entry_2 = Entry(self, show="*")

        self.label_1.grid(row=0, sticky=E)
        self.label_2.grid(row=1, sticky=E)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)

        # self.checkbox = Checkbutton(self, text="Keep me logged in")
        # self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Login", command = self._login_btn_clickked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _login_btn_clickked(self):
        #print("Clicked")
        username = self.entry_1.get()
        password = self.entry_2.get()

        #print(username, password)

        while True:
            if username == "exit" and password == "exit":
                quit()
            r = requests.post(URL + '', data={'username': username, 'password': password})
            # access (URL + 'something/' ) for a new url/view
            # send parameters dictionary style

            success = r.json().get('verification')
            if success:
                # print("You have successfully logged in")
                global user
                user = username
                tm.showinfo("Welcome!", "Welcome to Lokahi Fintech Crowdfunding\n" + "User, " + user)
                self.destroy()
                LoggedIn(root)
                break
            else:
                tm.showerror("Login error", "Incorrect username")
                # print("ERROR: Invalid Login")
                break

root = Tk()
lf = LoginFrame(root)
root.wm_title("Lokahi FDA")
t = Text(root)
root.mainloop()
