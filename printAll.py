def run(data, config):
    for key, val in data.items():
        print(f"{key}: {val['value']} {val['unit']}")
