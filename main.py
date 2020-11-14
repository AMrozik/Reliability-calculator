import zadanie1 as z1
import zadanie2 as z2


while True:
    print("Podaj numer zadania (aby wyjsc wpisz 'exit')")
    console_in = input()

    if console_in == "1":
        # zadanie 2 w pliku pfd
        z1.exercise()
    elif console_in == "2":
        z2.exercise()
    # elif console_in == "3":
    #     exercise3()
    # elif console_in == "4":
    #     exercise4()
    # elif console_in == "5":
    #     exercise5()
    # exits program loop
    elif console_in == "exit":
        break
