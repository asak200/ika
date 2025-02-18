from math import cos, sin
import pyperclip
from random import randint, random

### CREATE AN ARCH
# number = 18
# radius = 3.425
# radius = 6.575

# delta: float = 3.1416/number
# angle = 3.1416/2

# segment_length = 0.7
# segment_length = 1.2
# link = \
# f"""    <link name="NAME">
#       <pose>POSE_X POSE_Y 0.4 0 0 ANGLE</pose>
#       <collision name="col1">
#         <geometry>
#           <box><size>0.15 {segment_length} 0.8</size></box>
#         </geometry>
#       </collision>
#       <visual name="vis1">
#         <geometry>
#           <box><size>0.15 {segment_length} 0.8</size></box>
#         </geometry>
#       </visual>
#     </link>
# """

# header ="""<model name="arch">
#   <static>true</static>
# """

# for i in range(number+1):
#     x = radius * cos(angle) - 10
#     y = radius * sin(angle) + 25

#     seg = link.replace('NAME', f'link_l3_{i}')
#     seg = seg.replace('POSE_X', f'{x}')
#     seg = seg.replace('POSE_Y', f'{y}')
#     seg = seg.replace('ANGLE', f'{angle}')
#     header += seg

#     angle += delta

# header += "</model>"
# pyperclip.copy(header)
# print(header)

