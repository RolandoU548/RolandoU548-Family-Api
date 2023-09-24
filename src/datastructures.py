
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = []

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        self._members.append(member)
        return "Member added succesfully"

    def delete_member(self, id):
        id = int(id)
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return "Member deleted succesfully"
        return "Couldn't delete any member since id doesn't exist"

    def get_member(self, id):
        id = int(id)
        for member in self._members:
            if member["id"] == id:
                return member
        return "Couldn't get any member since id doesn't exist"

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
