p = "Password1!!!!!?"


#tests if password contains uppercase letters
def testUC (password):
    UC_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if len([x for x in p if x in UC_LETTERS]) != 0:
        return True
    else:
        return False


#tests if password contains lowercase letters
def testLC (password):
    lc_letters = "abcdefghijklmnopqrstuvwxyz"

    if len([x for x in p if x in lc_letters]) != 0:
        return True
    else:
        return False


#tests if password contains numbers
def testNums (password):
    nums = "1234567890"

    if len([x for x in p if x in nums]) != 0:
        return True
    else:
        return False


#returns number of symbols in password, capped at 4
def testSymbols (password):
    symbols = ".?!&#,;:-_*"

    if len([x for x in p if x in symbols]) >= 4:
        return 4
    else:
        return len([x for x in p if x in symbols])


#validates password -- must have an uppercase letter, lowercase letter, and a number
def testPassword (password):
    return(testUC(password) and testLC(password) and testNums(password))


#rates password out of 10 -- if the password is valid it automatically has a score of 6, and increments by one for each additional symbol up to four symbols
def ratePassword (password):
    rating = 0

    if testUC(password):
        rating += 2

    if testLC(password):
        rating += 2

    if testNums(password):
        rating += 2

    rating += testSymbols(password)

    return rating
