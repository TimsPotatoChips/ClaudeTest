def run(data, config):
    for key, val in data.items():
        if isinstance(val, dict) and "value" in val and "unit" in val:
            print(f"{key}: {val['value']} {val['unit']}")
