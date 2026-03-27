def hanoi(n, source, helper, dest):
    if n == 1:
        print(f"Move disk 1 from {source} to {dest}")
        return
    hanoi(n-1, source, dest, helper)
    print(f"Move disk {n} from {source} to {dest}")
    hanoi(n-1, helper, source, dest)

hanoi(3, 'A', 'B', 'C')