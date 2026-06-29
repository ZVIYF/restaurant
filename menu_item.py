# menu_item.py - מחלקת פריט תפריט ותתי-מחלקות


class MenuItem:
    """
    מחלקת בסיס לפריט בתפריט.
    
    שדות:
        _name (str): שם המנה (פרטי)
        _price (float): מחיר המנה (פרטי)
        _description (str): תיאור קצר (פרטי)
    """
    
    def __init__(self, name: str, price: float, description: str = ""):
        """
        אתחול פריט תפריט.
        
        דרישות:
        - לשמור את name ב-_name
        - לשמור את description ב-_description  
        - להשתמש ב-setter של price (לצורך ולידציה)
        
        Args:
            name: שם הפריט
            price: מחיר (חייב להיות אי-שלילי)
            description: תיאור (ברירת מחדל: מחרוזת ריקה)
        """
        raise NotImplementedError("Implement this method")
    
    # --- Properties ---
    
    @property
    def name(self) -> str:
        """מחזיר את שם הפריט"""
        raise NotImplementedError("Implement this method")
    
    @property
    def price(self) -> float:
        """מחזיר את מחיר הפריט"""
        raise NotImplementedError("Implement this method")
    
    @price.setter
    def price(self, value: float):
        """
        קובע את מחיר הפריט.
        
        דרישות:
        - אם המחיר שלילי, להעלות ValueError עם הודעה "Price cannot be negative"
        - אחרת, לשמור את הערך ב-_price
        """
        raise NotImplementedError("Implement this method")
    
    @property
    def description(self) -> str:
        """מחזיר את תיאור הפריט"""
        raise NotImplementedError("Implement this method")
    
    @description.setter
    def description(self, value: str):
        """קובע את תיאור הפריט"""
        raise NotImplementedError("Implement this method")
    
    # --- Methods ---
    
    def get_category(self) -> str:
        """
        מחזיר את קטגוריית הפריט.
        
        דרישות:
        - במחלקת הבסיס, להחזיר "General"
        - בתתי-מחלקות, לדרוס ולהחזיר קטגוריה מתאימה
        
        Returns:
            שם הקטגוריה כמחרוזת
        """
        raise NotImplementedError("Implement this method")
    
    @staticmethod
    def format_price(price: float) -> str:
        """
        מחזיר מחיר מפורמט עם סימן $.
        
        דרישות:
        - להחזיר מחרוזת בפורמט "$XX.XX" (שתי ספרות אחרי הנקודה)
        
        Args:
            price: המחיר לפרמוט
            
        Returns:
            מחרוזת מפורמטת, לדוגמה: "$32.00"
        """
        raise NotImplementedError("Implement this method")
    
    # --- Magic Methods ---
    
    def __str__(self) -> str:
        """
        מחזיר ייצוג מחרוזת ידידותי.
        
        דרישות:
        - להחזיר: "name - $price"
        - להשתמש ב-format_price
        
        Returns:
            לדוגמה: "Hummus - $32.00"
        """
        raise NotImplementedError("Implement this method")
    
    def __repr__(self) -> str:
        """
        מחזיר ייצוג טכני.
        
        Returns:
            לדוגמה: "MenuItem(name='Hummus', price=32.0, description='desc')"
        """
        raise NotImplementedError("Implement this method")
    
    def __eq__(self, other) -> bool:
        """
        השוואה בין פריטים לפי שם.
        
        דרישות:
        - אם other הוא MenuItem, להשוות לפי name
        - אחרת, להחזיר False
        """
        raise NotImplementedError("Implement this method")


