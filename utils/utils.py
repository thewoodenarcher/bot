def slice_text(text: str, limit = 2048, suffix = "..."):
    if len(text) < limit:
        return text
    if suffix and type(suffix) == str:
        return text[:limit - len(suffix)] + suffix
    else:
        return text[:limit]

def capitalize(msg: str):
    res = []
    snakes = msg.split("_")
    for x in snakes:
        res.append(x.title())
    return " ".join(res)
