stocks = [100, 80, 60, 70, 60, 75, 85]
max_value_pos_before_checkpoint = 0
results = []
current_pos = 0
for i in range(len(stocks)):
    if i == 0:
        results = [1]
    else:
        if stocks[i] >= stocks[i -1] && stocks[i] < stocks[max_value_pos_before_checkpoint]:
            results.append(i -max_value_pos_before_checkpoint)
        elif stocks[i] <= stocks[i - 1]:
            results.append(1)
            max_value_pos_before_checkpoint = current_pos - 1
        elif stocks[i] >= stocks[i -1] && stocks[i] >= stocks[max_value_pos_before_checkpoint]:
            results.append(i -max_value_pos_before_checkpoint+results[max_value_pos_before_checkpoint])
print(results)

