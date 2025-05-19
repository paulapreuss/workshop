from src.utils.cooking_techniques import mix, bake

def banana_cake(*ingredients):
    dough = mix(*ingredients)
    return bake(dough)

def cheesecake(*ingredients):
    print("watch out for lactose intolerance")
    dough = mix(*ingredients)
    return bake(dough)

def pekan_pie(*ingredients):
    print("watch out for nut allergies")
    dough = mix(*ingredients)
    return bake(dough)

def key_lime_pie(*ingredients):
    dough = mix(*ingredients)
    return bake(dough)
