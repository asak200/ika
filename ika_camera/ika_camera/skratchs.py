from math import cos, sin
import pyperclip

number = 18
radius = 3.425
radius = 6.575

delta: float = 3.1416/number
angle = 3.1416/2

segment_length = 0.7
segment_length = 1.2
link = \
f"""    <link name="NAME">
      <pose>POSE_X POSE_Y 0.4 0 0 ANGLE</pose>
      <collision name="col1">
        <geometry>
          <box><size>0.15 {segment_length} 0.8</size></box>
        </geometry>
      </collision>
      <visual name="vis1">
        <geometry>
          <box><size>0.15 {segment_length} 0.8</size></box>
        </geometry>
      </visual>
    </link>
"""

header ="""<model name="arch">
  <static>true</static>
"""

for i in range(number+1):
    x = radius * cos(angle) - 10
    y = radius * sin(angle) + 25

    seg = link.replace('NAME', f'link_l3_{i}')
    seg = seg.replace('POSE_X', f'{x}')
    seg = seg.replace('POSE_Y', f'{y}')
    seg = seg.replace('ANGLE', f'{angle}')
    header += seg

    angle += delta

header += "</model>"
pyperclip.copy(header)
print(header)

