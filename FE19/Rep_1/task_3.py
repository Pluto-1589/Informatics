class Item:

    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class Backpack():

    def __init__(self, max_volume):
        self.max_volume = max_volume
        self.curr_vol = 0
        self.packed = []

    def current_volume(self):
        return self.curr_vol

    def unpack(self):
        if not self.packed:
            return None
        else:
            last_item = self.packed.pop()
            self.curr_vol -= last_item.volume

            return last_item

    def pack(self, item: Item):

        if item.volume > self.max_volume:
            raise AssertionError("Item is too big, doesn't fit!")

        if (item.volume + self.curr_vol) > self.max_volume:
            raise AssertionError(
                "Can't add this item, doesn't fit into the backpack")

        else:
            self.curr_vol += item.volume
            self.packed.append(item)


bp = Backpack(4.0)
print(bp)
bp.pack(Item("water bottle", 0.75))
bp.pack(Item("lighter", 0.05))
print(bp.current_volume())  # 0.755
print(bp.unpack())  # returns Item("lighter", 0.05)
bp.pack(Item("camping tent", 20.0))  # AssertionError!
