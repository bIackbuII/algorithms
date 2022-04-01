def twosum_extra_ds(cnt_chips, chips, answer):
    previous = set()
    for chip in chips:
        Y = answer - chip
        if Y in previous:
            return "{} {}".format(chip, Y)
        else:
            previous.add(chip)
    return None
print(twosum_extra_ds(int(input()), list(map(int, input().split())), int(input())))