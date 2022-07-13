#SAL'S SHIPPING

# STEP ONE: CREATE A VARIABLE 'WEIGHT' AND SET IT TO AN EQUAL NUMBER
weight = 41.5

#STEP TWO: WE NEED TO KNOW HOW MUCH SHIPPING A PACKAGE OG GIVEN WEIGHT WITH NORMAL GROUND SHIPPING
# CREATE AN IF/ELIF/ ELSE FOR THE COST OF GROUND SHIPPING
# IT SHOULD CHECK 'WEIGHT' AND 'COST'
drone_shipping = 1
# GROUND SHIPPING

if weight <= 2:
  cost = 1.5 * weight + 20
elif weight <= 6:
  cost = 3 * weight + 20
elif weight <= 10:
  cost = 4 * weight + 20
else:
  cost = 4.75 * weight + 20

print(' Shipping for ground', cost)


#GROUND SHIPPING PREMIUM
cost_ground_premium = 125.00

print(cost_ground_premium)
#DRONE SHIPPING:
# Create an if/elif/else statement for the cost of drone shipping. 
# This statement should check against weight and print the cost 
# of shipping a package of that weight.

if weight <= 2:
  drone_shipping = 4.5 * weight
elif weight <= 6:
  drone_shipping = 9 * weight
elif weight <= 10:
  drone_shipping = 12 * weight
else:
  drone_shipping = 14.75 * weight

print('shipping for drone shipping $', drone_shipping)
