import random


def lotto_45(wieoft, wieviel):
    list = []
    list.extend(range(1, wieviel))
    winning_numbers = random.sample(list, wieoft)
    return winning_numbers


def statistic():
    stat_dic = {}
    for i in range(1000):
        v = lotto_45(1, 46)[0]  # [0] um das erste element der liste zu bekommen , funfact [-1] ist es letzte elem
        stat_dic.update({i: v})
    return stat_dic


if __name__ == "__main__":
    # Aufgabe 1
    print(lotto_45(6, 46))
    ##Aufgabe 2
    print(statistic())
    #stat_dic = statistic()
    # print(stat_dic)

    # Add some spice https://www.python-graph-gallery.com/all-charts/
    # pip3 install matplotlib
    ##import matplotlib.pyplot as plt

    #plt.rcParams["figure.figsize"] = (10, 6)
    #plt.plot(stat_dic.keys(), stat_dic.values(), linestyle="-", label="Statistic")
    #plt.legend()
    #plt.show()
