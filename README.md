# Hospital
5003 Project
This is a simulated Hospital Management System, primarily designed to familiarize with backend development and to learn about the use and optimization of MySQL databases.
The system consists of 13 tables in total, which are: department、doctor、patient、pharmaceutical_factory、medicine、registration_window、registration、diagnosis、treatment、prescription、stock_warning、garage、parking。
<img width="1308" height="1036" alt="20251210223434_1147_452" src="https://github.com/user-attachments/assets/d4dc3df0-467c-4464-b27f-4638611aff78" />

Our hospital management system is divided into four sections, each corresponding to a main table: physician information, patient information, medication information, and parking lot information.This design is because we find that it is always lack of information about parking lot for people in hospital.Parking lot information is always isolated by the whole internal hospital system,which causes a lot of problems and inconvenience for both patients and administrative staff.So we proposed to add this part into hospital system to make it more complete.These sections are interconnected through a framework to enhance the overall utilization efficiency of hospital resources through precise queries, thereby providing convenient services for both patients and management staff.The hospital management application, enhanced with car park information, enables more efficient resource utilisation. When patients travel to the hospital, they can check the latest system updates to determine if parking spaces are available and accurately locate their parking spot within the car park. The dispensing area issues alerts during medication shortages.

To ensure data integrity, the insertion and updating of some tables are constrained by foreign keys. For example, the medicine table is constrained by pharmaceutical_factory in the pharmaceutical_factory table; the parking table is constrained by garage_id in the garage table and patient_id in the patient table, and so on.  

To improve query performance, we have also added several indexes.
For instance, an index on is_otc in the medicine table is used to check whether a medicine is over-the-counter, 
and indexes on registration_id in the diagnosis table and patient_id in the registration table are used to retrieve all medical diagnosises of a patient.
