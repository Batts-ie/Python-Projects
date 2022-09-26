import random


def lotto_45(wieoft, wieviel): # 2 params for the second task
    list = []
    list.extend(range(1, wieviel))
    winning_numbers = random.sample(list, wieoft)
    return winning_numbers


def statistic():
    stat_dic = {}
    for i in range(1000):
        v = lotto_45(1, 46)[0]  # [0] um das erste Element der Liste zu bekommen,[-1] ist das letzte Elem
        stat_dic.update({i: v})
    return stat_dic


if __name__ == "__main__":
    # Aufgabe 1
    print(lotto_45(6, 46))
    ##Aufgabe 2
    print(statistic())
    stat_dic = statistic()
    #print(stat_dic)

    # extra task: plot - https://www.python-graph-gallery.com/all-charts/
    # pip3 install matplotlib==3.5.3
    import matplotlib.pyplot as plt

    plt.rcParams["figure.figsize"] = (10, 6)
    plt.plot(stat_dic.keys(), stat_dic.values(), color="lightgreen", linestyle="-", label="Statistic")
    plt.legend()
    plt.show()
