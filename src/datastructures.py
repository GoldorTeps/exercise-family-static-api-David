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
        # example list of members
        self._members = [
        ]
    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)
    def add_member(self, member):
        # fill this method and update the return
        to_add = {
                "id" : member["id"],
                "first_name": member["first_name"],
                "last_name" : self.last_name,
                "age" : member["age"],
                "lucky_numbers" : member["lucky_numbers"]
        }
        self._members.append(to_add)
        return "added"
    def delete_member(self, id):
        # fill this method and update the return
        self._members = list(filter( lambda x: x["id"]!=id  ,self._members))
        return "deleted"
    def update_member (self,id,member):
        for i in range (len(self._members)):
            if( self._members[i]["id"] == id):
                index = i
                self._members[index] = member
                return "found"
        return "not found"
    def get_member(self, id):
        # fill this method and update the return
        for i in self._members:
            if (i["id"] == id):
                return i
        return False
    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

