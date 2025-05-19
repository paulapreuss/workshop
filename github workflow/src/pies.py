from src.utils.cooking_techniques import mix, bake


def pecan_pie(*ingredients):
    print("Watch out for nut allergies")
    dough = mix(*ingredients)
    return bake(dough)

def key_lime_pie(*ingredients):
    if "lime" not in ingredients:
        print("this is going to be a problem :(")
    dough = mix(*ingredients)
    return bake(dough)

