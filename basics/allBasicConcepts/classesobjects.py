# Python supports object-oriented programming (OOP). Classes are blueprints for objects.

class test_case:
    def __init__(self,name):
        self.name = name

    def run(self):
        print(f"runnning test as {self.name}")

ob = test_case("vinay")
ob.run()


class some:
    def __init__(self):
        pass

    def nav(self):
        return "https://"

obs = some()
print(obs.nav())