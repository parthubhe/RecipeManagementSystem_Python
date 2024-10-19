class recipeNode:
    def __init__(self,id,name,title,image_url,time_required,ingredients,instructions):
        self.id = id
        self.title =title
        self.name =  name
        self.image_url = image_url

        self.time_required = time_required
        self.ingredients = ingredients
        self.instructions = instructions


        self.next = None
        self.prev = None

class RecipeDLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self): #need t o make the class iterable object or it will show type error
        current = self.head
        while current:
            yield current #yield is used to return each node one by one during each increment of the while loop
            current = current.next
    def traverseRecipeList(self):
        current = self.head
        while current:
            print(f"{current.id},{current.name},{current.title}")
            current = current.next
        print("eND OF LIST")

    def append(self,id,title,name,image_url,time_Requierd,ingredients,instructions):
        new_Recipe = recipeNode(id,title,name,image_url,time_Requierd,ingredients,instructions)
        if not self.head:
            self.head = new_Recipe
            self.tail =new_Recipe
        else:
            self.tail.next = new_Recipe
            new_Recipe.prev = self.tail
            self.tail = new_Recipe

    def get_recipe_by_id(self,id):
        current = self.head
        while current:
            if current.id == id:
                return current
            else:
                current = current.next
        return None

    def delete_recipe(self,id):
        current = self.head
        while current:
            if current.id == id:
                if current.prev: #if currents prev exists
                    current.prev.next = current.next
                if current.next: #if currents next exists
                    current.next.prev = current.prev
                if current == self.head: #if head node is the id(deletion at first)
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                return
        current = current.next

# recipe_list = RecipeDLL()
# recipe_list.append(1, "Spaghetti", "Italian Pasta", "img_url_1", 30, "pasta, tomatoes", "Boil pasta, make sauce.")
# recipe_list.append(2, "Salad", "Greek Salad", "img_url_2", 15, "lettuce, tomatoes, cucumber", "Chop vegetables, mix.")
# recipe_list.append(3, "Pancakes", "Breakfast Pancakes", "img_url_3", 20, "flour, eggs, milk", "Mix ingredients, fry.")
#
# # Traverse and print the list
# recipe_list.traverseRecipeList()