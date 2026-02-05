class Person:
    species = "Homo Sapiens"

    @classmethod
    def get_person(cls):
        # With this, you can access all the static methods and
        # the properties of the class
        return cls.species

    def get_name(self):
        return self.species


p = Person()
print(f"This is a person class: {p.get_person()}")


