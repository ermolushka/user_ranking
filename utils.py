import math
import json

"""
Accept float arguments x1, y1, x2, and y2: the latitude
and longitude, in degrees, of two points on the earth. Also accept name of the person. Compute the great circle
distance (in nautical miles) between those two points.
"""


def compute_distance(x2, y2, x1=53.339428, y1=-6.257664, name=None):

    try:
        x1 = float(x1)
        y1 = float(y1)
        x2 = float(x2)
        y2 = float(y2)
        """
        The following formulas assume that angles are expressed in radians.
        So convert to radians.
        """
        x1 = math.radians(x1)
        y1 = math.radians(y1)
        x2 = math.radians(x2)
        y2 = math.radians(y2)

        """
        Compute using the law of cosines.

        Great circle distance in radians
        """
        angle1 = math.acos(math.sin(x1) * math.sin(x2) \
                 + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

        # Convert back to degrees.
        angle1 = math.degrees(angle1)

        # Each degree on a great circle of Earth is 60 nautical miles.
        distance1 = 60.0 * angle1

        conversion_factor = 0.62137119

        kilometers = distance1 / conversion_factor

        return [kilometers, name]

    except:

        return [0, 0]


def read_txt(file):

    data = {}
    try:

        f = open(file, 'r')
        for line in f.readlines():
            d = json.loads(line)
            data[d["user_id"]] = [d['latitude'], d['longitude'], d['name']]

        return data

    except:

        return {0: [0, 0, "test"]}


def rank_users(file):

    ranked = {}
    try:
        coord = read_txt(file)
        for x in coord:

            distance = compute_distance(coord[x][0], coord[x][1], name=coord[x][2])

            if distance[0] <= 100.0:

                ranked[x] = distance[1]

        return str(dict(sorted(ranked.items())))

    except:

        return str({})
