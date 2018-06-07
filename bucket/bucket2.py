from operator import attrgetter

from location import Location

class Bucket(object):
    def __init__(self, location_count):
        self._location_count = location_count

    def pack(self, items, fill_limit):
        locations = []
        other = Location(-1)

        for x in range(0, self._location_count):
            locations.append(Location(x))

        items = sorted(items, key=attrgetter('weight'), reverse=True)
        items = sorted(items, key=attrgetter('value'), reverse=True)
        
        for item in items:
            stored = False

            locations = sorted(locations, key=attrgetter('weight'))

            for idx, location in enumerate(locations):
                if location.weight < fill_limit and item.weight <= (fill_limit - location.weight):
                    location.add_item(item)
                    stored = True

                    break

            if not stored:
                other.add_item(item)
        
        return (locations, other)

