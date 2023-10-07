from collections import deque

class Hospital:
    def __init__(self):
        self.specialization = {}
        for i in range (1,21):
            self.specialization[i] = None
        self.running = True
        self.run()

    def run(self):
        while self.running:
            print ("\nWelcome to the hospital system :). Please select an option from the options below!\n\nProgram Options:\n", "1) Add new patient.\n", "2) Print all patients.\n", "3) Get next patient.\n", "4) Remove a leaving patient.\n", "5) End the program.\n")
            self.operation = int(input("Enter your choice (from 1 to 5): "))
            if self.operation == 1:
                self.add_patient()
                print("\n--------------------------------------------------------")
            elif self.operation == 2:
                self.print_all_patients()
                print("\n--------------------------------------------------------")
            elif self.operation == 3:
                self.get_next_patient()
                print("\n--------------------------------------------------------")
            elif self.operation == 4:
                self.remove_patient()
                print("\n--------------------------------------------------------")
            elif self.operation == 5:
                self.running = False
                print("\n--------------------------------------------------------")
            else:
                print("Invalid input!")
                print("\n--------------------------------------------------------")
    
    def add_patient(self):
        self.p_specialization = int(input("\nEnter specialization (from 1 to 20): "))
        if self.p_specialization > 0 and self.p_specialization < 21:
            if self.specialization[self.p_specialization] == None:
                self.specialization[self.p_specialization] = deque()
            if len(self.specialization[self.p_specialization]) == 10: 
                print("Sorry, we can't add more patients at this moment!")
                return
            patient = {}
            name = input("Enter patient name: ")
            status = int(input("Enter patient status: "))
            while status not in [0, 1, 2]:
                print("Invalid status! Please enter 0, 1, or 2.")
                status = int(input("Enter patient status (0, 1, or 2): "))
            if status == 0:
                status_string = "Normal"
            elif status == 1:
                status_string = "Urgent"
            else:
                status_string = "Super Urgent"
            patient['name'] = name
            patient['status'] = status
            patient['s_status'] = status_string
            if status == 0:
                self.specialization[self.p_specialization].append(patient)
            elif status == 1:
                try:
                    idx = self.specialization[self.p_specialization].index(next(filter(lambda x: x['status'] == 0, self.specialization[self.p_specialization])))
                    self.specialization[self.p_specialization].insert(idx, patient)
                except StopIteration:
                    self.specialization[self.p_specialization].append(patient)
            else:  
                try:
                    idx = self.specialization[self.p_specialization].index(next(filter(lambda x: x['status'] == 1, self.specialization[self.p_specialization])))
                    self.specialization[self.p_specialization].insert(idx, patient)
                except StopIteration:
                    if filter(lambda x: x['status'] == 2, self.specialization[self.p_specialization]):
                        idx = self.specialization[self.p_specialization].index(next(filter(lambda x: x['status'] == 0, self.specialization[self.p_specialization])))
                        self.specialization[self.p_specialization].insert(idx, patient)
                    else:
                        self.specialization[self.p_specialization].append(patient)
            print("Patient added successfully!")
        else:
            print("Specialization out of range!")

    def print_all_patients(self):
        self.p_specilaization = int(input("\nEnter specialization (from 1 to 20): "))
        self.patient = self.specialization[self.p_specilaization]
        if self.patient != None:
            for i in self.patient:
                print("Patient", i['name'], "is", i['s_status'])
        else: 
            print("An empty specilization.")
        
    def get_next_patient(self):
        self.p_specilaization = int(input("\nEnter specialization (from 1 to 20): "))
        patient = self.specialization[self.p_specilaization]
        if patient == None or len(patient) == 0:
            print("No patients at this moment. Have a rist, doctor.")
        else:
            print("Patient", patient[0]['name'], "Please go with the doctor!")
            patient.popleft()
            
    def remove_patient(self):
        self.p_specilaization = int(input("\nEnter specialization (from 1 to 20): "))
        patient = self.specialization[self.p_specilaization]
        found = False
        if patient != None:
            name = input("Please enter the patient name: ")
            for i in patient:
                if i['name'] == str(name):
                    patient.remove(i)
                    found = True
                    break
            if not found:
                print("No patient with such a name in this specialization!")
        else:
            print("An empty specilization.")

    def test(self):
        self.specialization[1] = [] #making specialization 1 full by default
        for i in range (10):
            self.specialization[1].append(i)
        self.specialization[2] = deque()
        self.specialization[2].append({'name': 'yy', 'status': 2, 's_status': 'Super Urgent'})    
        self.specialization[2].append({'name': 'xx', 'status': 0, 's_status': 'Normal'}) # these are a test elements in specialization 2

a = Hospital() 