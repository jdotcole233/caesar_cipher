import time
from FileModule import encrypt_file
from CaesarModule import CaesarCipher

def userchoices(choice):
    program = True
    if choice == 1:
        try:
            file_name = input("Enter file name: ")
            sk = int(input("Enter number of shifts expected (default=4): "))
            encrypt_file(file_name, sk)
        except ValueError:
            print("Wrong value entered")
    # elif choice == 2:
    #     try:
    #         text = input("Enter something nice: ") 
    #         sk = int(input("Enter number of shifts expected (default=4): "))
    #     except ValueError:
    #         print("wrong key entered")
        
    #     caesar = CaesarCipher(text, sk)
    #     cipher = caesar.caesar_encryption()
    #     time.sleep(0.5)
    #     print("Cipher Text generated: {}".format(cipher))
    #     print("Share key {} securely with third party".format(sk))
    #     print("\n")

    elif choice == 2:
        print("Ending program. Good bye!")
        time.sleep(0.5)
        program = False
    else:
        print("wrong choice. Try Again")

    return program



def main() -> None:
    program = True
    while program:
        try:
            choice =  int(input("Encrypt from:\n1.File\n2.Quit\n> "))
            time.sleep(0.5)
            program = userchoices(choice)
        except ValueError:
            print("Wrong value inputted.")
        except KeyboardInterrupt:
            print("\nEnding program. GoodBye!")
            program = False




if __name__ == '__main__':
    main()