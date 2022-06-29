def read_APIkey(path: str) -> str:
    key = ''
    with open(path) as kf:
        key = kf.readline().strip()
    return key
