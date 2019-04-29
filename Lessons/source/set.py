from hashtable import HashTable



class Set(HashTable):

    def __init__(self, elements=None):
        """Initialize this Set with the given elements"""

      self.data = HashTable()  #Store data in hashtable

        if elements != None:
            for element in elements:
                self.add(element)


    def add(self, element):
        """Add element to this set, if not present already"""
        # HashTable requires key,value. Sets are essentially just keys,
        # so setting the value to element ensures no confusion in terms of whats in the set
        self.data.set(element,element)

    def remove(self, element):
        """Remove element from this set, if present, or else raise KeyError"""

        self.data.delete(element)


    def union(self, other_set):
        """Return a new set that is the union of this set and other_set"""

        union = self

        # Go through other_set and add the keys that are not in the current set
        for key in other_set:
            if self.data.contains(key):
                continue

            # Key not found in current set
            else:
                new_set.add(key)

        return union


    def intersection(self, other_set):
        """Return a new set that is the intersection of this set and other_set"""

        # Empty set without any values from current or other set because we only want SIMILAR keys
        intersection = self.__init__()

        for key in other_set.data:

            # Keys matched in current set and other_set
            if self.data.contains(key):
                intersection.add(key)

            # There was no matching key
            else:
                continue

        return intersection


    def difference(self, other_set):
         """Return a new set that is the difference of this set and other_set"""

         difference = self

         for key in other_set:

            if other_set.data.contains(key):
                continue

            else
