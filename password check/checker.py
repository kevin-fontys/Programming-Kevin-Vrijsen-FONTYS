def pwcheck(PASSWORD):

    if len(PASSWORD) < 11:
        print("dit wachtwoord is teleurstellend slecht")
        print("probeer een sterker wachtwoord te verzinnen")
        return
    if uppercase is True and str.isalpha(PASSWORD) is False:
        print("uw wachtwoord is zeer stronk. good job!")
        return

    print("U heeft een matig wachtwoord")
    print("er is nog ruimte voor verbetering")


PASSWORD = input("voer uw wachtwoord in")
uppercase = any(x.isupper() for x in PASSWORD)
pwcheck(PASSWORD)