class Appetizer(MenuItem):
    """
    מנה ראשונה - עם אפשרות להוסיף לחם.
    
    שדות מחלקה:
        _bread_inventory (dict): מילון {סוג_לחם: כמות} - משותף לכל המופעים
        BREAD_PRICE (float): מחיר תוספת לחם (קבוע: 5.0)
    
    שדות מופע:
        _selected_bread (str או None): סוג הלחם שנבחר
    """
    
    # משתני מחלקה
    _bread_inventory: dict = {}
    BREAD_PRICE: float = 5.0
    
    def __init__(self, name: str, price: float, description: str = ""):
        """
        אתחול מנה ראשונה.
        
        דרישות:
        - לקרוא ל-__init__ של מחלקת האב
        - לאתחל _selected_bread ל-None
        """
        raise NotImplementedError("Implement this method")
    
    # --- Properties ---
    
    @property
    def selected_bread(self) -> str:
        """מחזיר את סוג הלחם שנבחר (או None)"""
        raise NotImplementedError("Implement this method")
    
    # --- Instance Methods ---
    
    def add_bread(self, bread_type: str) -> bool:
        """
        בחירת סוג לחם מהמלאי.
        
        דרישות:
        - לבדוק שסוג הלחם קיים במלאי וכמותו > 0
        - אם כן: לעדכן _selected_bread, להוריד 1 מהמלאי, להחזיר True
        - אם לא: להחזיר False
        
        Args:
            bread_type: סוג הלחם המבוקש
            
        Returns:
            True אם הצליח, False אחרת
        """
        raise NotImplementedError("Implement this method")
    
    def remove_bread(self):
        """
        ביטול בחירת לחם.
        
        דרישות:
        - אם יש לחם נבחר: להחזיר 1 למלאי ולאפס את _selected_bread
        """
        raise NotImplementedError("Implement this method")
    
    def get_total_price(self) -> float:
        """
        מחזיר מחיר כולל לחם.
        
        Returns:
            מחיר + BREAD_PRICE אם נבחר לחם, אחרת רק המחיר
        """
        raise NotImplementedError("Implement this method")
    
    def get_category(self) -> str:
        """מחזיר 'Appetizers'"""
        raise NotImplementedError("Implement this method")
    
    # --- Class Methods ---
    
    @classmethod
    def get_available_breads(cls) -> list:
        """
        מחזיר רשימת סוגי לחמים זמינים.
        
        Returns:
            רשימה של סוגי לחם שהכמות שלהם > 0
        """
        raise NotImplementedError("Implement this method")
    
    @classmethod
    def add_bread_to_inventory(cls, bread_type: str, quantity: int):
        """
        הוספת לחמים למלאי.
        
        דרישות:
        - אם סוג הלחם קיים: להוסיף לכמות הקיימת
        - אם לא קיים: להוסיף מפתח חדש עם הכמות
        
        Args:
            bread_type: סוג הלחם
            quantity: כמות להוספה
        """
        raise NotImplementedError("Implement this method")
    
    @classmethod
    def remove_bread_from_inventory(cls, bread_type: str, quantity: int) -> bool:
        """
        הורדת לחמים מהמלאי.
        
        דרישות:
        - לבדוק שיש מספיק במלאי
        - אם כן: להוריד ולהחזיר True
        - אם לא: להחזיר False
        
        Returns:
            True אם הצליח, False אחרת
        """
        raise NotImplementedError("Implement this method")
    
    @classmethod
    def get_bread_quantity(cls, bread_type: str) -> int:
        """
        מחזיר כמות מסוג לחם מסוים.
        
        Returns:
            הכמות במלאי, או 0 אם לא קיים
        """
        raise NotImplementedError("Implement this method")
    
    @classmethod
    def get_bread_inventory(cls) -> dict:
        """מחזיר עותק של מילון המלאי"""
        raise NotImplementedError("Implement this method")
    
    # --- Magic Methods ---
    
    def __str__(self) -> str:
        """
        ייצוג מחרוזת כולל פרטי לחם.
        
        Returns:
            "name - $price" או "name - $price (with bread_type +$5.00)"
        """
        raise NotImplementedError("Implement this method")


