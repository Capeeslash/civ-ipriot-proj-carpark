

def parse_config(config) -> dict:
    import tomli
    with open(config, mode="rb") as fp:
        config = tomli.load(fp)
    return config




