from src.utils.cooking_techniques import mix, bake


def pekan_pie(*ingredients):
    dough = mix(*ingredients)
    return bake(dough)

def key_lime_pie(*ingredients):
    dough = mix(*ingredients)
    return bake(dough)
