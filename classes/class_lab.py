class age(object):
    name = 'Oskon'
    def __init__(self,a):
        self.add=a


    def pr(self):
        return self.add
    @staticmethod
    def Man(age):
        if age>18:
            return ('Совершеннолетний')
        else:
            return 'не совершенно летний'
    @classmethod
    def hiring(cls):
        print(f'Hello{cls.name}')
        return cls.add
class ageOskon(age):
    pass

aser=age(12)

print(aser.name)
print(aser.pr())
print(aser.hiring())
