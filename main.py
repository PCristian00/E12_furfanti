def traduzione(testo):
    vocali = "aeiou"
    specials = [" ", ",", ".", "?", "!", '"', "'"]
    tradotto = ""
    for c in testo:
        if c in vocali or c in specials:
            tradotto += c
        else:
            tradotto = tradotto + c + "o" + c
    print(tradotto)


testo = input("Inserire frase da tradurre in linguaggio dei furfanti.\n")
traduzione(testo)
