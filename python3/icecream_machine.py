class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        combinations = []
        for flavour in self.ingredients:
            for topping in self.toppings:
                merge = []
                merge.append(flavour)
                merge.append(topping)
                combinations.append(merge)
        return combinations

if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    print(machine.scoops()) #should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
