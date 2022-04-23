from app.database import get_db


def output_formatter(results):
    out = []
    for result in results:
        result_dict = {
            "id": result[0],
            "color": result[1],
            "licence_plate": result[2],
            "v_type": result[3],
            "owner_id": result[4],
            "active": result[5],
        }
        out.append(result_dict)
    return out


def insert(vehicle_dict):
    value_tuple = (
        vehicle_dict.get("color"),
        vehicle_dict.get("licence_plate"),
        vehicle_dict.get("v_type"),
        vehicle_dict.get("owner_id"),
        vehicle_dict.get("active")
    )
    statement = """
        INSERT INTO vehicle (
            color,
            licence_plate,
            v_type,
            owner_id,
            active
        ) VALUES (?, ?, ?)
    """
    cursor = get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close()


def scan():
    cursor = get_db().execute("SELECT * FROM vehicle WHERE active=1", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def select_by_id(pk):
    cursor = get_db().execute("SELECT * FROM vehicle WHERE id=?", (pk,))
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)

def deactivate(pk, vehicle_data):
    statement = """
        UPDATE vehicle 
        SET active=0
        WHERE id=?
    """
    cursor = get_db()
    cursor.execute(statement, pk)
    cursor.commit()
    cursor.close()


    
def update(pk, vehicle_data):
    value_tuple = (
        vehicle_data.get("color"),
        vehicle_data.get("licence_plate"),
        vehicle_data.get("v_type"),
        vehicle_data.get("owner_id"),
        vehicle_data.get("active"),
        pk
    )
    statement = """
        UPDATE vehicle
        SET color=?,
        licence_plate=?,
        v_type=?
        owner_id=?
        active=?
        WHERE id=?
    """
    cursor = get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close()