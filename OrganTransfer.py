

from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, person_id, name, organ):

        self._person_id = person_id

        self._name = name

        self._organ = organ

    @abstractmethod

    def display_info(self):
        pass   

    def get_id(self):
        return self._person_id


    def get_name(self):
        return self._name


    def get_organ(self):
        return self._organ



class Donor (Person):
    def __init__(self, person_id, name, organ, urgency_level):
        super().__init__(person_id, name, organ)
        self._urgency_level = urgency_level
        self.left = None
        self.right = None
    
    def get_urgency(self):
        return self._urgency_level

    def display_info(self):
        return f"[DONOR] ID: {self._person_id}, Name: {self._name}, Organ: {self._organ}, Urgency: {self._urgency_level}"

class Recipient(Person):
    def __init__(self, person_id, name, organ, blood_type):
        super().__init__(person_id, name, organ)
        self._blood_type = blood_type


    def display_info(self):
        return f"[RECIPIENT] ID: {self._person_id}, Name: {self._name}, Organ Needed: {self._organ}, Blood Type: {self._blood_type}"


class OrganTransfer:
    def __init__(self):
        self.root = None

    def insert_donor(self, donor):
        if self.root is None:
            self.root = donor
        else:
            self._insert(self.root, donor)

    def _insert(self, current, donor):
        if donor.get_urgency() < current.get_urgency():
            if current.left is None:
                current.left = donor
            else:
                self._insert(current.left, donor)
        else:
            if current.right is None:
                current.right = donor
            else:
                self._insert(current.right, donor)

    def search_by_urgency(self, urgency_level):

        return self._search(self.root, urgency_level)

    def _search(self, current, urgency_level):
        if current is None:
            return None

        if urgency_level == current.get_urgency():
            return current

        elif urgency_level < current.get_urgency():
            return self._search(current.left, urgency_level)
        else:
            return self._search(current.right, urgency_level)  
    
    def display_all_donors(self):
        print("=== All Donors (sorted by urgency) ===")
        self._inorder_traversal (self.root)

    def _inorder_traversal(self, current):
        if current:
            self._inorder_traversal (current.left)
            print(current.display_info())
            self._inorder_traversal (current.right)


if __name__ == "__main__":
    bst = OrganTransfer()
    d1 = Donor (101, "Jefferson", "Kidney", 2)
    
    d2 = Donor (102, "Stipanie", "Liver", 5)

    d3 = Donor (103, "Jolo", "Heart", 1)

    d4 = Donor (104, "Sescar", "Lung", 3)

    bst.insert_donor(d1)
    bst.insert_donor(d2)
    bst.insert_donor(d3)
    bst.insert_donor(d4)

    bst.display_all_donors()

    print("\n Searching for donor with urgency level 2:")

    found = bst.search_by_urgency(2)
    if found:
        print("Donor Found:", found.display_info())
    else:
        print("Donor not found.")

    print("\n=== Recipient Info ===")
    r1 = Recipient(201, "Tom Young", "Kidney", "0+")
    print(r1.display_info())
