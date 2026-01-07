from src.database import SessionLocal, BeyondMessage, Branch

def Get_Branch_DB(user_id: int):
    db = SessionLocal()

    rows = db.query(
        Branch.branch_name,
        Branch.input_id,
        Branch.output_id,
    ).filter(Branch.user_id == user_id).all()

    db.close()
    return rows

def Get_Addition_DB(user_id: int):
    db = SessionLocal()

    rows = db.query(
        BeyondMessage.addition,
    ).filter(BeyondMessage.user_id == user_id).first()

    db.close()
    return rows