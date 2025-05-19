from src.utils.cooking_techniques import mix, bake


def pecan_pie(*ingredients):
    print("Watch out for nut allergies")
    dough = mix(*ingredients)
    return bake(dough)

def key_lime_pie(*ingredients):
    if "lime" not in ingredients:
        print("No lime found, please check your ingredients")
    dough = mix(*ingredients)
    return bake(dough)

