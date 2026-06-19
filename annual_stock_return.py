import random

def run(data, config):
    retirement = data["retirement"]
    stock_returns = retirement["stock_returns"]

    rand = random.random()
    cumulative = 0
    for entry in stock_returns:
        cumulative += entry["probability"]
        if rand <= cumulative:
            data["annual_stock_return"] = {
                "value": round(entry["return"] * 100, 2),
                "unit": "%"
            }
            break
