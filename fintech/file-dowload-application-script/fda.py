import requests
import os, struct
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES


URL = 'http://127.0.0.1:8000/fda/'
MEDIA = 'http://127.0.0.1:8000/media/'

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
# main method redirected to top of page
def main():
    clear()
    print("***********************************************")
    print("Welcome to the Lokahi File Download Application")
    print("***********************************************")
    username = verifylogin()
    print("Welcome, " + username)

    # this input is just to delay the user and show the welcome
    print("Enter anything to continue. Type 'exit' to leave")
    starter = input()
    if starter == "exit":
        quit()

    # the choice variable will dictate which path to take every time.
    # update choice after every action!!
    # You may change (and will most likely change) these actions or add additional actions.
    # Please update this table if you do!
    # -1: quit
    # 0: List Reports, then user can select
    # 1: Detailed Report View.
    # 2: Download Files
    # 3: Decrypt a File
    # 4: Encrypt a File
    choice = 0 #indicates which 'page' the view is in
    report_choice = -1 #indicates which report we're dealing with (-1 means none)
    reports = [] #indicates reports the user can view.

    while True:
    # LIST REPORTS THEN USER CAN SELECT ####################################
        if choice == -1:
            print("THANK YOU FOR USING LOKAHI")
            quit()
        if choice == 0:
            clear()
            print("================================================")
            print("Select a report by entering the appropriate number")

            reports = getReportsList(username)

            for i in range(0, len(reports)):
                print(str(i+1) + ". " + "REPORT ID: " + str(reports[i]['id']))
                print("     Project: " + reports[i]['projects'])
                print("     Company: " + reports[i]['company_name'])
                print("     Sector: " + reports[i]['sector'])

            while True:
                print("================================================")
                print("Select the report you would like to view by entering the number")
                print("Enter the number zero (0) to quit")
                try:
                    report_choice = int(input())
                except Exception:
                    print("Please enter an integer")
                    report_choice = -1

                if report_choice == 0:
                    choice = -1
                    break
                elif report_choice > 0 and report_choice <= len(reports):
                    choice = 1
                    break
                else:
                    print("ERROR. Invalid Choice")

        # DETAILED REPORT VIEW ########## MUST GO THROUGH CHOICE 0 FIRST ########
        elif choice == 1:
            clear()
            print("================================================")
            current_report = reports[report_choice-1]
            print("REPORT ID: " + str(current_report['id']))
            print("Timestamp: " + current_report['timestamp'])
            print("Project: " + current_report['projects'])
            print("Company Name: " + current_report['company_name'])
            print("Company Phone: " + current_report['company_phone'])
            print("Company Location: " + current_report['company_location'])
            print("Company Country: " + current_report['company_country'])
            print("Sector: " + current_report['sector'])
            content_list = current_report['content']
            print("Attached Files: ")
            for file_name in content_list:
                print("     " + file_name)
            while True:
                print("================================================")
                print("Enter the number one (1) to go back to report views")
                print("Enter the number two (2) to download files")
                print("Enter the number three (3) to decrypt files")
                print("Enter the number four (4) to encrypt files")
                try:
                    nav = int(input())
                except Exception:
                    print("Please enter an integer")
                    nav = -1

                if nav == 1:
                    choice = 0
                    break
                elif nav == 2:
                    choice = 2
                    break
                elif nav == 3:
                    choice = 3
                    break
                elif nav == 4:
                    choice = 4
                    break
                else:
                    print("ERROR: Invalid Choice")
        elif choice == 2:
            clear()
            current_report = reports[report_choice - 1]
            content_list = current_report['content']
            while True:
                print("================================================")
                print("Select a file by entering the corresponding number")
                for i in range(0, len(content_list)):
                    print(str(i+1) + ". " + content_list[i])
                try:
                    file_choice = int(input())
                except Exception:
                    print("Please enter an integer")
                    file_choice = -1

                if file_choice > 0 and file_choice <= len(content_list):
                    current_file_name = content_list[file_choice-1]
                    r = requests.get(MEDIA + current_file_name, stream=True)
                    with open(current_file_name[8:], 'wb') as f:
                        for chunk in r.iter_content(chunk_size=1024):
                            if chunk:
                                f.write(chunk)
                    f.close()
                    print("SUCCESSFULLY DOWNLOADED '" + current_file_name[8:] + "'")
                    if current_report['is_encrypted'] == 'Y':
                        print("**Our records indicate that this file may be encrypted**")
                    input()
                    choice = 1
                    break
                else:
                    print("ERROR: Invalid Choice")

        elif choice == 3:
            clear()
            while True:
                print("================================================")
                print("FILE DECRYPTION")
                print("Please enter the name of the file that needs to be decrypted")
                print("[Enter 'exit' to leave]")
                to_decrypt = input()
                if to_decrypt == "exit":
                    choice = 1
                    break
                if decrypt_file(to_decrypt, str.encode("password")):
                    print("File successfully decrypted!")
                    input()
                    choice = 1
                    break
                else:
                    print("ERROR: File Not Found")
                    print("NOTE: This may be because the file does not seem to be encrypted")
                    print("     If you would like to force a decryption, add an '.enc' extension")
                    print("     Make sure you're confident or you may run into data corruption")

        elif choice == 4:
            clear()
            while True:
                print("================================================")
                print("FILE ENCRYPTION")
                print("Please enter the name of the file that needs to be encrypted")
                print("[Enter 'exit' to leave]")
                to_encrypt = input()
                if to_encrypt == "exit":
                    choice = 1
                    break
                if encrypt_file(to_encrypt, str.encode("password")):
                    print("File successfully encrypted!")
                    input()
                    choice = 1
                    break
                else:
                    print("ERROR: File Not Found")

        else:
            clear()
            print("ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR")
            print("ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR")
            print("ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR")
            print("ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR")
            print("=====================================================")
            print("THIS IS THE PROGRAMMER'S FAULT. YOU SHOULD HAVE NEVER REACHED HERE")
            print("CHOICE IS INVALID AND YOU ALMOST CAUSED AN INFINITE LOOP")
            print("EXITING SAFELY")
            quit()



def verifylogin():
    while True:
        print("Type 'exit' for the Username and Password to leave")
        username = input("Please enter your Username: ")
        password = input("Please enter your Password: ")
        if username == "exit" and password == "exit":
            quit()
        r = requests.post(URL + '', data={'username': username, 'password': password})
        # access (URL + 'something/' ) for a new url/view
        # send parameters dictionary style

        success = r.json().get('verification')
        if success:
            print("You have successfully logged in")
            break
        else:
            print("ERROR: Invalid Login")
    return username
def getReportsList(username):
    r = requests.post(URL + 'getReportsList/', data={'username': username})
    reports = r.json().get('reports_list')
    return reports


########################################################################################
########################################################################################
# -------------------- ENCRYPTION AND DECRYPTION USING AES -----------------------------
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
                    elif len(chunk) %16 !=0:
                        chunk += str.encode(' ' * (16 - (len(chunk) %16)))
                    outfile.write(encryptor.encrypt(chunk))
        return True
    except FileNotFoundError:
        return False
# sym_key is byte string
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
                if iv != (16* 'a'):
                    return False
                decryptor = AES.new(key, mode, iv)

                with open(new_name, 'wb') as outfile:
                    while True:
                        chunk = f.read(chunk_size)
                        if len(chunk) ==0:
                            break
                        outfile.write(decryptor.decrypt(chunk))
                    outfile.truncate(filesize)
            return True
        return False
    except FileNotFoundError:
        return False

if __name__ == "__main__":
    main()
