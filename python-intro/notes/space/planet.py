class Planet:

    shape = 'round' #these are class level attribute - same for all instances
    
    def __init__(self, name, radius, gravity, system):
        self.name = name #these are instance attributes
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self): #these are instance methods
        return f'{self.name} is orbiting in the {self.system}'
    
    @classmethod #these are class level methods
    def commons(cls):
        return f'All planets are {cls.shape}'
    
    @staticmethod #doesnt have access to self or class, only has access to parameters we pass into it individually
    def spin(speed = '2000 miles per hour'):
        return f'The planet spins {speed}'