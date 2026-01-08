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

    addition = db.query(
        BeyondMessage.addition,
    ).filter(BeyondMessage.user_id == user_id).first()

    db.close()
    return addition

class BranchNotFoundError(Exception):
    """branch is not found"""
    pass

def Set_Branch_Name(user_id: int, old_name: str, new_name: str):
    db = SessionLocal()

    try:
        branch_to_update = db.query(Branch).filter(
            Branch.user_id == user_id,
            Branch.branch_name == old_name
            ).update(
                {Branch.branch_name: new_name},
                synchronize_session=False
            )

        db.commit()

    except:
        db.rollback()
        raise
    finally:
        db.close()

def Set_Branch_Status(user_id: int, branch_name: str , status: bool):
    db = SessionLocal()

    try:
        branch_to_update = db.query(Branch).filter(
            Branch.user_id == user_id,
            Branch.branch_name == branch_name
        ).update(
            {Branch.status: status},
            synchronize_session=False
        )
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()
