for i in range(1,5):
    for j in range(1,5):
        if i == j:
            continue
        for k in range(1,5):
            if k == j or k == i:
                continue
            print str(i) + str(j) + str(k)