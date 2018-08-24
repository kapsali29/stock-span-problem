import pandas


class StockSpan(object):
    """The class StockSpan contains methods that load a list or csv with stocks and computes the stock-span problem"""

    def __init__(self, filepath):
        self.filepath = filepath
        self.stocks = pandas.read_csv(self.filepath)

    def read_stock_values(self):
        values = list(self.stocks["VALUE"])
        print(values)
        return values

    def calculateSpan(self, values):
        """
        The method compute the daily stock span.
        :return: results
        """
        max_value_pos_before_checkpoint = 0
        results = []
        camel = 0
        stocks = values
        for i in range(len(stocks)):
            if i == 0:
                camel = 1
                results = [1]
            else:
                if stocks[i] >= stocks[i - 1] and stocks[i] < stocks[max_value_pos_before_checkpoint]:
                    results.append(i - max_value_pos_before_checkpoint)
                elif stocks[i] < stocks[i - 1]:
                    results.append(1)
                    if stocks[max_value_pos_before_checkpoint] > stocks[i - 1]:
                        camel += results[max_value_pos_before_checkpoint]
                    max_value_pos_before_checkpoint = i - 1
                elif stocks[i] >= stocks[i - 1] and stocks[i] >= stocks[max_value_pos_before_checkpoint]:
                    results.append(i - max_value_pos_before_checkpoint + camel)
        return results

