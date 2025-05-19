from src.utils.cooking_techniques import mix, bake


def pecan_pie(*ingredients):
    dough = mix(*ingredients)
    return bake(dough)

def key_lime_pie(*ingredients):
    if "lime" not in ingredients:
        print("oh no, that's so sad :(")
    dough = mix(*ingredients)
    return bake(dough)
