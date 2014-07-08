class gameobject:
  def __init__(self, name, health, damage):
    self.name = name
    self.health = health
    self.damage = damage

class player:
  def __init__(self):
    items_list = []
    skills_list = []
    health = 50
    damage = 5
    items_list.append(item("Frozen Heart", """UNIQUE: Reduces the attack speed
    of nearby enemies by 15%. (700 range)"""))
    skills_list.append(skill("Baleful Strike", 10))

class item:
  def __init__(self, name, description):
    self.name = name
    self.description = description

class skill:
  def __init__(self, name, damage):
    self.name = name
    self.damage = damage
