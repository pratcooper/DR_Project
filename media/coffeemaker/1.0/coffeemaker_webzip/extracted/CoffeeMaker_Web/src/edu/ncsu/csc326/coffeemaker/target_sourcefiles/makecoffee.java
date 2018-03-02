Returns the change of a user's beverage purchase, or the user's money if the beverage cannot be made
public synchronized int makeCoffee(int recipeToPurchase, int amtPaid) {
    int change = 0;
    if (getRecipes()[recipeToPurchase] == null) {
      change = amtPaid;
    } else if (getRecipes()[recipeToPurchase].getPrice() <= amtPaid) {
      if (inventory.useIngredients(getRecipes()[recipeToPurchase])) {
        change = amtPaid - getRecipes()[recipeToPurchase].getPrice();
      } else {
        change = amtPaid;
      }
    } else {
      change = amtPaid;
    }
    return change;