stocks = [100, 80, 60, 70, 60, 75, 85]


def calculateSpan(stocks):
    max_value_pos_before_checkpoint = 0
    results = []
    camel = 0
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


print(calculateSpan(stocks))
