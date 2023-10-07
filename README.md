# Hospital System

A hospital management system that allows the user to manage patients' details all over the whole hospital specializations. The patients are added on a priority basis, where a "super urgent" patient is on the top of the queue, while the "normal" patient goes the last.

## Description

An application of object-oriented programming & deque data structure using `Python` in a hospital system. 
The system allows the user to manage the visiting patients in _(20)_ specializations (queues). Besides, the system sorts the patients' queue according to the priority the user provides: `normal (0)`, `urgent (1)`, and `super urgent (2)` with no more than 10 patients in each specialization (queue). 

#### This system allows the user to:
1. Add a new patient.
   > The user can _**add**_ patients by providing the following data: specialization number, patient name, and patient priority status.

   > Once added, the patient is placed in the queue according to the priority with the super urgent status at the top of the queue, the normal at the end, and the urgent in between. If two patients are with the same priority, they are placed following the rule of **_"first come first served."_**
   
   > For example if there are `2 super urgent`, `1 urgent`, and `1 normal` -> if 1 super urgent comes, he is placed as the third super urgent but before the 1st urgent patient.
   
1. Print all patients.
   > The user can **_view_** all the patients in each specialization with all their details. If no patient at the right moment, it displays _"No patients at the moment! Have a rest, Dr."_
2. Get next patient.
   > The doctor can **_view_** the next patient (top of queue) on the **_priority status_**. Once the patient is displayed, he is removed from the queue.
3. Remove a leaving patient.
   > By providing the patient _**specialization**_ and name, the doctor can _**remove**_ from the application. The system will automatically re-sort the queue after deletion.
4. End the program.
   > If the user chooses 5, the program _**terminates**_.

## Executing program
Run the program, choose your desired process, and have fun ^^.






