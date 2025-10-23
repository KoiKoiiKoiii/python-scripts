# Handiwork Circut Board Count = 250
# Electricity Generation Circuit Board Count = 250


# Enter the number of circuit boards to be produced
circuitBoardsNeeded = 250
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
# Calculate total Pal Oil cost for Polymer needed 

# 30 35 35 Handiwork High Quality Cloth
# 30 + 35 + 35 = 100

# Kindling 150 Plasteel

# Output the results
print('---')
print("Total Polymer needed: " + str(totalPolymer))
print('Total Pal Oil cost for remaining Polymer: ' + str(totalPalOilCost))
print('---')
print("Total Pure Quartz needed: " + str(totalPureQuartz))
print("Runs needed for Pure Quartz: " + str(runsNeeded))
print('---')

# To run this script, make sure you have Python installed on your system.
# Save this code in a file named PartCalculator.py and run it using the command: python