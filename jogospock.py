import random

pedra=1
papel=2
tesoura=3
spock=4
lagarto=5

jogadapc = 0
t=0
jpc=0
jjog=0 
 
while (jpc<3 and jjog<3):
    jogadapc=random.randint(1,5)
    t=t+1
    print("Jogada:%d" %t)
    x=(int(input("Digite 1-pedra, 2-papel, 3-tesoura, 4-Spock, 5-lagarto:\n")))
    print("Jogador= %d" %x)
    print("Computador= %d" %jogadapc)
    if x==1:
        if jogadapc==1:
            print("Empate")
        elif jogadapc==2:
            print("Computador ganha")
            jpc=jpc+1
        elif jogadapc==3:
            print("Jogador ganha")
            jjog=jjog+1
        elif jogadapc==4:
            print("Computador ganha")
            jpc=jpc+1
        elif jogadapc==5:
            print("Jogador ganha")
            jjog=jjog+1
        else:
            print("Jogada inválida")
    elif x==2:
        if jogadapc==1:
            print("Jogador ganha")
            jjog=jjog+1
        elif jogadapc==2:
            print("Empate")
        elif jogadapc==3:
            print("Computador ganha")
            jpc=jpc+1
        elif jogadapc==4:
            print("Jogador ganha")
            jjog=jjog+1
        elif jogadapc==5:
            print("Computador ganha")
            jpc=jpc+1
        else:
            print("Jogada inválda")
    elif x==3:
         if jogadapc==1:
            print("Computador ganha")
            jpc=jpc+1
         elif jogadapc==2:
             print("Jogador ganha")
             jjog=jjog+1
         elif jogadapc==3:
             print("Empate")
         elif jogadapc==4:
             print("Computador ganha")
             jpc=jpc+1
         elif jogadapc==5:
             print("Jogador ganha")
             jjog=jjog+1
         else:
             print("Jogada inválida")
    elif x==4:
          if jogadapc==1:
              print("Jogador ganha")
              jjog=jjog+1
          elif jogadapc==2:
              print("Computador ganha")
              jpc=jpc+1
          elif jogadapc==3:
              print("Jogador ganha")
              jjog=jjog+1
          elif jogadapc==4:
              print("Empate")
          elif jogadapc==5:
              print("Computador ganha")
              jpc=jpc+1
          else:
              print("Jogada inválida")
    elif x==5:
           if jogadapc==1:
               print("Computador ganha")
               jpc=jpc+1
           elif jogadapc==2:
               print("Jogador ganha")
               jjog=jjog+1
           elif jogadapc==3:
               print("Computador ganha")
               jpc=jpc+1
           elif jogadapc==4:
               print("Jogador ganha")
               jjog=jjog+1
           elif jogadapc==5:
               print("Empate")
           else:
               print("Jogada inválida")
if jjog>=3:
            print("Jogador ganhou")
else:
            if jpc>=3:
                print("Computador ganhou")
               

