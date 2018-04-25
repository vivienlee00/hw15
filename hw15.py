p = "Password1"

def testPassword (password):
    
    UC_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lc_letters = "abcdefghijklmnopqrstuvwxyz"
    nums = "1234567890"
    
    hasUC = False
    hasLC = False
    hasNum = False
    
    if len([x for x in p if x in UC_LETTERS]) != 0:
        hasUC = True

    if len([x for x in p if x in lc_letters]) != 0:
        hasLC = True
        
    if len([x for x in p if x in nums]) != 0:
        hasNum = True

    return(hasUC and hasLC and hasNum)

if(testPassword(p)):
    print("yas")


def ratePassword (password):
    
