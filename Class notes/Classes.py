class Fruit:
    # fruit_type: str
    # color: str
    # is_seedless: bool
    # contition: str

    def __init__(self, fruit_type, color, is_seedless, age):
        self.fruit_type = str(fruit_type)
        self.color = str(color)
        if self.color not in ['red', 'green', 'blue', 'yellow', 'orange']:
            raise Exception('cannot instantiate fruit of unknow color')
        self.is_seedless =  bool(is_seedless)
        self.age = int(age)

    def __str__(self): #a private method. We don't call it directly from the outside of the class, invoked when the object is printed
        fruit_str = f"This is a {self.fruit_type} with a {self.color} color"
        return fruit_str
    
    def foo(self):
        print("foo method in fruit")
    
def foo(some_fruit):
    print("global foo showing this fruit:", some_fruit.fruit_type)
    
    #self is a pointer to the object that is passed to the methods of the class
    #the method then uses the self pointer to access the object

if __name__ == "__main__":
    apple = Fruit(fruit_type="apple", color="red", is_seedless=False, age=5)

    # apple = Fruit()
    # apple.fruit_type = "apple"
    # apple.color = "red"
    # =procedural code involving an object i.e. passing an object to a function
    foo(apple) #calling global foo

    #object-oriented code - an object invoking its member method
    apple.foo() #object apple is incoking its member method foo

    orange = Fruit()
    orange.fruit_type = "orange"
    orange.color = orange
    print(apple)