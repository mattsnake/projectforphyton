#CPE PETITION
#MATT ANDREW SOLATAN
#batobatopick

print "batobatopick"
def batobatopick():
    player1 = input("[1] -Papel\n[2] -bato\n[3] -Gunting\n   Enter Player 1: ")
    player2 =input("   Enter Player 2: ")
    if player1 == 1:
        if player2 == 2:
             print "   PLAYER 1 WINS!\n"
        elif player2 ==3:
            print ("   PLAYER 2 WINS!\n")
        elif player2==1:
             print ("   Draw!\n")
        return batobatopick()
    elif player1 ==3:
        if player2==1:
             print ("   PLAYER 1 WINS!\n")
        elif player2==2:
             print ("   PLAYER 2 WINS!\n")
        elif player2==3:
             print ("   Draw!\n")
        return batobatopick()
    elif player1 ==2:
        if player2==2:
             print ("   Draw!\n")
        elif player2==3:
             print ("   PLAYER 1 WINS!\n")
        elif player2==1:
             print ("   PLAYER 2 WINS!\n")
        return batobatopick()
    
batobatopick()
