import math
# This algorithm runs in O(n^2) time and O(n) space, where n is the number of ghost rooms that the beam can reach.
# Which depends on the distance and the dimensions of the room.

def findGhostCoordinate(ordinate, ghostRoomNum, dimensions):
    # Return the ghostRoomNum'th reflection of the passed ordinate (could be x or y)

    # The pattern of ordinates in the ghost rooms is that first the ordinate will be at 2*ordinate,
    # then 2*(dimensions-ordinate), then last+(2*ordinate), then last+(2*(dimensions-ordinate)), etc.:
    alternatingValues = [2 * ordinate, 2 * (dimensions - ordinate)]
    direction = 1 if ghostRoomNum >= 0 else -1
    offset = 1 if direction == 1 else 0
    for i in (range(abs(ghostRoomNum))):
        ordinate += alternatingValues[(i + offset) % 2] * direction
    # Return reflection for nth ghost room
    return ordinate


def ghostRoomCoordinateSeriesFinder(ordinate, dimensions, distance):
    # Return a list of lists of translation of given ordinate into ghost rooms (all the way until laser range is exceeded)

    ghostCoordinates = []
    # Run a loop for both x and y ordinates
    for i in range(len(ordinate)):
        # List of ordinates for all possible ghost rooms for given distance
        ordinates = []
        maxNegativeGhostRoomNum = -1 * (distance // dimensions[i]) - 1
        maxPositiveGhostRoomNum = (distance // dimensions[i]) + 1
        # +1 in loop to include the Max ghost room as well
        for j in range(maxNegativeGhostRoomNum, maxPositiveGhostRoomNum + 1):
            ordinates.append(findGhostCoordinate(ordinate[i], j, dimensions[i]))
        ghostCoordinates.append(ordinates)
    return ghostCoordinates


def solution(dimensions, your_position, guard_position, distance):
    # Return the number of unique angles at which you can shoot the guard
    # We find them by first finding all possible angles that you can kill yourself
    # Then we only keep angles that can kill enemy without killing yourself (so if beam can kill enemy at dist d1 for
    # some angle x but also kills you at distance d2 for same x, then only use this angle if d1<d2
    if your_position == guard_position:
        return 0
    hittingAngles = {}
    killingAngles = set()
    myGhostPositions = ghostRoomCoordinateSeriesFinder(your_position, dimensions, distance)
    enemyGhostPositions = ghostRoomCoordinateSeriesFinder(guard_position, dimensions, distance)
    for checker in (myGhostPositions, enemyGhostPositions):
        # Go through all x ordinates possible in ghost rooms until beam runs out
        for xOrdinate in checker[0]:
            # Pair xOrdinate with all possible yOrdinates to get all ghost coordinates for you/enemy
            for yOrdinate in checker[1]:
                # Find the angle b/w you and this coordinate
                hittingBeamAngle = math.atan2((your_position[1] - yOrdinate), (your_position[0] - xOrdinate))
                # Find the distance b/w you and this coordinate
                hittingBeamDist = math.sqrt((your_position[0] - xOrdinate) ** 2 + (your_position[1] - yOrdinate) ** 2)
                # If this angle is at your position itself or if this beam's dist is beyond the range of the laser,
                # ignore it
                if (xOrdinate != your_position[0] or yOrdinate != your_position[1]) and distance >= hittingBeamDist:
                    # If this angle is already in the dictionary, then check if this distance is less than the one
                    # already present. If so, replace the distance with this one. If not, do nothing.
                    if hittingBeamAngle not in hittingAngles or (hittingBeamAngle in hittingAngles and
                                                                 hittingAngles[hittingBeamAngle] > hittingBeamDist):
                        # If this angle kills you, add it/update hittingAngles dictionary
                        if checker == myGhostPositions:
                            hittingAngles[hittingBeamAngle] = hittingBeamDist
                        # If this angle kills enemy, add it to the killingAngles set and update hittingAngles
                        else:
                            hittingAngles[hittingBeamAngle] = hittingBeamDist
                            killingAngles.add(hittingBeamAngle)
    # Return the number of angles that kill enemy but not you
    return len(killingAngles)


if __name__ == '__main__':
    print(solution([3, 4],[1, 1],[2, 1],4))
    print(solution([300,275], [150,150], [185,100], 500))
