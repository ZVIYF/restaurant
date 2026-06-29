# order.py - מחלקת הזמנה

from datetime import datetime
from os import remove

from menu_item import MenuItem
from order_item import OrderItem
from table import Table


class Order:
    """
    הזמנה שלמה של שולחן.
    
    שדות מחלקה:
        _order_counter (int): מונה הזמנות - עולה ב-1 בכל יצירה (פרטי)
        DEFAULT_TIP_PERCENT (float): אחוז טיפ ברירת מחדל (10.0)
    
    שדות מופע:
        _order_id (int): מזהה ייחודי (נקבע אוטומטית מהמונה)
        _table (Table): אובייקט השולחן
        _items (list): רשימת OrderItem
        _created_at (datetime): זמן פתיחת ההזמנה
        _is_closed (bool): האם ההזמנה נסגרה
    """
    
    _order_counter: int = 0
    DEFAULT_TIP_PERCENT: float = 10.0
    
    def __init__(self, table: Table):
        """
        אתחול הזמנה.
        
        דרישות:
        - להעלות את _order_counter ב-1
        - לשמור את הערך החדש של המונה ב-_order_id
        - לשמור את table ב-_table
        - לאתחל _items לרשימה ריקה
        - לשמור את הזמן הנוכחי ב-_created_at (datetime.now())
        - לאתחל _is_closed ל-False
        
        Args:
            table: אובייקט השולחן
        """
        Order._order_counter += 1
        self.__order_id = Order._order_counter
        self.__table = table
        self.__items = []
        self.__created_at = datetime.now()
        self.__is_closed = False

    # --- Properties ---
    
    @property
    def order_id(self) -> int:
        """מחזיר את מזהה ההזמנה"""
        return self.__order_id

    @property
    def table(self) -> Table:
        """מחזיר את אובייקט השולחן"""
        return self.__table

    @property
    def items(self) -> list:
        """
        מחזיר עותק של רשימת הפריטים.
        
        דרישות:
        - להחזיר עותק (copy) ולא את הרשימה עצמה
        """
        return self.__items.copy()

    @property
    def is_closed(self) -> bool:
        """מחזיר האם ההזמנה נסגרה"""
        return self.__is_closed

    @property
    def created_at(self) -> datetime:
        """מחזיר את זמן יצירת ההזמנה"""
        return self.__created_at

    # --- Methods ---
    
    def add_item(self, menu_item: MenuItem, quantity: int = 1, notes: str = "") -> OrderItem:
        """
        הוספת פריט להזמנה.
        
        דרישות:
        - אם ההזמנה סגורה, להעלות Exception עם הודעה "Cannot add items to closed order"
        - לבדוק אם הפריט כבר קיים (לפי שם ואותן הערות)
          - אם כן: להוסיף לכמות הקיימת
          - אם לא: ליצור OrderItem חדש ולהוסיף לרשימה
        - להחזיר את ה-OrderItem
        
        Args:
            menu_item: הפריט מהתפריט
            quantity: כמות
            notes: הערות
            
        Returns:
            ה-OrderItem שנוסף/עודכן
        """
        if self.__is_closed:
            raise Exception("Cannot add items to closed order")
        for item in self.__items:
            if menu_item.name == item.name and item.order_item.notes == notes:
                item.quantity += quantity
                return item
        new_order_item = OrderItem(menu_item, quantity, notes)
        self.__items.append(new_order_item)
        return new_order_item


    def remove_item(self, menu_item: MenuItem) -> bool:
        """
        הסרת פריט מההזמנה.
        
        דרישות:
        - אם ההזמנה סגורה, להעלות Exception עם הודעה "Cannot remove items from closed order"
        - לחפש פריט עם אותו menu_item ולהסיר אותו
        
        Returns:
            True אם נמצא והוסר, False אחרת
        """
        if self.__is_closed:
            raise Exception("Cannot remove items from closed order")
        for i in range(len(self)):
            if self.__items[i].name == menu_item.name:
                self.__items.pop(i)
                return True
        return False

    def get_subtotal(self) -> float:
        """
        מחזיר סכום ביניים (לפני טיפ).
        
        Returns:
            סכום כל ה-subtotal של הפריטים
        """
        sub_sum = 0
        for item in self.__items:
            sub_sum += item.subtotal
        return sub_sum

    def get_total(self, tip_percent: float = None) -> float:
        """
        מחזיר סכום כולל עם טיפ.
        
        דרישות:
        - אם tip_percent הוא None, להשתמש ב-DEFAULT_TIP_PERCENT
        - לחשב: subtotal + (subtotal × tip_percent / 100)
        
        Args:
            tip_percent: אחוז טיפ (ברירת מחדל: None)
            
        Returns:
            סכום כולל טיפ
        """
        raise NotImplementedError("Implement this method")
    
    def get_bill(self, tip_percent: float = None) -> str:
        """
        מחזיר חשבון מפורט כמחרוזת.
        
        דרישות:
        - כותרת עם מספר הזמנה ושולחן
        - רשימת כל הפריטים
        - סכום ביניים (Subtotal)
        - טיפ (Tip) - סכום ואחוז
        - סכום סופי (Total)
        
        הפורמט:
        ========================================
        Bill - Order #X
        Table: Y
        Time: HH:MM:SS
        ========================================
        (items list)
        ----------------------------------------
        Subtotal: $XX.XX
        Tip (X%): $XX.XX
        ========================================
        Total: $XX.XX
        ========================================
        
        Returns:
            חשבון מפורמט
        """
        raise NotImplementedError("Implement this method")
    
    def close(self):
        """
        סגירת ההזמנה.
        
        דרישות:
        - לסמן את ההזמנה כסגורה
        - לשחרר את השולחן (לקרוא ל-free)
        """
        raise NotImplementedError("Implement this method")
    
    # --- Class Methods ---
    
    @classmethod
    def get_total_orders(cls) -> int:
        """מחזיר כמה הזמנות נוצרו בסה"כ"""
        raise NotImplementedError("Implement this method")
    
    # --- Magic Methods ---
    
    def __len__(self) -> int:
        """מחזיר כמות פריטים בהזמנה"""
        return len(self.__items)

    def __str__(self) -> str:
        """
        ייצוג מחרוזת.
        
        Returns:
            "Order #X (Table Y) - Z items - Open/Closed"
        """
        status = "Open"
        if self.__is_closed:
            status = "Closed"
        return f"Order #{self.__order_id} (Table {self.__table.number}) - {len(self)} items - {status}"
