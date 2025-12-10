<img width="1308" height="1036" alt="c3f085a43f03af63861f1e465125cfa8" src="https://github.com/user-attachments/assets/7f568a87-815a-47cd-9848-1ef689088e55" /># Hospital
5003 Project
This is a simulated Hospital Management System, primarily designed to familiarize with backend development and to learn about the use and optimization of MySQL databases.
The system consists of 13 tables in total, which are: department、doctor、patient、pharmaceutical_factory、medicine、registration_window、registration、diagnosis、treatment、prescription、stock_warning、garage、parking。
<img width="1308" height="1036" alt="20251210223434_1147_452" src="https://github.com/user-attachments/assets/d4dc3df0-467c-4464-b27f-4638611aff78" />

To ensure data integrity, the insertion and updating of some tables are constrained by foreign keys. For example, the medicine table is constrained by pharmaceutical_factory in the pharmaceutical_factory table; the parking table is constrained by garage_id in the garage table and patient_id in the patient table, and so on.  

To improve query performance, we have also added several indexes.
For instance, an index on is_otc in the medicine table is used to check whether a medicine is over-the-counter, 
and indexes on registration_id in the diagnosis table and patient_id in the registration table are used to retrieve all medical diagnosises of a patient.
