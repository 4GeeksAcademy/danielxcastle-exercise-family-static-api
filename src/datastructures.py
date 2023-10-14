
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint



family_initial_data = [{
    "name": "John",
    "age": 33, 
    "lucky_numbers": [7,13,22],
}, {    
    "name": "Jane",
    "age": 35, 
    "lucky_numbers": [10,14,3],
}, {
    "name": "Jimmy",
    "age": 5, 
    "lucky_numbers": [1],
}]

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []
        for member_data in family_initial_data:
            self.add_member(member_data)


    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member.update(
            id=self._generateId()
        )
        self._members.append(member)
        return self._members

          

    def delete_member(self, id):
        self._members = list(filter(
            lambda member: id != member["id"],
            self._members
        ))
   
    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
            
    


    def get_all_members(self):
        return self._members
