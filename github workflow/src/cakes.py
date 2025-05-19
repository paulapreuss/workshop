from src.utils.cooking_techniques import mix, bake

def banana_cake(*ingredients):
    if "banana" not in ingredients:
        print("oh no, that's so sad :(")
    dough = mix(*ingredients)
    return bake(dough)

def cheesecake(*ingredients):
    print("watch out for lactose intolerance")
    dough = mix(*ingredients)
    return bake(dough)

