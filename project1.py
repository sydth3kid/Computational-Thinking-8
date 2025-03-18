###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("summer")

q1 = codesters.Square(100, 100, 200, 'RoyalBlue')
q2 = codesters.Square(-100, 100, 200, 'Navy')
q3 = codesters.Square(-100, -100, 200, 'SkyBlue')
q4 = codesters.Square(100, -100, 200, 'PowderBlue')

s1 = codesters.Sprite("PSBnb", 100, 100)
s1.set_size(0.5)
s2 = codesters.Sprite("ghost", -100, -100)
s2.set_size(0.5)
s3 = codesters.Sprite("ramen", 100, -100)
s3.set_size(0.1)
s4 = codesters.Sprite("roblox", -100, 100)
s4.set_size(0.5)

message1 = codesters.Text("Sydney Fiona Frank", 0, 210, "black")
message2 = codesters.Text("sup", 0, -210, "black")