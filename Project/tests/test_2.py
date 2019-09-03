def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie -= 3
        return method_to_decorate(self, lie)

    return wrapper


class Lucy:
    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def sayYourAge(self, lie):
        print("Мне {} лет, а ты бы сколько дал?".format(self.age + lie))


l = Lucy()
l.sayYourAge(-3)
