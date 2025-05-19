from src.utils.cooking_techniques import mix, bake

def banana_cake(*ingredients):
    if "banana" not in ingredients:
        print("this is going to be a problem :(")
    dough = mix(*ingredients)
    return bake(dough)

def cheesecake(*ingredients):
    print("Watch out for lactose intolerance")
    dough = mix(*ingredients)
    return bake(dough)

def cake(*ingredients, cake_name=""):
    dough = mix(*ingredients)
    return f"{bake(dough)}for {cake_name}"