class Box:
def __init__(self, width = None, height = None):
self.Width = width
self.Height = height
def __str__(self):
return f"Width = {self.Width}\n" \
f"Height = {self.Height}\n" \
f"Call super:\t" \
f"{super().__str__()}"
from box import Box
box = Box(10, 5)
print(box.__str__())