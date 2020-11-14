import zadanie1 as z1
import zadanie2 as z2
import zadanie3 as z3
import zadanie4 as z4
import zadanie5 as z5


if __name__ == '__main__':
    while True:
        print("Podaj numer zadania (aby wyjsc wpisz 'exit')")
        console_in = input()

        if console_in == "1":
            # zadanie 2 z pliku reliability.pdf
            z1.exercise()
        elif console_in == "2":
            # zadanie 3 z pliku reliability.pdf
            z2.exercise()
        elif console_in == "3":
            # zadanie 4 z pliku reliability.pdf
            z3.exercise()
        elif console_in == "4":
            # zadanie 5 z pliku reliability.pdf
            z4.exercise()
        elif console_in == "5":
            # zadanie 6 z pliku reliability.pdf
            z5.exercise()
        # exits program loop
        elif console_in == "exit":
            break
