import unittest


class test_parkingLot(unittest.TestCase):

    def test_park_vehicle(self):
        parking_lot = parkingLot(3)
        slot1 = parking_lot.park_vehicle("car1")
        slot2 = parking_lot.park_vehicle("car2")
        slot3 = parking_lot.park_vehicle("car3")
        slot4 = parking_lot.park_vehicle("car4")
        self.assertEqual(slot1, "Vehicle is parked")
        self.assertEqual(slot2, "Vehicle is parked")
        self.assertEqual(slot3, "Vehicle is parked")
        self.assertEqual(slot4, "No slots available")

    def test_remove_vehicle(self):
        parking_lot = parkingLot(3)
        parking_lot.park_vehicle("car1")
        parking_lot.park_vehicle("car2")
        self.assertEqual(parking_lot.remove_vehicle(
            "car1"), "Vehicle is removed")
        self.assertEqual(parking_lot.remove_vehicle(
            "car1"), "Vehicle not found")
        self.assertEqual(parking_lot.remove_vehicle(
            "car2"), "Vehicle is removed")

    def test_get_empty_slots(self):
        parking_lot = parkingLot(3)
        parking_lot.park_vehicle("car1")
        parking_lot.park_vehicle("car2")
        self.assertEqual(parking_lot.empty_slots(), 1)


class parkingLot:

    def __init__(self, size):
        self.size = size
        self.slots = [None]*size

    def park_vehicle(self, vehicle):
        if None in self.slots:
            slot = self.slots.index(None)
            self.slots[slot] = vehicle
            return "Vehicle is parked"
        else:
            return "No slots available"

    def remove_vehicle(self, vehicle):
        if vehicle in self.slots:
            slot = self.slots.index(vehicle)
            self.slots[slot] = None
            return "Vehicle is removed"
        else:
            return "Vehicle not found"

    def empty_slots(self):
        return self.slots.count(None)


if __name__ == "__main__":
    unittest.main()