### CHANGE THE POSITION
# text = """        <link name='Wall_1_0'>
#           <pose>0.0 -6.925 0.0 0.0 -0.0 0.0</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='Wall_1_1'>
#           <pose>0.0 -10.075 0.0 0.0 -0.0 0.0</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='Wall_2_0'>
#           <pose>0.0 3.0749999999999993 0.0 0.0 -0.0 0.0</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='Wall_2_1'>
#           <pose>0.0 -0.07499999999999929 0.0 0.0 -0.0 0.0</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='Wall_3_0'>
#           <pose>0.0 13.075 0.0 0.0 -0.0 0.0</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='Wall_3_1'>
#           <pose>0.0 9.925 0.0 0.0 -0.0 0.0</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='Wall_4_0'>
#           <pose>0.0 23.075 0.0 0.0 -0.0 0.0</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='Wall_4_1'>
#           <pose>0.0 19.925 0.0 0.0 -0.0 0.0</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_0'>
#           <pose>-10.0 3.0749999999999993 0.4 0.0 -0.0 1.5708</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_1'>
#           <pose>-11.1418 2.9750999999999994 0.4 0.0 -0.0 1.74533</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_10'>
#           <pose>-16.4751 -4.64179 0.4 0.0 0.0 -2.96705</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_11'>
#           <pose>-16.1785 -5.74883 0.4 0.0 0.0 -2.79252</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_12'>
#           <pose>-15.694099999999999 -6.7875499999999995 0.4 0.0 0.0 -2.61799</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_13'>
#           <pose>-15.0367 -7.726374 0.4 0.0 0.0 -2.44345</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_14'>
#           <pose>-14.226299999999998 -8.536782 0.4 0.0 0.0 -2.26892</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_15'>
#           <pose>-13.287400000000002 -9.194149 0.4 0.0 0.0 -2.09438</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_16'>
#           <pose>-12.2487 -9.6785 0.4 0.0 0.0 -1.91985</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_17'>
#           <pose>-11.1417 -9.97512 0.4 0.0 0.0 -1.74532</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_18'>
#           <pose>-9.9999 -10.075 0.4 0.0 0.0 -1.57079</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_2'>
#           <pose>-12.2488 2.6784999999999997 0.4 0.0 -0.0 1.91987</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_3'>
#           <pose>-13.287500000000001 2.1941000000000006 0.4 0.0 -0.0 2.0944</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_4'>
#           <pose>-14.226400000000002 1.5366999999999997 0.4 0.0 -0.0 2.26893</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_5'>
#           <pose>-15.0368 0.7263000000000002 0.4 0.0 -0.0 2.44347</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_6'>
#           <pose>-15.694099999999999 -0.21254000000000062 0.4 0.0 -0.0 2.618</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_7'>
#           <pose>-16.1785 -1.2512600000000003 0.4 0.0 -0.0 2.79253</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_8'>
#           <pose>-16.4751 -2.3583100000000004 0.4 0.0 -0.0 2.96707</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_9'>
#           <pose>-16.575 -3.50005 0.4 0.0 0.0 -3.14159</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l2_0'>
#           <pose>9.99998 -0.07499999999999929 0.4 0.0 0.0 -1.5708</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l2_1'>
#           <pose>11.1417 0.02487999999999957 0.4 0.0 0.0 -1.39627</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l2_10'>
#           <pose>16.4751 7.6417 0.4 0.0 -0.0 0.174533</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l2_11'>
#           <pose>16.1785 8.7488 0.4 0.0 -0.0 0.349067</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l2_12'>
#           <pose>15.694099999999999 9.787500000000001 0.4 0.0 -0.0 0.5236</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l2_13'>
#           <pose>15.0367 10.726299999999998 0.4 0.0 -0.0 0.698133</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l2_14'>
#           <pose>14.2263 11.5368 0.4 0.0 -0.0 0.872667</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l2_15'>
#           <pose>13.2875 12.194099999999999 0.4 0.0 -0.0 1.0472</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l2_16'>
#           <pose>12.2488 12.6785 0.4 0.0 -0.0 1.22173</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l2_17'>
#           <pose>11.1417 12.975100000000001 0.4 0.0 -0.0 1.39627</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l2_18'>
#           <pose>9.99998 13.075 0.4 0.0 -0.0 1.5708</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l2_2'>
#           <pose>12.2488 0.32150999999999996 0.4 0.0 0.0 -1.22173</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l2_3'>
#           <pose>13.2875 0.8058800000000002 0.4 0.0 0.0 -1.0472</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l2_4'>
#           <pose>14.2263 1.4632500000000004 0.4 0.0 0.0 -0.872667</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l2_5'>
#           <pose>15.0367 2.2737 0.4 0.0 0.0 -0.698133</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l2_6'>
#           <pose>15.694099999999999 3.2125000000000004 0.4 0.0 0.0 -0.5236</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l2_7'>
#           <pose>16.1785 4.251200000000001 0.4 0.0 0.0 -0.349067</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l2_8'>
#           <pose>16.4751 5.3583 0.4 0.0 0.0 -0.174533</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l2_9'>
#           <pose>16.575 6.5 0.4 0.0 -0.0 0.0</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l3_0'>
#           <pose>-10.0 23.075 0.4 0.0 -0.0 1.5708</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l3_1'>
#           <pose>-11.1418 22.9751 0.4 0.0 -0.0 1.74533</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l3_10'>
#           <pose>-16.4751 15.3582 0.4 0.0 0.0 -2.96705</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l3_11'>
#           <pose>-16.1785 14.2512 0.4 0.0 0.0 -2.79252</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l3_12'>
#           <pose>-15.694099999999999 13.212499999999999 0.4 0.0 0.0 -2.61799</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l3_13'>
#           <pose>-15.0367 12.273599999999998 0.4 0.0 0.0 -2.44345</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l3_14'>
#           <pose>-14.226299999999998 11.4632 0.4 0.0 0.0 -2.26892</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l3_15'>
#           <pose>-13.287400000000002 10.805900000000001 0.4 0.0 0.0 -2.09438</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l3_16'>
#           <pose>-12.2487 10.3215 0.4 0.0 0.0 -1.91985</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l3_17'>
#           <pose>-11.1417 10.024899999999999 0.4 0.0 0.0 -1.74532</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l3_18'>
#           <pose>-9.9999 9.925 0.4 0.0 0.0 -1.57079</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l3_2'>
#           <pose>-12.2488 22.6785 0.4 0.0 -0.0 1.91987</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l3_3'>
#           <pose>-13.287500000000001 22.1941 0.4 0.0 -0.0 2.0944</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l3_4'>
#           <pose>-14.226400000000002 21.5367 0.4 0.0 -0.0 2.26893</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l3_5'>
#           <pose>-15.0368 20.7263 0.4 0.0 -0.0 2.44347</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l3_6'>
#           <pose>-15.694099999999999 19.7875 0.4 0.0 -0.0 2.618</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l3_7'>
#           <pose>-16.1785 18.7487 0.4 0.0 -0.0 2.79253</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l3_8'>
#           <pose>-16.4751 17.6417 0.4 0.0 -0.0 2.96707</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_l3_9'>
#           <pose>-16.575 16.5 0.4 0.0 0.0 -3.14159</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s1_0'>
#           <pose>-10.0 -0.07499999999999929 0.4 0.0 -0.0 1.5708</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s1_1'>
#           <pose>-10.5948 -0.12703999999999915 0.4 0.0 -0.0 1.74533</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s1_10'>
#           <pose>-13.373000000000001 -4.09477 0.4 0.0 0.0 -2.96705</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s1_11'>
#           <pose>-13.218399999999999 -4.6714400000000005 0.4 0.0 0.0 -2.79252</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s1_12'>
#           <pose>-12.9661 -5.21252 0.4 0.0 0.0 -2.61799</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s1_13'>
#           <pose>-12.6237 -5.70157 0.4 0.0 0.0 -2.44345</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s1_14'>
#           <pose>-12.2015 -6.1237200000000005 0.4 0.0 0.0 -2.26892</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s1_15'>
#           <pose>-11.712499999999999 -6.46615 0.4 0.0 0.0 -2.09438</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s1_16'>
#           <pose>-11.171399999999998 -6.71846 0.4 0.0 0.0 -1.91985</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s1_17'>
#           <pose>-10.5947 -6.8729700000000005 0.4 0.0 0.0 -1.74532</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s1_18'>
#           <pose>-10.0 -6.925 0.4 0.0 0.0 -1.57079</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s1_2'>
#           <pose>-11.171399999999998 -0.2815600000000007 0.4 0.0 -0.0 1.91987</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s1_3'>
#           <pose>-11.712499999999999 -0.5338700000000003 0.4 0.0 -0.0 2.0944</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s1_4'>
#           <pose>-12.2016 -0.8763100000000001 0.4 0.0 -0.0 2.26893</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s1_5'>
#           <pose>-12.6237 -1.29847 0.4 0.0 -0.0 2.44347</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s1_6'>
#           <pose>-12.9661 -1.7875199999999998 0.4 0.0 -0.0 2.618</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s1_7'>
#           <pose>-13.218499999999999 -2.3286 0.4 0.0 -0.0 2.79253</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s1_8'>
#           <pose>-13.373000000000001 -2.9052800000000003 0.4 0.0 -0.0 2.96707</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s1_9'>
#           <pose>-13.425 -3.50002 0.4 0.0 0.0 -3.14159</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s2_0'>
#           <pose>9.99999 3.0749999999999993 0.4 0.0 0.0 -1.5708</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s2_1'>
#           <pose>10.5947 3.1270000000000007 0.4 0.0 0.0 -1.39627</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s2_10'>
#           <pose>13.373000000000001 7.0947 0.4 0.0 -0.0 0.174533</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s2_11'>
#           <pose>13.218399999999999 7.671399999999998 0.4 0.0 -0.0 0.349067</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s2_12'>
#           <pose>12.9661 8.212499999999999 0.4 0.0 -0.0 0.5236</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s2_13'>
#           <pose>12.6237 8.7016 0.4 0.0 -0.0 0.698133</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s2_14'>
#           <pose>12.2015 9.1237 0.4 0.0 -0.0 0.872667</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s2_15'>
#           <pose>11.7125 9.4661 0.4 0.0 -0.0 1.0472</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s2_16'>
#           <pose>11.1714 9.718499999999999 0.4 0.0 -0.0 1.22173</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s2_17'>
#           <pose>10.5947 9.873000000000001 0.4 0.0 -0.0 1.39627</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s2_18'>
#           <pose>9.99999 9.925 0.4 0.0 -0.0 1.5708</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s2_2'>
#           <pose>11.1714 3.2814999999999994 0.4 0.0 0.0 -1.22173</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s2_3'>
#           <pose>11.7125 3.533899999999999 0.4 0.0 0.0 -1.0472</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s2_4'>
#           <pose>12.2015 3.8763000000000005 0.4 0.0 0.0 -0.872667</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s2_5'>
#           <pose>12.6237 4.298400000000001 0.4 0.0 0.0 -0.698133</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s2_6'>
#           <pose>12.9661 4.7875 0.4 0.0 0.0 -0.5236</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s2_7'>
#           <pose>13.218399999999999 5.3286 0.4 0.0 0.0 -0.349067</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s2_8'>
#           <pose>13.373000000000001 5.9053 0.4 0.0 0.0 -0.174533</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s2_9'>
#           <pose>13.425 6.5 0.4 0.0 -0.0 0.0</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s3_0'>
#           <pose>-10.0 19.925 0.4 0.0 -0.0 1.5708</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s3_1'>
#           <pose>-10.5948 19.873 0.4 0.0 -0.0 1.74533</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s3_10'>
#           <pose>-13.373000000000001 15.9052 0.4 0.0 0.0 -2.96705</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s3_11'>
#           <pose>-13.218399999999999 15.328600000000002 0.4 0.0 0.0 -2.79252</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s3_12'>
#           <pose>-12.9661 14.787500000000001 0.4 0.0 0.0 -2.61799</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s3_13'>
#           <pose>-12.6237 14.2984 0.4 0.0 0.0 -2.44345</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s3_14'>
#           <pose>-12.2015 13.8763 0.4 0.0 0.0 -2.26892</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s3_15'>
#           <pose>-11.712499999999999 13.5338 0.4 0.0 0.0 -2.09438</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s3_16'>
#           <pose>-11.171399999999998 13.281500000000001 0.4 0.0 0.0 -1.91985</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s3_17'>
#           <pose>-10.5947 13.126999999999999 0.4 0.0 0.0 -1.74532</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s3_18'>
#           <pose>-10.0 13.075 0.4 0.0 0.0 -1.57079</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s3_2'>
#           <pose>-11.171399999999998 19.7184 0.4 0.0 -0.0 1.91987</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s3_3'>
#           <pose>-11.712499999999999 19.4661 0.4 0.0 -0.0 2.0944</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s3_4'>
#           <pose>-12.2016 19.1237 0.4 0.0 -0.0 2.26893</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s3_5'>
#           <pose>-12.6237 18.7015 0.4 0.0 -0.0 2.44347</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s3_6'>
#           <pose>-12.9661 18.2125 0.4 0.0 -0.0 2.618</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s3_7'>
#           <pose>-13.218499999999999 17.6714 0.4 0.0 -0.0 2.79253</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s3_8'>
#           <pose>-13.373000000000001 17.0947 0.4 0.0 -0.0 2.96707</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>
#         <link name='link_s3_9'>
#           <pose>-13.425 16.5 0.4 0.0 0.0 -3.14159</pose>
#           <velocity>0 0 0 0 -0 0</velocity>
#           <acceleration>0 0 0 0 -0 0</acceleration>
#           <wrench>0 0 0 0 -0 0</wrench>
#         </link>

