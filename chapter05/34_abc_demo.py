from abc import ABC, abstractmethod

class AbstractStudentDAO(ABC):
    """Defines the student DAO API"""
    @abstractmethod
    def insert(self, student):
        raise NotImplementedError() #or pass
    
    @abstractmethod
    def update(self, student_id, student):
        raise NotImplementedError()
    
    @abstractmethod
    def delete(self, student_id):
        raise NotImplementedError
    
    @abstractmethod
    def get_one(self, student_id):
        raise NotImplementedError()
    
class StudentImpl(AbstractStudentDAO):
    def __init__(self):
        self.students = {}

    def insert(self, student):
        student_id = student["id"]
        self.students[student_id] = student
        print(f"inserted student with ID: {student_id}")
    
    def update(self, student_id, student):
        if student_id in self.students:
            self.students[student_id] = student
            print(f"updated student with id: {student_id}")
        else:
            print(f"studentwith id: {student_id}, not found")

    def delete(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print(f"student with id: {student_id}, deleted")
        else:
            print(f"student with id: {student_id}, not found")

    def get_one(self, student_id):
        return self.students.get(student_id, None)
    
class ABCInventory(ABC):
    @abstractmethod
    def add_item(self, item):
        pass
    @abstractmethod
    def remove_itme(self, item_name_to_remove):
        pass

class Inventory(ABCInventory):
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added item: {item}")
    
    def remove_item(self, item_name_to_remove):
        for item in self.items:
            if item.name == item_name_to_remove:
                self.items.remove(item)
                print(f"Remove item: {item_name_to_remove}")
                return
        print(f"item not found: {item_name_to_remove}")

class Item:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

def main():
    student_d = StudentImpl()
    student_d.insert({'id': 1, 'name':"Bob"})
    student_d.insert({'id': 2, 'name':"Alice"})

    student_d.update(1, {'id':1, 'name':"John"})
    st = student_d.get_one(1)
    student_d.delete(2)
    

if __name__ == "__main__":
    main()