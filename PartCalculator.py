# Handiwork Circut Board Count = 250
# Electricity Generation Circuit Board Count = 250


# Enter the number of circuit boards to be produced
circuitBoardsNeeded = 0

# Current inventory of materials
currentPolymerCount = 500
currentPureQuartzCount = 9

# Materials required per circuit board
polymerPerBoard = 2
pureQuartzPerBoard = 4
pureQuartzPerRun = 240
polymerPalOilCostPer = 2 

# Calculate total materials needed
totalPolymer = circuitBoardsNeeded * polymerPerBoard - currentPolymerCount if circuitBoardsNeeded * polymerPerBoard > currentPolymerCount else 0
totalPureQuartz = circuitBoardsNeeded * pureQuartzPerBoard - currentPureQuartzCount if circuitBoardsNeeded * pureQuartzPerBoard > currentPureQuartzCount else 0
totalPalOilCost = polymerPalOilCostPer * totalPolymer if totalPolymer > 0 else 0

runsNeeded = totalPureQuartz / pureQuartzPerRun

# Pal Oil cost per unit of Polymer
 
# Output the results
if circuitBoardsNeeded > 0:
    print('---')
    print("Total Polymer needed: " + str(totalPolymer))
    print('Total Pal Oil cost for remaining Polymer: ' + str(totalPalOilCost))
    print('---')
    print("Total Pure Quartz needed: " + str(totalPureQuartz))
    print("Runs needed for Pure Quartz: " + str(runsNeeded))
    print('---')

# To run this script, make sure you have Python installed on your system.
# Save this code in a file named PartCalculator.py and run it using the command: python



# Legendary Sphere Cost Calculator

legendarySphereLF = 999
legendarySphereCost = {
    "Paldium": 10,
    "Pal Metal": 5,
    "Carbon Fiber": 3,
    "Cement": 5
}

carbonFiberCost = {
    "Coal": 2
}

cementCost = {
    "Stone": 50,
    "Bone": 1,
    "Pal Fluid": 1
}


totalCost = {}


print('--- Legendary Sphere Total Material Requirements ---')
print(f'Calculating for {legendarySphereLF} Legendary Spheres:')
for material, quantity in legendarySphereCost.items():
    totalCost[material] = quantity * legendarySphereLF
    print(f'Total {material} needed: {totalCost[material]}')

for material, quantity in carbonFiberCost.items():
    totalCost[material] = quantity * legendarySphereLF * legendarySphereCost["Carbon Fiber"]
    print(f'Total {material} needed for Carbon Fiber: {totalCost[material]}')

print ('---')
for material, quantity in cementCost.items():
    totalCost[material] = quantity * legendarySphereLF * legendarySphereCost["Cement"]
    print(f'Total {material} needed for Cement: {totalCost[material]}')