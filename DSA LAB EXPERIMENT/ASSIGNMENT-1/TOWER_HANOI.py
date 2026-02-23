move_count = 0

def hanoi(n, source, auxiliary, destination):
    global move_count
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        move_count += 1
        return
    hanoi(n-1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    move_count += 1
    hanoi(n-1, auxiliary, source, destination)

hanoi(3, 'A', 'B', 'C')
print("Total moves:", move_count)