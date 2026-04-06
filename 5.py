log1 = input().split()
log2 = input().split()
log3 = input().split()
set1, set2, set3 = set(log1), set(log2), set(log3)
all_ips = set1 | set2 | set3
common_all = set1 & set2 & set3
result = sorted(all_ips - common_all)
print(' '.join(result))
