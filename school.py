class School:
    
    def __init__(self, name=None):
        self.name = name
        self.roster = {}
        
    def get_roster(self):
        return self.roster
    
    def add_student(self, name, grade):
        
        if grade not in self.roster:
            self.roster[grade] = []
            self.roster[grade].append(name)
        else:
            self.roster[grade].append(name)
            
    def grade(self, grade):
        return self.roster[grade]
    
    def sort_roster(self):
        new_sorted_dict = {}
        for key in self.roster.keys():
            new_sorted_dict[key] = sorted(self.roster[key])
        return new_sorted_dict
    
     
      
                                       
                                     
        