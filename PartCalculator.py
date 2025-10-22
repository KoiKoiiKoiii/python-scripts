# Handiwork Circut Board Count = 250
# Electricity Generation Circuit Board Count = 250


# Enter the number of circuit boards to be produced
circuitBoardsNeeded = 500
currentPolymerCount = 725
currentPureQuartzCount = 769
# Materials required per circuit board
polymerPerBoard = 2
pureQuartzPerBoard = 4
pureQuartzPerRun = 240

# Calculate total materials needed
totalPolymer = circuitBoardsNeeded * polymerPerBoard - currentPolymerCount 
totalPureQuartz = circuitBoardsNeeded * pureQuartzPerBoard - currentPureQuartzCount 


runsNeeded = totalPureQuartz / pureQuartzPerRun  # Ceiling division to get full runs   

# Pal Oil cost per unit of Polymer
polymerPalOilCostPer = 2 

# Calculate total Pal Oil cost for Polymer needed 
totalPalOilCost = polymerPalOilCostPer * totalPolymer


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