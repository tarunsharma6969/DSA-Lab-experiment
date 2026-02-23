# move_count = global variable to count total moves
move_count = 0


# hanoi = function name
# (n) = number of disks
# source = starting rod
# auxiliary = helper rod
# destination = target rod
def hanoi(n, source, auxiliary, destination):

    # global keyword allows modification of global variable
    global move_count

    # Base Case:
    # if only 1 disk, move directly from source to destination
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        move_count += 1
        return

    # Step 1:
    # Move n-1 disks from source to auxiliary
    # destination becomes temporary helper
    hanoi(n - 1, source, destination, auxiliary)

    # Step 2:
    # Move nth disk to destination
    print(f"Move disk {n} from {source} to {destination}")
    move_count += 1

    # Step 3:
    # Move n-1 disks from auxiliary to destination
    hanoi(n - 1, auxiliary, source, destination)


# ------------------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------------------

def main():

    global move_count

    # Take input
    n = int(input("Enter number of disks: "))

    print("\n--- Tower of Hanoi Moves ---\n")

    move_count = 0

    hanoi(n, 'A', 'B', 'C')

    print("\nTotal Moves:", move_count)

    # Show formula result
    print("Expected Moves (2^n - 1):", (2 ** n) - 1)


# run program
if __name__ == "__main__":
    main()