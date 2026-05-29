import random

bingo = random.randint(1, 100)
print("================================================")
count = 0
while True:
    count += 1
    guess = int(input(f"Lần đoán {count}: Nhập số của bạn: "))
    if guess == bingo: 
        print("chúc mừng bạn đã đoán đúng số may mắn")
        print("trò chơi kết thúc")
        break