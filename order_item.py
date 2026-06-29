# order_item.py - מחלקת פריט בהזמנה

from menu_item import MenuItem


class OrderItem:
    """
    פריט בודד בהזמנה - מכיל MenuItem + כמות + הערות.
    
    שדות מופע:
        _menu_item (MenuItem): הפריט מהתפריט (פרטי)
        _quantity (int): כמות (פרטי)
        _notes (str): הערות מיוחדות (פרטי)
    """
    
    def __init__(self, menu_item: MenuItem, quantity: int = 1, notes: str = ""):
        """
        אתחול פריט בהזמנה.
        
        דרישות:
        - לשמור את menu_item ב-_menu_item
        - להשתמש ב-setter של quantity (לולידציה)
        - לשמור את notes ב-_notes
        
        Args:
            menu_item: הפריט מהתפריט
            quantity: כמות (ברירת מחדל: 1)
            notes: הערות (ברירת מחדל: מחרוזת ריקה)
        """
        raise NotImplementedError("Implement this method")
    
    # --- Properties ---
    
    @property
    def menu_item(self) -> MenuItem:
        """מחזיר את הפריט מהתפריט"""
        raise NotImplementedError("Implement this method")
    
    @property
    def quantity(self) -> int:
        """מחזיר את הכמות"""
        raise NotImplementedError("Implement this method")
    
    @quantity.setter
    def quantity(self, value: int):
        """
        קובע את הכמות.
        
        דרישות:
        - אם הכמות קטנה מ-1, להעלות ValueError עם הודעה "Quantity must be at least 1"
        """
        raise NotImplementedError("Implement this method")
    
    @property
    def notes(self) -> str:
        """מחזיר את ההערות"""
        raise NotImplementedError("Implement this method")
    
    @notes.setter
    def notes(self, value: str):
        """קובע את ההערות"""
        raise NotImplementedError("Implement this method")
    
    @property
    def subtotal(self) -> float:
        """
        מחזיר סכום ביניים (מחיר × כמות).
        
        דרישות:
        - אם לפריט יש מתודת get_total_price (כמו Appetizer, Beverage), להשתמש בה
        - אחרת, להשתמש ב-price רגיל
        - להכפיל בכמות
        
        Returns:
            מחיר × כמות
        """
        raise NotImplementedError("Implement this method")
    
    # --- Magic Methods ---
    
    def __str__(self) -> str:
        """
        ייצוג מחרוזת.
        
        Returns:
            "quantity x name = $subtotal" או "quantity x name = $subtotal (notes)"
        """
        raise NotImplementedError("Implement this method")
