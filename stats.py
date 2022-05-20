def fourStats(data, header):
    sum = round(data[header].sum(), 2)
    mean = round(data[header].mean(), 2)
    min = round(data[header].min(), 2)
    max = round(data[header].max(), 2)
    std = round(data[header].std(), 2)
    return {
        "sum": sum,
        "mean": mean,
        "min": min,
        "max": max,
        "std": std
    }