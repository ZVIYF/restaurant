# menu.py - מחלקת תפריט

from menu_item import MenuItem, Appetizer, MainCourse, Dessert, Beverage


class Menu:
    """
    תפריט המסעדה.
    
    שדות מופע:
        _items (list): רשימת פריטי התפריט
    """
    
    def __init__(self):
        """
        אתחול תפריט ריק.
        
        דרישות:
        - לאתחל _items לרשימה ריקה
        """
        raise NotImplementedError("Implement this method")
    
    # --- Properties ---
    
    @property
    def items(self) -> list:
        """
        מחזיר עותק של רשימת הפריטים.
        
        דרישות:
        - להחזיר עותק (copy) ולא את הרשימה עצמה
        """
        raise NotImplementedError("Implement this method")
    
    # --- Methods ---
    
    def add_item(self, item: MenuItem) -> bool:
        """
        הוספת פריט לתפריט.
        
        דרישות:
        - לבדוק שפריט עם אותו שם לא קיים כבר
        - אם קיים: להחזיר False
        - אם לא קיים: להוסיף ולהחזיר True
        
        Returns:
            True אם נוסף, False אם כבר קיים
        """
        raise NotImplementedError("Implement this method")
    
    def remove_item(self, name: str) -> bool:
        """
        הסרת פריט לפי שם.
        
        Returns:
            True אם נמצא והוסר, False אחרת
        """
        raise NotImplementedError("Implement this method")
    
    def find_item(self, name: str) -> MenuItem:
        """
        חיפוש פריט לפי שם.
        
        Returns:
            הפריט אם נמצא, None אחרת
        """
        raise NotImplementedError("Implement this method")
    
    def update_price(self, name: str, new_price: float) -> bool:
        """
        עדכון מחיר פריט.
        
        דרישות:
        - למצוא את הפריט ולעדכן את המחיר שלו
        
        Returns:
            True אם נמצא ועודכן, False אחרת
        """
        raise NotImplementedError("Implement this method")
    
    def get_by_category(self, category: str) -> list:
        """
        מחזיר את כל הפריטים בקטגוריה מסוימת.
        
        Returns:
            רשימת פריטים שה-get_category שלהם שווה לקטגוריה
        """
        raise NotImplementedError("Implement this method")
    
    def get_all_categories(self) -> list:
        """
        מחזיר רשימת כל הקטגוריות בתפריט.
        
        Returns:
            רשימה ללא כפילויות
        """
        raise NotImplementedError("Implement this method")
    
    def get_items_in_price_range(self, min_price: float, max_price: float) -> list:
        """
        מחזיר פריטים בטווח מחירים.
        
        Returns:
            רשימת פריטים שהמחיר שלהם בין min_price ל-max_price (כולל)
        """
        raise NotImplementedError("Implement this method")
    
    # --- Class Methods ---
    
    @classmethod
    def from_file(cls, filename: str) -> 'Menu':
        """
        יצירת תפריט מקובץ טקסט.
        
        פורמט הקובץ (כל שורה):
            type,name,price,description
        
        סוגים: "Appetizer", "MainCourse", "Dessert", "Beverage"
        
        דרישות:
        - לדלג על שורות ריקות או שמתחילות ב-#
        - ליצור את הפריט המתאים לפי הסוג
        - להוסיף לתפריט
        - אם הקובץ לא נמצא, להדפיס "File {filename} not found" ולהחזיר תפריט ריק
        
        Returns:
            אובייקט Menu חדש
        """
        raise NotImplementedError("Implement this method")
    
    # --- Magic Methods ---
    
    def __len__(self) -> int:
        """מחזיר כמות פריטים בתפריט"""
        raise NotImplementedError("Implement this method")
    
    def __contains__(self, name: str) -> bool:
        """
        בדיקה אם פריט קיים בתפריט לפי שם.
        
        שימוש: "Hummus" in menu
        """
        raise NotImplementedError("Implement this method")
    
    def __iter__(self):
        """
        אפשרות לעבור על הפריטים בלולאה.
        
        שימוש: for item in menu: ...
        """
        raise NotImplementedError("Implement this method")
    
    def __getitem__(self, name: str) -> MenuItem:
        """
        גישה לפריט לפי שם.
        
        שימוש: menu["Hummus"]
        
        דרישות:
        - אם לא נמצא, להעלות KeyError עם הודעה "Item 'name' not found in menu"
        """
        raise NotImplementedError("Implement this method")
