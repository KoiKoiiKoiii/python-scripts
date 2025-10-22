circuitBoards = 190
polymerPerBoard = 2
pureQuartzPerBoard = 4

totalPolymer = circuitBoards * polymerPerBoard
totalPureQuartz = circuitBoards * pureQuartzPerBoard    

polymerPalOilCostPer = 2

totalPalOilCost = polymerPalOilCostPer * totalPolymer


# Output the results
print("Total Polymer needed: " + str(totalPolymer))
print("Total Pure Quartz needed: " + str(totalPureQuartz))
print('Total Pal Oil Cost: ' + str(totalPalOilCost))

