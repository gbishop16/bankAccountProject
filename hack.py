def check_account(file):
    myfile = open("Accounts 0.txt", "rt")
    contents = myfile.read(14)
    myfile.close()
    print(contents)
