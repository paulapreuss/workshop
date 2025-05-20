from src.utils.cooking_techniques import mix, bake


def pecan_pie(*ingredients):
    dough = mix(*ingredients)
    return bake(dough)

def key_lime_pie(*ingredients):
    if "lime" not in ingredients:
        print("Lime missing")
    dough = mix(*ingredients)
    return bake(dough)