# """

# left = 1

# a = text.split('</link>')
# final_text = ''

# for i in a:
#   lines = i.split('\n')
#   for index in range(len(lines)):
#       if 'pose' in lines[index]:
#           numbers = lines[index].strip().split(' ')
#           first_number = numbers[0].split('>')[1]
#           last_number = numbers[-1].split('<')[0]
#           numbers[0] = first_number
#           numbers[-1] = last_number

#           for n in range(len(numbers)):
#               numbers[n] = float(numbers[n])
#           numbers[0] += 0
#           numbers[1] += 0
#           numbers[2] += 0.5
#           # print(numbers)
#           numbers = ' '.join(map(str, numbers))
#           # print(numbers)
#           numbers = '          <pose>' + numbers + '</pose>'
#           lines[index] = numbers
#           final_text += '\n'.join(lines)
#           final_text += '</link>'

# print(final_text)

### CREATE RANDOM ROCKS
# og_text = """   <link name='rock_NUMBER'>
#       <pose>POSE_X POSE_Y 0.5 0 0 0</pose>
#       <collision name='rock_Collision'>
#         <geometry>
#           <box>
#             <size>SIZE_X SIZE_Y SIZE_Z</size>
#           </box>
#         </geometry>
#       </collision>
#       <visual name='rock_Visual'>
#         <geometry>
#           <box>
#             <size>SIZE_X SIZE_Y SIZE_Z</size>
#           </box>
#         </geometry>
#         <material>
#           <script>
#             <uri>file://media/materials/scripts/gazebo.material</uri>
#             <name>Gazebo/Black</name>
#           </script>
#           <ambient>1 1 1 1</ambient>
#         </material>
#         <meta>
#           <layer>0</layer>
#         </meta>
#       </visual>
#     </link>
# """
# final_text = """<?xml version='1.0'?>
# <sdf version='1.7'>
#   <model name='rocks'>
# """
# for i in range(150):
#     text = og_text.replace('NUMBER', str(i))
    
