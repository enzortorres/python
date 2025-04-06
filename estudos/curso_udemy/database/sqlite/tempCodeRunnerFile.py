cursor.execute(
    f"""
    DELETE FROM {TABLE_NAME}
    WHERE id > 2
    """
)
cursor.commit()