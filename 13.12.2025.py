import time
radius = {
    1: "🟨",
    5: "🟩🟩🟩🟩🟩",
    3: "🟥🟥🟥",
    2: "🟦🟦",
    4: "🟧🟧🟧🟧",
    0: "|"
}
final = 0
count = 0
global_wait_timer = 0
def show_towers(towers, radius, global_timer, start = True):
    global count, global_wait_timer
    if start:
        print(" 🟨 - 1 см\n",
            "🟦 - 2 см\n",
            "🟥 - 3 см\n",
            "🟧 - 4 см\n",
            "🟩 - 5 см")
    if count == 0:
        print("Башни: ")
    else:
        print(f"\nХод: {count}")
    for x in range(len(towers)):
        print(f"\n\n{x + 1}\n\n")
        for space in range(5 - len(towers[x])):
            print("|\n|")
        for y in range(len(towers[x])):
            if y + 1 > 1:
                print(f"|\n{radius[towers[x][y]]}")
            elif y + 1 == 1:
                print(f"{radius[towers[x][y]]}")
    if len(towers[final]) == 5:
        print(f"\nУшло времени: {time.time() - (global_timer + global_wait_timer)}")
        print(f"Ушло ходов: {count}")
        return
    count += 1

        
        
def change_up_disk(count_disk, main, help, final, towers, radius,global_timer):
    global global_wait_timer
    if count_disk == 0:
        return
    change_up_disk(count_disk - 1, main, final, help, towers, radius,global_timer)
    timer1 = time.time()
    input("Нажмите enter для следующего шага: ")
    global_wait_timer += time.time() - timer1
    towers[final].insert(0, towers[main][0])
    towers[main].pop(0)
    show_towers(towers,radius,global_timer, start=False)
    return change_up_disk(count_disk - 1, help, main, final, towers, radius,global_timer)

def choose_tower(count_disk):
    global final
    towers = [
        [],
        [],
        []
    ]
    main = 0
    while True:
        main = int(input("Введите номер башни с дисками от 1 до 3: ")) - 1
        if main >= 0 and main < 3:
            break
    final = 2
    while True:
        final = int(input("Введите номер башни на которую нужно положить диски от 1 до 3: ")) - 1
        if final >= 0 and final < 3 and final != main:
            break
        elif final >= 0 and final < 3 and final == main:
            print("Вы ввели номер конечной башни схожий с номером начальной башни")
    help = 3 - main - final
    towers[main] = [i for i in range(1, count_disk+1)]
    global_timer = time.time()
    show_towers(towers, radius, global_timer=global_timer)
    change_up_disk(count_disk, main, help, final, towers, radius, global_timer)
    
choose_tower(5)