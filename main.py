from stock_span_calc import StockSpan


def main(filepath):
    s = StockSpan(filepath=filepath)
    values = s.read_stock_values()
    results = s.calculateSpan(values)


main()
