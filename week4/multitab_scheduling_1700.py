import sys

N, K = map(int, sys.stdin.readline().split())

multitap = list(map(int, sys.stdin.readline().split()))

plugs = []
count = 0

for i in range(K):
    if multitap[i] in plugs:
        continue
    if len(plugs) < N:
        plugs.append(multitap[i])
        continue

    multitap_idxs = []
    hasplug = True

    for j in range(N):
        if plugs[j] in multitap[i + 1:]:
            multitap_idxs.append(multitap[i + 1:].index(plugs[j]))
        else:
            multitap_idxs.append(101)
            hasplug = False

        if not hasplug:
            break

    pop_idx = multitap_idxs.index(max(multitap_idxs))
    del plugs[pop_idx]
    plugs.append(multitap[i])
    count += 1

print(count)
