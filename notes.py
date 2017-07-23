

import os, datetime, sys


wdir = os.path.join(os.getenv("HOME"), ".local")
datetimeNow = datetime.datetime.today()
dateForm = datetimeNow.strftime("%b,%d %H:%M:%S")
Green = '\033[92m'
Default = '\033[0m'
Red = '\033[91m'
notesFile = '.mynotes.nt'


def notesGraper():
    note = input(" please enter note :  ").capitalize()
    # counter = counter + 1
    return note


def notesWriter():
    if os.path.exists(wdir):
        os.chdir(wdir)
        if os.path.exists(notesFile):
            with open(notesFile, 'a+') as file:
                file.writelines(Green + str(dateForm) + Default + "   " + notesGraper() + "\n")
        else:
            with open(notesFile, 'w+') as file:
                file.writelines(Green + str(dateForm) + Default + "   " + notesGraper() + "\n")
    else:
        print(Green, "First time to use mynotes : ", Default, "Creating Data Store")
        os.makedirs(wdir)
        os.chdir(wdir)
        notesWriter()


def notesReader():
    try:
        if os.path.exists(wdir) and os.path.exists(os.path.join(wdir, notesFile)):
            os.chdir(wdir)
            fileHolder = open(notesFile, 'r+')
            content = fileHolder.read()
            for line in content.splitlines():
                print(line)
        else:
            return ( ' This is the first time to use "mynotes" , Please use write instead ..')
    except:
        print(" Something wrong happened ...")

def notesCleaner():
    try:
        if os.path.exists(wdir) and os.path.exists(os.path.join(wdir, notesFile)):
            os.chdir(wdir)
            ans = input("Are you sure ? [All notes will be removed] [yes|no]  ")
            if ans == 'yes':
                os.remove(notesFile)
                print("Deleted...")
            elif ans == 'no':
                pass
            else:
                print("please use > yes|no")
        else:
            print("Notes file does not exist ...")

    except:
        print(" Something wrong happened ...")



if __name__ == '__main__':
    try:
        chose = sys.argv[1]
        if chose == 'read':
            notesReader()
        elif chose == 'write':
            notesWriter()
        elif chose == 'clear':
            notesCleaner()
        else:
            print(" Pleae use possible value [write, read or clear]")
    except:
        print(" Pleae use possible value [write, read or clear]")