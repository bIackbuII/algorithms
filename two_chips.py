def make_anwer(cnt_chips, chips, answer):
    for i in range(cnt_chips):
        for j in range(i+1, cnt_chips):
            if chips[i] + chips[j] == answer:
                return "{} {}".format(chips[i], chips[j])
    return None

print(make_anwer(int(input()), list(map(int, input().split())), int(input())))