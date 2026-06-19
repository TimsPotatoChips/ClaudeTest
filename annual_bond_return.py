import random

def run(data, config):
    retirement = data["retirement"]
    bond_returns = retirement["bond_returns"]

    rand = random.random()
    cumulative = 0
    for entry in bond_returns:
        cumulative += entry["probability"]
        if rand <= cumulative:
            data["annual_bond_return"] = {
                "value": round(entry["return"] * 100, 2),
                "unit": "%"
            }
            break

    savings = retirement["current_savings"]
    bonds_allocation = retirement["portfolio"]["bonds_allocation"]
    bond_return_rate = data["annual_bond_return"]["value"] / 100
    total = savings * bonds_allocation * bond_return_rate
    data["total_bond_return"] = {
        "value": round(total, 2),
        "unit": "USD"
    }
