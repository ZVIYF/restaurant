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
        self.__menu_item = menu_item
        self.quantity = quantity
        self.__notes = notes

    # --- Properties ---
    
    @property
    def name(self):
        return self.__menu_item.name

    @property
    def menu_item(self) -> MenuItem:
        """מחזיר את הפריט מהתפריט"""
        return self.__menu_item

    @property
    def quantity(self) -> int:
        """מחזיר את הכמות"""
        return self.__quantity

    @quantity.setter
    def quantity(self, value: int):
        """
        קובע את הכמות.
        
        דרישות:
        - אם הכמות קטנה מ-1, להעלות ValueError עם הודעה "Quantity must be at least 1"
        """
        if value < 1:
            raise ValueError("Quantity must be at least 1")
        self.__quantity = value

    @property
    def notes(self) -> str:
        """מחזיר את ההערות"""
        return self.__notes

    @notes.setter
    def notes(self, value: str):
        """קובע את ההערות"""
        self.__notes = value

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
        try:
            return self.menu_item.get_total_price * self.quantity
        except:
            return self.menu_item.price * self.quantity

    # --- Magic Methods ---
    
    def __str__(self) -> str:
        """
        ייצוג מחרוזת.
        
        Returns:
            "quantity x name = $subtotal" או "quantity x name = $subtotal (notes)"
        """
        if self.notes:
            return f"{self.quantity} x {self.name} = {self.subtotal} ({self.notes})"
        return f"{self.quantity} x {self.name} = {self.subtotal}"
