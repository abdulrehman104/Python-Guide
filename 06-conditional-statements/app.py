# ====================================== Syntax ======================================

# if condition1:   ---> Code to execute if condition1 is true

# elif condition2: ---> # Code to execute if condition2 is true

# else:


# ================= if Statement =================

# Code to execute if the condition is true
traffic_light = "green"

if traffic_light == "green":
  print("You can go")



# ================= Else Statement =================

# Code to execute if the condition is false
traffic_light = "red"

if traffic_light == "green":

  print("You can go")
else:
  print("You must stop")



# ================= Elif Statement =================

# Code to execute if all conditions are false
traffic_light = "yellow"

if traffic_light == "green":
  print("You can go")
elif traffic_light == "yellow":
  print("Slow down and prepare to stop")
else:
  print("You must stop")



# ================= Nested if Statement =================
car_speed = 60
seat_belt = True

if car_speed <= 60:
  if seat_belt:
    print("You are driving safely")
  else:
    print("Please wear your seat belt")
else:
  print("Slow down, you are exceeding the speed limit")



# =================================== Logical Operators in Conditional Statements ===================================

# ================= AND if Statement =================
pedestrian_signal = "walk"
is_flashing = False

if pedestrian_signal == "walk" and not is_flashing:

  print("Pedestrian can cross safely")
else:
  print("Pedestrian should wait")



# ================= OR if Statement =================
traffic_light = "red"
vehicle_type = "ambulance"

if traffic_light == "green" or vehicle_type == "ambulance":

  print("You can go")
else:
  print("You must stop")



# ================= NOT if Statement =================
pedestrian_signal = "dont walk"

if not pedestrian_signal == "walk":

  print("Do not cross")
else:
  print("You can cross")



# =================================== Case Sensitivity in Conditions ===================================
traffic_light = "Red"

if traffic_light == "red":

  print("You must stop")
else:
  print("Slow down and prepare to stop")