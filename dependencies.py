from database import SessionLocal, BeyondMessage, Branch

def Get_Branch_DB(user_id: int) -> list[tuple]:
    with SessionLocal() as db:
        rows = db.query(
            Branch.branch_name,
            Branch.input_id,
            Branch.output_id,
            Branch.status,
        ).filter(Branch.user_id == user_id).all()
        return rows

def Get_Addition_DB(user_id: int) -> str | None:
    with SessionLocal() as db:
        addition = db.query(
            BeyondMessage.addition,
        ).filter(BeyondMessage.user_id == user_id).first()
        
        return addition[0] if addition else None

def Set_Branch_Name(user_id: int, old_name: str, new_name: str) -> None:
    with SessionLocal() as db:
        db.query(Branch).filter(
            Branch.user_id == user_id,
            Branch.branch_name == old_name
        ).update(
            {Branch.branch_name: new_name},
            synchronize_session=False
        )
        db.commit()

def Set_Branch_Status(user_id: int, branch_name: str , status: bool) -> None:
    with SessionLocal() as db:
        db.query(Branch).filter(
            Branch.user_id == user_id,
            Branch.branch_name == branch_name
        ).update(
            {Branch.status: status},
            synchronize_session=False
        )
        db.commit()

def Get_Branch_Status(user_id: int, branch_name: str) -> bool | None:
    with SessionLocal() as db:
        status = db.query(Branch.status).filter(Branch.user_id == user_id, Branch.branch_name == branch_name).first()
        return status[0] if status else None

def Is_There_Branch(user_id: int) -> bool:
    return bool(Get_Branch_DB(user_id))

def Is_There_Branch_With_Name(user_id: int, branch_name: str) -> bool:
    with SessionLocal() as db:
        return bool(db.query(Branch.id).filter(Branch.user_id == user_id, Branch.branch_name == branch_name).first())

def Is_There_Addtion(user_id: int) -> bool:
    return bool(Get_Addition_DB(user_id))
