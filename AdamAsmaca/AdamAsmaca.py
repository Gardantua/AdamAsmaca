import random
import string

def adamAsmaca():
    kelimeler = ["Mandal","Mezura","Merdane","Masa","Makas","Mangal","Ampul","Anten","Ayakkabı","Atkı","Askı","Ayna","Balyoz","Bardak","Barut","Baston","Bavul","Bayrak","Bileklik","Bilgisayar","Cımbız","Cetvel","Ceket","Defter","Demir","Etek","Eldiven","Far","Fes","Gazete","Havlu","Hamak","Izgara","Küpe","Kolye","Lastik","Minder","Ranza","Saksı","Toka","Şapka","Yatak","Zurna","Jilet","Ocak","Para","Rende","Sandalye","Şampuan","Televizyon","Yaprak","Uçurtma","Ütü","Uçak"]                                                                    

    word = random.choice(kelimeler)
    upperWord = word.upper()
    wordLetters = set(upperWord)
    usedLetters = set()
    abv = ["A","B","C","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","P","Ö","Ü","U","V","Y","Z","T","Ç","R","S","Ş"]
    alphabet = set(abv)
    print("---------------------ADAM ASMACA---------------------")
    hangingCounter = 0   
    h1=("  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========")
    h2=("  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========")
    h3=("  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========")
    h4=("  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========")
    h5=("  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========")
    h6=("  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========")
    h7=("  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========")

    
    sayac = 0
    while True:
        print("Kullandığınız kelimeler : ",''.join(usedLetters))
        wordList = [letter if letter in usedLetters else '-' for letter in upperWord]
        print("Kelime ", ' '.join(wordList))

        if sayac == 0:
            print(h1)
        elif sayac == 1:
            print(h2)
        elif sayac == 2:
            print(h3)
        elif sayac == 3:
            print(h4)
        elif sayac == 4:
            print(h5)
        elif sayac == 5:
            print(h6)
        else:
            print(h7)

        if sayac==6:
            print("Oyunu kaybettiniz :(")
            break

        if '-' in wordList:
            adwgakgwdu = 2
        else:
            print("Tebrikler kazandınız !!!  :)")
            break
        
        letterGuess = input("Bir harf tahmin et : ").upper()
        if letterGuess in wordLetters:
            asdd=3
        else:
            sayac+=1

        if letterGuess in alphabet:
            usedLetters.add(letterGuess)
            """
            if letterGuess in wordLetters:
                wordLetters.remove(letterGuess)
                """
        elif letterGuess in usedLetters:
            print(f"Oyunu kaybettiniz :( Kelime {upperWord} idi")
            sayac+=1
        else:
            sayac+=1

        if '-' in wordList:
            adwgakgwdu = 2
        else:
            print("Tebrikler kazandınız !!!  :)")
            break

adamAsmaca()


