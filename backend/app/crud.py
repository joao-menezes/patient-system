from sqlalchemy.orm import Session

from . import schemas, models

def read_patient(db: Session, patient_id: int):
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()

def read_patients(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Patient).offset(skip).limit(limit).all()

def create_patient(db: Session, patient: schemas.CreatePatient):
    db_patient = models.Patient(name=patient.name, 
                                birth_date=patient.birth_date, 
                                height=patient.height,
                                weight=patient.weight,
                                blood_type=patient.blood_type,
                                sex=patient.sex
                                )
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def delete_patient(db: Session, patient_id: int):
    result = db.delete(read_patient(db, patient_id=patient_id))
    db.commit()
    return result