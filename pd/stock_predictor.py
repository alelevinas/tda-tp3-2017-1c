def calculate_best_stock_days(v):
    """
    Calculates which day it is best to buy and sell stock according to the prediction in v
    :param v: Contains the prediction of the price of the stock for day i
    :return: b, s : buying day, selling day
    """
    pos_buy_day = 0
    buy_day = 0
    sell_day = 0  # we start with 0 earnings

    for i in range(len(v)):
        if v[i] < v[buy_day]:
            pos_buy_day = i  # possible augment in winnings if i find another day later to sell at a same or higher
                             # price as now
        if v[i] > v[sell_day]:
            sell_day = i     # winnings augment

        # if actual day (selling) and possible buy day augment winnings update values
        if pos_buy_day < i and (v[i] - v[pos_buy_day]) > (v[sell_day] - v[buy_day]):
            buy_day = pos_buy_day
            sell_day = i
