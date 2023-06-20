

def parse_config(filename: str = "config.toml") -> dict:
    import tomli
    with open(filename, mode="rb") as fp:
        config = tomli.load(fp)
    return config




