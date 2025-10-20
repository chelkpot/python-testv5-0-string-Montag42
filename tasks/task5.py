# tasks/task5.py

def solve():
# Ниже пишите решение задачи
    BIG_SHOT = input().split()
    for GUNGADERO in BIG_SHOT:
        SPAMPTON = ord(GUNGADERO)
        print("Код символа " + GUNGADERO + " равен " + str(SPAMPTON))
    
   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()