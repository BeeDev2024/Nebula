codes = """
** This is a comment
DISP Hiya World
s = Sun(20, 2, 'Made-up sun')
x = Planet('Xzyskahdxyz', 2.5, 23, 15, -100, 'Made-up planet')
t = Planet('Tjokobidzyx', 40, 100, 1, 200, 'Made-up planet')
s.sunprint()
x.planetprint()
t.planetprint()

life = Lifeform('Microbial', 'Water', 'Well, if you haven't got the memo this isn't real...')
life.lifeprint()
"""

class Planet:
    def __init__(self, name, radius, circumference, position, normal_temperature, notes):
        self.name = name
        self.radius = radius
        self.circumference = circumference
        self.position = position
        self.normal_temperature = normal_temperature
        self.notes = notes
    def planetprint(self):
        print(f"Planet name: {self.name}, Radius: {self.radius}, Circumference: {self.circumference}, Position from its sun: {self.position}, Normal temperature: {self.normal_temperature}°C, Notes: {self.notes}")

class Sun:
    def __init__(self, temperature, size, notes):
        self.temperature = float(temperature)
        self.solarradii = float(size)
        self.notes = notes
    def sunprint(self):
        print(f"Sun temperature: {self.temperature}, Size (in solar radii): {self.solarradii}, Notes: {self.notes}")

class Lifeform:
    def __init__(self, type, habitat, notes):
        self.type = type
        self.habitat = habitat
        self.notes = notes
    def lifeprint(self):
        print(f"Life form type: {self.type}, Habitat: {self.habitat}, Notes: {self.notes}")

class Interpreter:
    def __init__(self, code):
        self.planets = []
        self.sun = None
        self.life_forms = []
        self.current_line = 0
        self.code = code.splitlines()
    def execute(self):
        for line in self.code:
            if line.startswith("DISP"):
                disp = line.split()
                disp.pop(0)
                print(" ".join(disp))
            elif line.startswith("**"):
                pass
            else:
                print("!ERR ERR ERR ERR!")
            self.current_line += 1
            
i = Interpreter(codes)
i.execute()
