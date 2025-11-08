def print_towers(towers, num_disks):
    # Print the towers as ASCII art
    for level in range(num_disks, 0, -1):
        row = ""
        for rod in ['A', 'B', 'C']:
            if len(towers[rod]) >= level:
                disk = towers[rod][level - 1]
                row += " " * (num_disks - disk) + "=" * (disk * 2 - 1) + " " * (num_disks - disk) + "  "
            else:
                row += " " * (num_disks - 1) + "|" + " " * (num_disks - 1) + "  "
        print(row)
    print("  A" + " " * (num_disks * 2 - 2) + "   B" + " " * (num_disks * 2 - 2) + "   C\n")

def Tower(n, source, target, auxiliary, towers, num_disks, step_counter):
    if n == 1:
        disk = towers[source].pop()
        towers[target].append(disk)
        step_counter[0] += 1
        print(f"Step {step_counter[0]}: Move disk 1 from {source} to {target}")
        print_towers(towers, num_disks)
        return
    Tower(n - 1, source, auxiliary, target, towers, num_disks, step_counter)
    disk = towers[source].pop()
    towers[target].append(disk)
    step_counter[0] += 1
    print(f"Step {step_counter[0]}: Move disk {n} from {source} to {target}")
    print_towers(towers, num_disks)
    Tower(n - 1, auxiliary, target, source, towers, num_disks, step_counter)

# Example usage:
num_disks = 3
towers = {'A': list(range(num_disks, 0, -1)), 'B': [], 'C': []}
step_counter = [0]
print_towers(towers, num_disks)
Tower(num_disks, 'A', 'C', 'B', towers, num_disks, step_counter)
print(f"Total steps: {step_counter[0]}")