class MainCourse(MenuItem):
    """
    מנה עיקרית - עם בחירת תוספת.
    
    שדות מחלקה:
        _side_options (list): רשימת תוספות אפשריות
    
    שדות מופע:
        _selected_side (str או None): התוספת שנבחרה
    """
    
    _side_options: list = []
    
    def __init__(self, name: str, price: float, description: str = ""):
        """
        אתחול מנה עיקרית.
        
        דרישות:
        - לקרוא ל-__init__ של מחלקת האב
        - לאתחל _selected_side ל-None
        """
        raise NotImplementedError("Implement this method")
    
    @property
    def selected_side(self) -> str:
        """מחזיר את התוספת שנבחרה (או None)"""
        raise NotImplementedError("Implement this method")
    
    def select_side(self, side: str) -> bool:
        """
        בחירת תוספת.
        
        דרישות:
        - לבדוק שהתוספת קיימת ברשימת האפשרויות
        - אם כן: לעדכן _selected_side ולהחזיר True
        - אם לא: להחזיר False
        """
        raise NotImplementedError("Implement this method")
    
    def get_category(self) -> str:
        """מחזיר 'Main Courses'"""
        raise NotImplementedError("Implement this method")
    
    @classmethod
    def get_side_options(cls) -> list:
        """מחזיר עותק של רשימת התוספות"""
        raise NotImplementedError("Implement this method")
    
    @classmethod
    def add_side_option(cls, side: str):
        """
        הוספת תוספת חדשה לרשימה.
        
        דרישות:
        - להוסיף רק אם לא קיימת כבר
        """
        raise NotImplementedError("Implement this method")
    
    @classmethod
    def remove_side_option(cls, side: str):
        """הסרת תוספת מהרשימה (אם קיימת)"""
        raise NotImplementedError("Implement this method")
    
    def __str__(self) -> str:
        """
        ייצוג מחרוזת כולל תוספת.
        
        Returns:
            "name - $price" או "name - $price (with side)"
        """
        raise NotImplementedError("Implement this method")


class Dessert(MenuItem):
    """
    קינוח - עם אפשרות לסימון ללא סוכר.
    
    שדות מופע:
        _is_sugar_free (bool): האם ללא סוכר
    """
    
    def __init__(self, name: str, price: float, description: str = "", is_sugar_free: bool = False):
        """
        אתחול קינוח.
        
        דרישות:
        - לקרוא ל-__init__ של מחלקת האב
        - לשמור את is_sugar_free ב-_is_sugar_free
        """
        raise NotImplementedError("Implement this method")
    
    @property
    def is_sugar_free(self) -> bool:
        """מחזיר האם הקינוח ללא סוכר"""
        raise NotImplementedError("Implement this method")
    
    def get_category(self) -> str:
        """מחזיר 'Desserts'"""
        raise NotImplementedError("Implement this method")
    
    def __str__(self) -> str:
        """
        ייצוג מחרוזת.
        
        Returns:
            "name - $price" או "name - $price (sugar-free)"
        """
        raise NotImplementedError("Implement this method")


class Beverage(MenuItem):
    """
    משקה - עם גודל ומצב חם/קר.
    
    שדות מחלקה:
        SIZES (list): גדלים אפשריים ["S", "M", "L"]
    
    שדות מופע:
        _size (str): גודל המשקה
        _is_cold (bool): האם קר
    """
    
    SIZES = ["S", "M", "L"]
    
    def __init__(self, name: str, price: float, description: str = "", 
                 size: str = "M", is_cold: bool = True):
        """
        אתחול משקה.
        
        דרישות:
        - לקרוא ל-__init__ של מחלקת האב
        - להשתמש ב-setter של size (לולידציה)
        - לשמור את is_cold ב-_is_cold
        """
        raise NotImplementedError("Implement this method")
    
    @property
    def size(self) -> str:
        """מחזיר את גודל המשקה"""
        raise NotImplementedError("Implement this method")
    
    @size.setter
    def size(self, value: str):
        """
        קובע את גודל המשקה.
        
        דרישות:
        - אם הגודל לא ברשימת SIZES, להעלות ValueError עם הודעה "Size must be one of: ['S', 'M', 'L']"
        """
        raise NotImplementedError("Implement this method")
    
    @property
    def is_cold(self) -> bool:
        """מחזיר האם המשקה קר"""
        raise NotImplementedError("Implement this method")
    
    def get_category(self) -> str:
        """מחזיר 'Beverages'"""
        raise NotImplementedError("Implement this method")
    
    @staticmethod
    def get_size_multiplier(size: str) -> float:
        """
        מחזיר מכפיל מחיר לפי גודל.
        
        Returns:
            S -> 0.8, M -> 1.0, L -> 1.3
        """
        raise NotImplementedError("Implement this method")
    
    def get_total_price(self) -> float:
        """
        מחזיר מחיר לפי גודל.
        
        Returns:
            מחיר בסיס כפול מכפיל הגודל
        """
        raise NotImplementedError("Implement this method")
    
    def __str__(self) -> str:
        """
        ייצוג מחרוזת כולל גודל וטמפרטורה.
        
        Returns:
            "name (size, cold/hot) - $price"
        """
        raise NotImplementedError("Implement this method")
