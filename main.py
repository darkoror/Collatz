from operator import itemgetter


def result(lowest_number, highest_number: int, top: int):
    all_results = {}
    all_len = {}

    for num in range(lowest_number, highest_number + 1):
        res_list = col(num)
        res_list = [i for i in res_list if i % 2 == 1]

        all_results[num] = res_list
        all_len[num] = len(res_list)

    sorted_result = sorted(all_len.items(), key=itemgetter(1), reverse=True)

    for index, value in list(enumerate(sorted_result))[:top]:
        number, length = value
        print(
            f"{index + 1}. {number} ({length}): {all_results[number]}\n"
        )


def col(n):
    sp = [n]

    if n < 1:
        return []

    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sp.append(n)

    return sp


if __name__ == '__main__':
    result(3, 100, 12)
