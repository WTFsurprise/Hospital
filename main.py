import uvicorn
from fastapi import FastAPI, Depends, HTTPException, APIRouter, Query
from sqlalchemy.orm import Session
from typing import List, Type, Any ,Optional
from decimal import Decimal
from database import engine, get_db, Base
import schemas.department, crud.department
import schemas.doctor, crud.doctor
import schemas.patient, crud.patient
import schemas.pharmaceutical_factory, crud.pharmaceutical_factory
import schemas.medicine, crud.medicine
import schemas.registration_window, crud.registration_window
import schemas.registration, crud.registration
import schemas.diagnosis, crud.diagnosis
import schemas.treatment, crud.treatment
import schemas.prescription, crud.prescription
import schemas.stock_warning, crud.stock_warning
import schemas.garage, crud.garage
import schemas.parking, crud.parking
from datetime import date, datetime
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Hospital System API")

def create_router(
    prefix: str,
    tag: str,
    crud_obj: Any,
    schema_create: Type,
    schema_update: Type,
    schema_response: Type,
):
    router = APIRouter(prefix=prefix, tags=[tag])
    # ====== 特殊路由 ======
    @app.get("/medicines/is_otc", response_model=List[schemas.medicine.Medicine], tags=["Medicines"])
    def read_medicines_by_otc(is_otc: bool,skip: int = 0,limit: int = 100,db: Session = Depends(get_db)
    ):
        return crud.medicine.crud_medicine.get_by_otc(db, is_otc=is_otc, skip=skip, limit=limit)
    
    @app.get("/medicines/name/{medicine_name}", response_model=List[schemas.medicine.Medicine], tags=["Medicines"])
    def read_medicines_by_name(medicine_name: str, db: Session = Depends(get_db)):
        return crud.medicine.crud_medicine.get_by_name(db, medicine_name=medicine_name)

    @app.get("/medicines/name/{keyword}", response_model=List[schemas.medicine.Medicine], tags=["Medicines"])
    def search_medicines_by_keyword(keyword: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        return crud.medicine.crud_medicine.search_by_name(db, keyword=keyword, skip=skip, limit=limit)

    @app.get("/medicines/price/range", response_model=List[schemas.medicine.Medicine], tags=["Medicines"])
    def read_medicines_by_price_range(
        min_price: Optional[Decimal] = None, 
        max_price: Optional[Decimal] = None, 
        skip: int = 0, 
        limit: int = 100, 
        db: Session = Depends(get_db)
    ):
        return crud.medicine.crud_medicine.get_by_price_range(db, min_price=min_price, max_price=max_price, skip=skip, limit=limit)

    @app.get("/medicines/price/high", response_model=List[schemas.medicine.Medicine], tags=["Medicines"])
    def read_high_price_medicines(threshold: Decimal, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        return crud.medicine.crud_medicine.get_high_price_medicines(db, threshold=threshold, skip=skip, limit=limit)

    @app.get("/medicines/stock/low", response_model=List[schemas.medicine.Medicine], tags=["Medicines"])
    def read_low_stock_medicines(threshold: int = 10, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        return crud.medicine.crud_medicine.get_low_stock(db, threshold=threshold, skip=skip, limit=limit)

    @app.get("/medicines/quantity/range", response_model=List[schemas.medicine.Medicine], tags=["Medicines"])
    def read_medicines_by_quantity_range(
        min_qty: Optional[int] = None, 
        max_qty: Optional[int] = None, 
        skip: int = 0, 
        limit: int = 100, 
        db: Session = Depends(get_db)
    ):
        return crud.medicine.crud_medicine.get_by_quantity_range(db, min_qty=min_qty, max_qty=max_qty, skip=skip, limit=limit)

    @app.get("/medicines/expiring/soon", response_model=List[schemas.medicine.Medicine], tags=["Medicines"])
    def read_expiring_soon_medicines(days: int = 30, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        return crud.medicine.crud_medicine.get_expiring_soon(db, days=days, skip=skip, limit=limit)

    @app.get("/medicines/expired", response_model=List[schemas.medicine.Medicine], tags=["Medicines"])
    def read_expired_medicines(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        return crud.medicine.crud_medicine.get_expired(db, skip=skip, limit=limit)

    @app.get("/medicines/production/range", response_model=List[schemas.medicine.Medicine], tags=["Medicines"])
    def read_medicines_by_production_date_range(
        start_date: Optional[date] = None, 
        end_date: Optional[date] = None, 
        skip: int = 0, 
        limit: int = 100, 
        db: Session = Depends(get_db)
    ):
        return crud.medicine.crud_medicine.get_by_production_date_range(db, start_date=start_date, end_date=end_date, skip=skip, limit=limit)

    @app.get("/medicines/factory/{factory_id}", response_model=List[schemas.medicine.Medicine], tags=["Medicines"])
    def read_medicines_by_factory(factory_id: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        return crud.medicine.crud_medicine.get_by_factory(db, factory_id=factory_id, skip=skip, limit=limit)
    
    @app.get("/prescriptions/patient/{patient_id}", response_model=List[schemas.prescription.Prescription], tags=["Prescriptions"])
    def read_prescriptions_by_patient(patient_id: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        return crud.prescription.crud_prescription.get_by_patient(db, patient_id=patient_id, skip=skip, limit=limit)

    @app.get("/prescriptions/medicine/{medicine_id}", response_model=List[schemas.prescription.Prescription], tags=["Prescriptions"])
    def read_prescriptions_by_medicine(medicine_id: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        return crud.prescription.crud_prescription.get_by_medicine(db, medicine_id=medicine_id, skip=skip, limit=limit)

    @app.get("/prescriptions/treatment/{treatment_id}", response_model=List[schemas.prescription.Prescription], tags=["Prescriptions"])
    def read_prescriptions_by_treatment(treatment_id: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        return crud.prescription.crud_prescription.get_by_treatment(db, treatment_id=treatment_id, skip=skip, limit=limit)

    @app.get("/prescriptions/price/range", response_model=List[schemas.prescription.Prescription], tags=["Prescriptions"])
    def read_prescriptions_by_price_range(
        min_price: Optional[Decimal] = None, 
        max_price: Optional[Decimal] = None, 
        skip: int = 0, 
        limit: int = 100, 
        db: Session = Depends(get_db)
    ):
        return crud.prescription.crud_prescription.get_by_price_range(db, min_price=min_price, max_price=max_price, skip=skip, limit=limit)

    @app.get("/prescriptions/price/high", response_model=List[schemas.prescription.Prescription], tags=["Prescriptions"])
    def read_high_price_prescriptions(threshold: Decimal, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        return crud.prescription.crud_prescription.get_high_price_prescriptions(db, threshold=threshold, skip=skip, limit=limit)

    @app.get("/prescriptions/patient/{patient_id}/medicine/{medicine_id}", response_model=List[schemas.prescription.Prescription], tags=["Prescriptions"])
    def read_prescriptions_by_patient_and_medicine(patient_id: str, medicine_id: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        return crud.prescription.crud_prescription.get_by_patient_and_medicine(db, patient_id=patient_id, medicine_id=medicine_id, skip=skip, limit=limit)

    @app.get("/prescriptions/patient/{patient_id}/time", response_model=List[schemas.prescription.Prescription], tags=["Prescriptions"])
    def read_patient_prescriptions_by_time(
        patient_id: str, 
        start_date: Optional[date] = None, 
        end_date: Optional[date] = None, 
        skip: int = 0, 
        limit: int = 100, 
        db: Session = Depends(get_db)
    ):
        return crud.prescription.crud_prescription.get_patient_prescriptions_by_time(db, patient_id=patient_id, start_date=start_date, end_date=end_date, skip=skip, limit=limit)

    @app.get("/prescriptions/recent", response_model=List[schemas.prescription.Prescription], tags=["Prescriptions"])
    def read_recent_prescriptions(days: int = 7, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        return crud.prescription.crud_prescription.get_recent_prescriptions(db, days=days, skip=skip, limit=limit)

    @app.get("/stock_warnings/medicine/{medicine_id}", response_model=List[schemas.stock_warning.StockWarning], tags=["Stock Warnings"])
    def read_warnings_by_medicine(medicine_id: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        return crud.stock_warning.crud_stock_warning.get_by_medicine(db, medicine_id=medicine_id, skip=skip, limit=limit)

    @app.get("/stock_warnings/type/{warning_type}", response_model=List[schemas.stock_warning.StockWarning], tags=["Stock Warnings"])
    def read_warnings_by_type(warning_type: schemas.stock_warning.WarningTypeEnum, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        return crud.stock_warning.crud_stock_warning.get_by_warning_type(db, warning_type=warning_type, skip=skip, limit=limit)

    @app.get("/stock_warnings/unhandled", response_model=List[schemas.stock_warning.StockWarning], tags=["Stock Warnings"])
    def read_unhandled_warnings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        return crud.stock_warning.crud_stock_warning.get_unhandled_warnings(db, skip=skip, limit=limit)

    @app.get("/stock_warnings/handled", response_model=List[schemas.stock_warning.StockWarning], tags=["Stock Warnings"])
    def read_handled_warnings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        return crud.stock_warning.crud_stock_warning.get_handled_warnings(db, skip=skip, limit=limit)

    @app.get("/stock_warnings/filter", response_model=List[schemas.stock_warning.StockWarning], tags=["Stock Warnings"])
    def read_warnings_by_filter(is_handled: Optional[bool] = None,start_date: Optional[date] = None,
end_date: Optional[date] = None,
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db)
    ):
        return crud.stock_warning.crud_stock_warning.get_by_time_status(db, is_handled=is_handled, start_date=start_date, end_date=end_date, skip=skip, limit=limit)

    @app.get("/stock_warnings/recent", response_model=List[schemas.stock_warning.StockWarning], tags=["Stock Warnings"])
    def read_recent_warnings(days: int = 7, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        return crud.stock_warning.crud_stock_warning.get_recent_warnings(db, days=days, skip=skip, limit=limit)

    @app.get("/stock_warnings/medicine/{medicine_id}/time", response_model=List[schemas.stock_warning.StockWarning], tags=["Stock Warnings"])
    def read_warnings_by_medicine_and_time(
        medicine_id: str,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db)
    ):
        return crud.stock_warning.crud_stock_warning.get_by_medicine_and_time(db, medicine_id=medicine_id, start_date=start_date, end_date=end_date, skip=skip, limit=limit)

    @app.get("/stock_warnings/low_stock", response_model=List[schemas.stock_warning.StockWarning], tags=["Stock Warnings"])
    def read_low_stock_warnings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        return crud.stock_warning.crud_stock_warning.get_low_stock_warnings(db, skip=skip, limit=limit)

    @app.get("/stock_warnings/near_expiration", response_model=List[schemas.stock_warning.StockWarning], tags=["Stock Warnings"])
    def read_near_expiration_warnings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        return crud.stock_warning.crud_stock_warning.get_near_expiration_warnings(db, skip=skip, limit=limit)
    
    @app.patch("/stock_warnings/{warning_id}/handle", response_model=schemas.stock_warning.StockWarning, tags=["Stock Warnings"])
    def mark_warning_as_handled(warning_id: str, handled_by: str, db: Session = Depends(get_db)):
        warning = crud.stock_warning.crud_stock_warning.mark_as_handled(db, warning_id=warning_id, handled_by=handled_by)
        if not warning:
            raise HTTPException(status_code=404, detail="Stock warning not found")
        return warning

    @app.get("/diagnoses/registration/{registration_id}", response_model=Optional[schemas.diagnosis.Diagnosis],
             tags=["Diagnoses"])
    def read_diagnosis_by_registration(registration_id: str, db: Session = Depends(get_db)):
        return crud.diagnosis.crud_diagnosis.get_by_registration(db, registration_id=registration_id)

    @app.get("/diagnoses/doctor/{doctor_id}", response_model=List[schemas.diagnosis.Diagnosis], tags=["Diagnoses"])
    def read_diagnoses_by_doctor(doctor_id: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        return crud.diagnosis.crud_diagnosis.get_by_doctor(db, doctor_id=doctor_id, skip=skip, limit=limit)
    @app.get("/diagnoses/patient/{patient_id}", response_model=List[schemas.diagnosis.Diagnosis], tags=["Diagnoses"])
    def read_diagnoses_by_patient(patient_id: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        return crud.diagnosis.crud_diagnosis.get_by_patient(db, patient_id=patient_id, skip=skip, limit=limit)

    @app.get("/diagnoses/search", response_model=List[schemas.diagnosis.Diagnosis], tags=["Diagnoses"])
    def search_diagnoses(keyword: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        return crud.diagnosis.crud_diagnosis.search_by_result(db, keyword=keyword, skip=skip, limit=limit)

    @app.get("/diagnoses/range", response_model=List[schemas.diagnosis.Diagnosis], tags=["Diagnoses"])
    def read_diagnoses_by_date_range(
            start_time: Optional[datetime] = None,
            end_time: Optional[datetime] = None,
            skip: int = 0,
            limit: int = 100,
            db: Session = Depends(get_db)
    ):
        return crud.diagnosis.crud_diagnosis.get_by_date_range(
            db,
            start_time=start_time,
            end_time=end_time,
            skip=skip,
            limit=limit
        )

    @app.get("/doctors", response_model=List[schemas.doctor.Doctor], tags=["Doctors"])
    def read_doctors(
            db: Session = Depends(get_db),
            doctor_id: Optional[str] = Query(None, description="Select by doctor_id"),
            dept_id: Optional[str] = Query(None, description="Select by dept_id"),
            min_age: Optional[int] = Query(None, description="Minimum age filter"),
            max_age: Optional[int] = Query(None, description="Maximum age filter"),
            min_salary: Optional[float] = Query(None,
                                                description="Filter doctors with salary greater than or equal to this value"),
            sort_by: str = Query('created_at', description="Field to sort by"),
            sort_order: str = Query('desc', description="Sort order: 'asc' or 'desc'"),
            skip: int = 0,
            limit: int = 100
    ):
        doctors = crud.doctor.crud_doctor.get_multi_filtered(
            db,
            doctor_id=doctor_id,
            dept_id=dept_id,
            min_age=min_age,
            max_age=max_age,
            min_salary=min_salary,
            sort_by=sort_by,
            sort_order=sort_order,
            skip=skip,
            limit=limit
        )
        return doctors

    @app.get("/patients", response_model=List[schemas.patient.Patient], tags=["Patients"])
    def read_patients(
            patient_id: Optional[str] = Query(None, description="Selected by patient_id"),
            age: Optional[int] = Query(None, ge=0, description="Selected by age"),
            sort_by: str = Query('created_at', description="Field to sort by"),
            sort_order: str = Query('desc', regex="^(asc|desc)$", description="Sort order: asc or desc"),
            skip: int = 0,
            limit: int = 100,
            db: Session = Depends(get_db)
    ):
        patients = crud.patient.crud_patient.get_multi_filtered(
            db=db,
            patient_id=patient_id,
            age=age,
            sort_by=sort_by,
            sort_order=sort_order,
            skip=skip,
            limit=limit
        )
        return patients

    @app.get("/treatments", response_model=List[schemas.treatment.Treatment], tags=["Treatments"])
    def read_treatments(
            db: Session = Depends(get_db),
            diagnosis_id: Optional[str] = Query(None, description="Filter by Diagnosis ID"),
            treatment_id: Optional[str] = Query(None, description="Filter by Treatment ID"),
            doctor_id: Optional[str] = Query(None, description="Filter by Doctor ID"),
            sort_by: str = Query('created_at', description="Field to sort by"),
            sort_order: str = Query('desc', description="Sort order: 'asc' or 'desc'"),
            skip: int = 0,
            limit: int = 100
    ):
        treatments = crud.treatment.crud_treatment.get_multi_filtered(
            db,
            diagnosis_id=diagnosis_id,
            treatment_id=treatment_id,
            doctor_id=doctor_id,
            sort_by=sort_by,
            sort_order=sort_order,
            skip=skip,
            limit=limit
        )
        return treatments

    @app.get("/registration-windows", response_model=List[schemas.registration_window.RegistrationWindow],
             tags=["Registration Windows"])
    def read_registration_windows(
            window_id: Optional[str] = Query(None, description="Selected by window_id"),
            doctor_id: Optional[int] = Query(None, description="Selected by doctor_id"),
            skip: int = 0,
            limit: int = 100,
            db: Session = Depends(get_db)
    ):
        windows = crud.registration_window.crud_registration_window.get_multi_filtered(
            db=db,
            window_id=window_id,
            doctor_id=doctor_id,
            skip=skip,
            limit=limit
        )
        return windows

    @app.get("/registrations", response_model=List[schemas.registration.Registration], tags=["Registrations"])
    def read_registrations(
            db: Session = Depends(get_db),
            registration_id: Optional[str] = Query(None, description="Filter by Registration ID"),
            doctor_id: Optional[str] = Query(None, description="Filter by Doctor ID"),
            window_id: Optional[str] = Query(None, description="Filter by Window ID"),
            patient_id: Optional[str] = Query(None, description="Filter by Patient ID"),
            sort_by: str = Query('created_at', description="Field to sort by"),
            sort_order: str = Query('desc', description="Sort order: 'asc' or 'desc'"),
            skip: int = 0,
            limit: int = 100
    ):

        registrations = crud.registration.crud_registration.get_multi_filtered(
            db,
            registration_id=registration_id,
            doctor_id=doctor_id,
            window_id=window_id,
            patient_id=patient_id,
            sort_by=sort_by,
            sort_order=sort_order,
            skip=skip,
            limit=limit
        )
        return registrations
    # ====== 新增：Garage自定义查询路由（利用索引） ======
    garage_router = APIRouter(prefix="/garages", tags=["Garages"])

    @garage_router.get("/by_garage_id/{garage_id}", response_model=schemas.garage.Garage)
    def get_garage_by_id(garage_id: str, db: Session = Depends(get_db)):
        garage = crud.garage.crud_garage.get_by_garage_id(db, garage_id=garage_id)
        if not garage:
            raise HTTPException(status_code=404, detail="Garage not found")
        return garage

    @garage_router.get("/available", response_model=List[schemas.garage.Garage])
    def get_available_garages(db: Session = Depends(get_db)):
        return crud.garage.crud_garage.get_available_garages(db)

    # ====== 新增：Parking自定义查询路由（利用索引） ======
    parking_router = APIRouter(prefix="/parkings", tags=["Parkings"])

    @parking_router.get("/by_garage_id/{garage_id}", response_model=List[schemas.parking.Parking])
    def get_parking_by_garage_id(garage_id: str, db: Session = Depends(get_db)):
        return crud.parking.crud_parking.get_by_garage_id(db, garage_id=garage_id)

    @parking_router.get("/by_patient_id/{patient_id}", response_model=List[schemas.parking.Parking])
    def get_parking_by_patient_id(patient_id: str, db: Session = Depends(get_db)):
        parkings = crud.parking.crud_parking.get_by_patient_id(db, patient_id=patient_id)
        if not parkings:
            raise HTTPException(status_code=404, detail="No parking records for this patient")
        return parkings

    # 注册自定义路由到app
    app.include_router(garage_router)
    app.include_router(parking_router)


    # ====== 通用路由 ======
    @router.post("/", response_model=schema_response)
    def create(item_in: schema_create, db: Session = Depends(get_db)):
        return crud_obj.create(db, obj_in=item_in)

    @router.get("/{id}", response_model=schema_response)
    def read(id: str, db: Session = Depends(get_db)):
        item = crud_obj.get(db, id=id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        return item

    @router.get("/", response_model=List[schema_response])
    def read_multi(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        return crud_obj.get_multi(db, skip=skip, limit=limit)

    @router.put("/{id}", response_model=schema_response)
    def update(id: str, item_in: schema_update, db: Session = Depends(get_db)):
        item = crud_obj.get(db, id=id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        return crud_obj.update(db, db_obj=item, obj_in=item_in)

    @router.delete("/{id}", response_model=schema_response)
    def delete(id: str, db: Session = Depends(get_db)):
        item = crud_obj.get(db, id=id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        return crud_obj.remove(db, id=id)

    return router

routers_config = [
    ("/departments", "Departments", crud.department.crud_department, schemas.department.DepartmentCreate, schemas.department.DepartmentUpdate, schemas.department.Department),
    ("/doctors", "Doctors", crud.doctor.crud_doctor, schemas.doctor.DoctorCreate, schemas.doctor.DoctorUpdate, schemas.doctor.Doctor),
    ("/patients", "Patients", crud.patient.crud_patient, schemas.patient.PatientCreate, schemas.patient.PatientUpdate, schemas.patient.Patient),
    ("/pharmaceutical_factories", "Pharmaceutical Factories", crud.pharmaceutical_factory.crud_pharmaceutical_factory, schemas.pharmaceutical_factory.PharmaceuticalFactoryCreate, schemas.pharmaceutical_factory.PharmaceuticalFactoryUpdate, schemas.pharmaceutical_factory.PharmaceuticalFactory),
    ("/medicines", "Medicines", crud.medicine.crud_medicine, schemas.medicine.MedicineCreate, schemas.medicine.MedicineUpdate, schemas.medicine.Medicine),
    ("/registration_windows", "Registration Windows", crud.registration_window.crud_registration_window, schemas.registration_window.RegistrationWindowCreate, schemas.registration_window.RegistrationWindowUpdate, schemas.registration_window.RegistrationWindow),
    ("/registrations", "Registrations", crud.registration.crud_registration, schemas.registration.RegistrationCreate, schemas.registration.RegistrationUpdate, schemas.registration.Registration),
    ("/diagnoses", "Diagnoses", crud.diagnosis.crud_diagnosis, schemas.diagnosis.DiagnosisCreate, schemas.diagnosis.DiagnosisUpdate, schemas.diagnosis.Diagnosis),
    ("/treatments", "Treatments", crud.treatment.crud_treatment, schemas.treatment.TreatmentCreate, schemas.treatment.TreatmentUpdate, schemas.treatment.Treatment),
    ("/prescriptions", "Prescriptions", crud.prescription.crud_prescription, schemas.prescription.PrescriptionCreate, schemas.prescription.PrescriptionUpdate, schemas.prescription.Prescription),
    ("/stock_warnings", "Stock Warnings", crud.stock_warning.crud_stock_warning, schemas.stock_warning.StockWarningCreate, schemas.stock_warning.StockWarningUpdate, schemas.stock_warning.StockWarning),
    ("/garages", "Garages", crud.garage.crud_garage, schemas.garage.GarageCreate, schemas.garage.GarageUpdate, schemas.garage.Garage),
    ("/parkings", "Parkings", crud.parking.crud_parking, schemas.parking.ParkingCreate, schemas.parking.ParkingUpdate, schemas.parking.Parking),
]

for prefix, tag, crud_instance, s_create, s_update, s_resp in routers_config:
    app.include_router(create_router(prefix, tag, crud_instance, s_create, s_update, s_resp))

@app.get("/")
def root():
    return {"message": "Hospital Management System API is running"}
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)