#     x = 0.03 + random()*0.05
#     y = 0.03 + random()*0.05
#     z = 0.03 + random()*0.03
#     text = text.replace('SIZE_X', str(x))
#     text = text.replace('SIZE_X', str(x))
#     text = text.replace('SIZE_Y', str(y))
#     text = text.replace('SIZE_Z', str(z))
#     text = text.replace('SIZE_Y', str(y))
#     text: str = text.replace('SIZE_Z', str(z))

#     pose_x = random()*8.5-4.25
#     pose_y = random()*2.92-1.46
#     text = text.replace('POSE_X', str(pose_x))
#     text = text.replace('POSE_Y', str(pose_y))

#     final_text += text
# final_text+= """  </model>
# </sdf>"""
# with open('/home/asak/building_editor_models/rocks/model.sdf', 'w') as file:
#     file.write(final_text)
# # pyperclip.copy(final_text)
# print(final_text)


### Create tumsek
final_text = """<?xml version='1.0'?>
<sdf version='1.7'>
  <model name='rocks'>
    <static>1</static>
    <pose>0 0 0.5 0 0 0</pose>
"""
og_text = """    <link name='tumsek_main_NUMBER'>
      <pose>POSE_X POSE_Y 0 0 0 0</pose>
      <collision name='tumsek_Collision'>
        <geometry>
          <box>
            <size>0.1 0.4 0.05</size>
          </box>
        </geometry>
        <pose>0 0 0.025 0 -0 0</pose>
      </collision>
      <visual name='tumsek_Visual'>
        <pose>0 0 0.025 0 -0 0</pose>
        <geometry>
          <box>
            <size>0.1 0.4 0.05</size>
          </box>
        </geometry>
        <material>
          <script>
            <uri>file://media/materials/scripts/gazebo.material</uri>
            <name>Gazebo/Bricks</name>
          </script>
          <ambient>1 1 1 1</ambient>
        </material>
        <meta>
          <layer>0</layer>
        </meta>
      </visual>
    </link>
    <link name='tumsek_front_NUMBER'>
      <pose>POSE_fX POSE_fY 0 0 0.785 0</pose>
      <collision name='tumsek_Collision'>
        <geometry>
          <box>
            <size>0.0707 0.4 0.0707</size>
          </box>
        </geometry>
        <pose>0 0 0 0 -0 0</pose>
      </collision>
      <visual name='tumsek_Visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <box>
            <size>0.0707 0.4 0.0707</size>
          </box>
        </geometry>
        <material>
          <script>
            <uri>file://media/materials/scripts/gazebo.material</uri>
            <name>Gazebo/Bricks</name>
          </script>
          <ambient>1 1 1 1</ambient>
        </material>
      </visual>
    </link>
    <link name='tumsek_back_NUMBER'>
      <pose>POSE_bX POSE_bY 0 0 0.785 0</pose>
      <collision name='tumsek_Collision'>
        <geometry>
          <box>
            <size>0.0707 0.4 0.0707</size>
          </box>
        </geometry>
        <pose>0 0 0 0 -0 0</pose>
      </collision>
      <visual name='tumsek_Visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <box>
            <size>0.0707 0.4 0.0707</size>
          </box>
        </geometry>
        <material>
          <script>
            <uri>file://media/materials/scripts/gazebo.material</uri>
            <name>Gazebo/Bricks</name>
          </script>
          <ambient>1 1 1 1</ambient>
        </material>
      </visual>
    </link>
"""

for i in range(60):
    text = og_text.replace('NUMBER', str(i))
    text = text.replace('NUMBER', str(i))
    text = text.replace('NUMBER', str(i))

    pose_x = random()*9.8-4.9
    pose_y = random()*2.6-1.3
    text = text.replace('POSE_X', str(pose_x))
    text = text.replace('POSE_Y', str(pose_y))
    text = text.replace('POSE_fX', str(pose_x + 0.05))
    text = text.replace('POSE_fY', str(pose_y))
    text = text.replace('POSE_bX', str(pose_x - 0.05))
    text = text.replace('POSE_bY', str(pose_y))
    final_text += text


final_text+= """  </model>
</sdf>"""
with open('/home/asak/building_editor_models/tumsek/model.sdf', 'w') as file:
    file.write(final_text)