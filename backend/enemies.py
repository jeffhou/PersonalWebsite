class Pillow:
  def __init__(self):
    self.name = "pillow"
    self.img_url = "../static/pillow.jpg"
    self.desc = "Oh my! It's a giant monster! Let's fight it!"
    self.health = 10
    self.damage = 1
    self.damage_message = "It falls over on you. Ow. That hurts."
  def is_dead(self):
    return not self.health > 0
  def is_alive(self):
    return self.health > 0
