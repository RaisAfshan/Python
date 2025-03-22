try:
    file1=open(r'C:\Users\slim5\Desktop\file2.txt','r')
    print(file1.read())
    file1.close()
except FileNotFoundError:
    print("file does not exist")