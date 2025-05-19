from src.utils.cooking_techniques import mix, bake

def banana_cake(*ingredients):
    dough = mix(*ingredients)
    return bake(dough)

def cheesecake(*ingredients):
    dough = mix(*ingredients)
    return bake(dough)

def pekan_pie(*ingredients):
    dough = mix(*ingredients)
    return bake(dough)


def cake(*ingredients, cake_name=""):
    dough = mix(*ingredients)
    return f"{bake(dough)}for {cake_name}"