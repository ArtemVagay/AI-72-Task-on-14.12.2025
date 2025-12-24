import time
radius = {
    0: "🟨",
    4: "🟩🟩🟩🟩🟩",
    2: "🟥🟥🟥",
    1: "🟦🟦",
    3: "🟧🟧🟧🟧",
}
iteration = 1
global_wait_timer = 0
global_timer = 0
def show_towers(target_tower):
    global iteration, main_pos, radius
    if iteration != 0:
        print(f"\nХод: {iteration}")
    print("1\t\t2\t\t3")
    for i, disk in enumerate(main_pos):
        print("\t\t" * disk + radius[i])
    iteration += 1
    
def change_up_disk(n, target_tower):
    global global_wait_timer, main_pos, global_timer
    if n == 0:
        return
    disk_index = n - 1
    tower_with_biggest_disk = main_pos[disk_index]
    if tower_with_biggest_disk == target_tower:
        change_up_disk(n - 1, target_tower)
    else:
        help_tower = 3 - tower_with_biggest_disk - target_tower
        change_up_disk(n - 1, help_tower)
        main_pos[n - 1] = target_tower
        timer = time.time()
        input("Нажмите enter для следующего хода: ")
        global_wait_timer += time.time() - timer
        show_towers(target_tower)
        change_up_disk(n - 1, target_tower)
            


def choose_tower(count_disk):
    global main_pos, radius, global_timer
    for i in range(5):
        while True:
            tower = int(input(f"Введите башню для {radius[4 - i]}: ")) - 1
            if tower >= 0 and tower < 3:
                main_pos.insert(0, tower)
                break
    final = 2
    while True:
        final = int(input("Введите номер башни на которую нужно положить диски от 1 до 3: ")) - 1
        if final >= 0 and final < 3:
            break
        elif final >= 0 and final < 3:
            print("Вы ввели номер конечной башни схожий с номером начальной башни")
    global_timer = time.time()
    show_towers(final)
    change_up_disk(count_disk, final)


print(" 🟨 - 1 см\n",
            "🟦 - 2 см\n",
            "🟥 - 3 см\n",
            "🟧 - 4 см\n",
            "🟩 - 5 см")

main_pos = []
choose_tower(5)
print(f"\nВсего ушло {iteration} ходов")
print(f"Всего ушло {time.time() - global_timer - global_wait_timer} времени")