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
        self.price = price
        self.__name = name
        self.description = description

    # --- Properties ---
    
    @property
    def name(self) -> str:
        """מחזיר את שם הפריט"""
        return self.__name

    @property
    def price(self) -> float:
        """מחזיר את מחיר הפריט"""
        return self.__price

    @price.setter
    def price(self, value: float):
        """
        קובע את מחיר הפריט.

        דרישות:
        - אם המחיר שלילי, להעלות ValueError עם הודעה "Price cannot be negative"
        - אחרת, לשמור את הערך ב-_price
        """
        if value < 0:
            raise ValueError("Price can't be negative!")
        self.__price = value

    @property
    def description(self) -> str:
        """מחזיר את תיאור הפריט"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """קובע את תיאור הפריט"""
        self.__description = value

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
        return "General"

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
        return f"${price:.2f}"

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
        return f"{self.name} - {MenuItem.format_price(self.price)}"

    def __repr__(self) -> str:
        """
        מחזיר ייצוג טכני.
        
        Returns:
            לדוגמה: "MenuItem(name='Hummus', price=32.0, description='desc')"
        """
        return f"MenuItem(name='{self.name}', price={self.price}, description='{self.description}')"

    def __eq__(self, other) -> bool:
        """
        השוואה בין פריטים לפי שם.
        
        דרישות:
        - אם other הוא MenuItem, להשוות לפי name
        - אחרת, להחזיר False
        """
        if isinstance(other, MenuItem):
            return self.name == other.name
        return False


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
        super().__init__(name, price, description)
        self.__selected_bread = None

    # --- Properties ---
    
    @property
    def selected_bread(self) -> str:
        """מחזיר את סוג הלחם שנבחר (או None)"""
        return self.__selected_bread

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
        if self.selected_bread is None:
            if (bread_type in Appetizer._bread_inventory
            and Appetizer._bread_inventory[bread_type] > 0):
                    self.selected_bread = bread_type
                    Appetizer._bread_inventory[bread_type] -= 1
                    return True
        return False

    def remove_bread(self):
        """
        ביטול בחירת לחם.
        
        דרישות:
        - אם יש לחם נבחר: להחזיר 1 למלאי ולאפס את _selected_bread
        """
        if self.selected_bread is not None:
            Appetizer._bread_inventory[self.selected_bread] += 1
            self.selected_bread = None

    def get_total_price(self) -> float:
        """
        מחזיר מחיר כולל לחם.
        
        Returns:
            מחיר + BREAD_PRICE אם נבחר לחם, אחרת רק המחיר
        """
        if self.selected_bread is not None:
           return self.price + Appetizer.BREAD_PRICE
        return self.price

    def get_category(self) -> str:
        """מחזיר 'Appetizers'"""
        return "Appetizers"

    # --- Class Methods ---
    
    @classmethod
    def get_available_breads(cls) -> list:
        """
        מחזיר רשימת סוגי לחמים זמינים.
        
        Returns:
            רשימה של סוגי לחם שהכמות שלהם > 0
        """
        breads = []
        for b in Appetizer._bread_inventory:
            if Appetizer._bread_inventory[b] > 0:
                breads.append(b)
        return breads

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
        if bread_type not in cls._bread_inventory:
            cls._bread_inventory[bread_type] = 0
        cls._bread_inventory[bread_type] += quantity

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
        if cls._bread_inventory[bread_type] >= quantity:
            cls._bread_inventory[bread_type] -= quantity
            return True
        return False

    @classmethod
    def get_bread_quantity(cls, bread_type: str) -> int:
        """
        מחזיר כמות מסוג לחם מסוים.
        
        Returns:
            הכמות במלאי, או 0 אם לא קיים
        """
        if bread_type in cls._bread_inventory:
            return cls._bread_inventory[bread_type]
        return 0

    @classmethod
    def get_bread_inventory(cls) -> dict:
        """מחזיר עותק של מילון המלאי"""
        return cls._bread_inventory.copy()

    # --- Magic Methods ---
    
    def __str__(self) -> str:
        """
        ייצוג מחרוזת כולל פרטי לחם.
        
        Returns:
            "name - $price" או "name - $price (with bread_type +$5.00)"
        """
        return f"{self.name} - {MenuItem.format_price(self.price)}"

    @selected_bread.setter
    def selected_bread(self, value):
        self.__selected_bread = value


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
        super().__init__(name, price, description)
        self.__selected_side = None

    @property
    def selected_side(self) -> str:
        """מחזיר את התוספת שנבחרה (או None)"""
        return self.__selected_side()

    def select_side(self, side: str) -> bool:
        """
        בחירת תוספת.
        
        דרישות:
        - לבדוק שהתוספת קיימת ברשימת האפשרויות
        - אם כן: לעדכן _selected_side ולהחזיר True
        - אם לא: להחזיר False
        """
        if side in MainCourse.get_side_options():
            self.__selected_side = side
            return True
        return False

    def get_category(self) -> str:
        """מחזיר 'Main Courses'"""
        return 'Main Courses'

    @classmethod
    def get_side_options(cls) -> list:
        """מחזיר עותק של רשימת התוספות"""
        return MainCourse._side_options.copy()

    @classmethod
    def add_side_option(cls, side: str):
        """
        הוספת תוספת חדשה לרשימה.
        
        דרישות:
        - להוסיף רק אם לא קיימת כבר
        """
        if side not in cls.get_side_options():
            MainCourse._side_options.append(side)

    @classmethod
    def remove_side_option(cls, side: str):
        """הסרת תוספת מהרשימה (אם קיימת)"""
        if side in cls.get_side_options():
            MainCourse._side_options.remove(side)

    def __str__(self) -> str:
        """
        ייצוג מחרוזת כולל תוספת.
        
        Returns:
            "name - $price" או "name - $price (with side)"
        """
        if self.selected_side is None:
            return (f"{self.name} - {MenuItem.format_price(self.price)}")
        return f"{self.name} - {MenuItem.format_price(self.price)} (with {self.selected_side})"

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
        super().__init__(name, price, description)
        self.__is_sugar_free = is_sugar_free


    @property
    def is_sugar_free(self) -> bool:
        """מחזיר האם הקינוח ללא סוכר"""
        return self.__is_sugar_free

    def get_category(self) -> str:
        """מחזיר 'Desserts'"""
        return "Desserts"

    def __str__(self) -> str:
        """
        ייצוג מחרוזת.
        
        Returns:
            "name - $price" או "name - $price (sugar-free)"
        """
        if not self.is_sugar_free:
            return f"{self.name} - {MenuItem.format_price(self.price)}"
        return f"{self.name} - {MenuItem.format_price(self.price)} (sugar-free)"

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
        super().__init__(name, price, description)
        self.size = size
        self.__is_cold = is_cold

    @property
    def size(self) -> str:
        """מחזיר את גודל המשקה"""
        return self.__size

    @size.setter
    def size(self, value: str):
        """
        קובע את גודל המשקה.
        
        דרישות:
        - אם הגודל לא ברשימת SIZES, להעלות ValueError עם הודעה "Size must be one of: ['S', 'M', 'L']"
        """
        if value in Beverage.SIZES:
            self.__size = value
        else:
            raise ValueError("Size must be one of: ['S', 'M', 'L']")

    @property
    def is_cold(self) -> bool:
        """מחזיר האם המשקה קר"""
        return self.__is_cold

    def get_category(self) -> str:
        """מחזיר 'Beverages'"""
        return "Beverages"

    @staticmethod
    def get_size_multiplier(size: str) -> float:
        """
        מחזיר מכפיל מחיר לפי גודל.
        
        Returns:
            S -> 0.8, M -> 1.0, L -> 1.3
        """
        if size == "S":
            return 0.8
        if size == "L":
            return 1.3
        return 1.0

    def get_total_price(self) -> float:
        """
        מחזיר מחיר לפי גודל.
        
        Returns:
            מחיר בסיס כפול מכפיל הגודל
        """
        return self.price * Beverage.get_size_multiplier(self.size)

    def __str__(self) -> str:
        """
        ייצוג מחרוזת כולל גודל וטמפרטורה.
        
        Returns:
            "name (size, cold/hot) - $price"
        """
        return f"{self.name} ({self.size}, {self.is_cold}) - {MenuItem.format_price(self.get_total_price())}"
