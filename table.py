# table.py - מחלקת שולחן


class Table:
    """
    שולחן במסעדה.
    
    שדות מחלקה:
        total_tables (int): סה"כ שולחנות שנוצרו (מתעדכן בכל יצירה)
    
    שדות מופע:
        _number (int): מספר השולחן (פרטי)
        _seats (int): כמות מקומות ישיבה (פרטי)
        _is_occupied (bool): האם תפוס (פרטי)
    """
    
    total_tables: int = 0
    
    def __init__(self, number: int, seats: int = 4):
        """
        אתחול שולחן.
        
        דרישות:
        - לשמור את number ב-_number
        - לשמור את seats ב-_seats
        - לאתחל _is_occupied ל-False
        - להעלות את total_tables ב-1
        
        Args:
            number: מספר השולחן
            seats: כמות מקומות (ברירת מחדל: 4)
        """
        raise NotImplementedError("Implement this method")
    
    # --- Properties ---
    
    @property
    def number(self) -> int:
        """מחזיר את מספר השולחן"""
        raise NotImplementedError("Implement this method")
    
    @property
    def seats(self) -> int:
        """מחזיר את כמות המקומות"""
        raise NotImplementedError("Implement this method")
    
    @property
    def is_occupied(self) -> bool:
        """מחזיר האם השולחן תפוס"""
        raise NotImplementedError("Implement this method")
    
    # --- Methods ---
    
    def occupy(self) -> bool:
        """
        סימון השולחן כתפוס.
        
        דרישות:
        - אם כבר תפוס: להחזיר False
        - אחרת: לסמן כתפוס ולהחזיר True
        
        Returns:
            True אם הצליח, False אם כבר היה תפוס
        """
        raise NotImplementedError("Implement this method")
    
    def free(self):
        """סימון השולחן כפנוי"""
        raise NotImplementedError("Implement this method")
    
    # --- Magic Methods ---
    
    def __str__(self) -> str:
        """
        ייצוג מחרוזת.
        
        Returns:
            "Table X (Y seats) - Free/Occupied"
        """
        raise NotImplementedError("Implement this method")
