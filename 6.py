dept1 = set(map(int, input().split()))
dept2 = set(map(int, input().split()))
dept3 = set(map(int, input().split()))
all_ids = set(range(0, 11))
present = dept1 | dept2 | dept3
ghosts = sorted(all_ids - present)
print(' '.join(map(str, ghosts)))
