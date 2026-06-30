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
        self.__items = []

    # --- Properties ---
    
    @property
    def items(self) -> list:
        """
        מחזיר עותק של רשימת הפריטים.
        
        דרישות:
        - להחזיר עותק (copy) ולא את הרשימה עצמה
        """
        return self.__items.copy()

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
        if item.name in self:
            return False
        self.__items.append(item)
        return True

    def remove_item(self, name: str) -> bool:
        """
        הסרת פריט לפי שם.
        
        Returns:
            True אם נמצא והוסר, False אחרת
        """
        for i in range(len(self)):
            if self[i] == name:
                self.__items.pop(i)
                return True
        return False

    def find_item(self, name: str) -> MenuItem|None:
        """
        חיפוש פריט לפי שם.
        
        Returns:
            הפריט אם נמצא, None אחרת
        """
        for item in self.items:
            if item.name == name:
                return item
        return None

    def update_price(self, name: str, new_price: float) -> bool:
        """
        עדכון מחיר פריט.
        
        דרישות:
        - למצוא את הפריט ולעדכן את המחיר שלו
        
        Returns:
            True אם נמצא ועודכן, False אחרת
        """
        for item in self.items:
            if item.name == name:
                item.price = new_price # לבדוק אם צריך super
        return False

    def get_by_category(self, category: str) -> list:
        """
        מחזיר את כל הפריטים בקטגוריה מסוימת.
        
        Returns:
            רשימת פריטים שה-get_category שלהם שווה לקטגוריה
        """
        searched_category = []
        for item in self:
            if item.get_category == category:
                searched_category.append(item)
        return searched_category

    def get_all_categories(self) -> list:
        """
        מחזיר רשימת כל הקטגוריות בתפריט.
        
        Returns:
            רשימה ללא כפילויות
        """
        categotries = set()
        for item in self:
            categotries.add(item.get_category)
        return list(categotries)

    def get_items_in_price_range(self, min_price: float, max_price: float) -> list:
        """
        מחזיר פריטים בטווח מחירים.
        
        Returns:
            רשימת פריטים שהמחיר שלהם בין min_price ל-max_price (כולל)
        """
        in_range = []
        for item in self:
            if min_price < item.price < max_price:
                in_range.append(item)
        return in_range

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
        pass
    
    # --- Magic Methods ---
    
    def __len__(self) -> int:
        """מחזיר כמות פריטים בתפריט"""
        return len(self.items)

    def __contains__(self, name: str) -> bool:
        """
        בדיקה אם פריט קיים בתפריט לפי שם.
        
        שימוש: "Hummus" in menu
        """
        for item in self:
            if item.name == name:
                return True
        return False

    def __iter__(self):
        """
        אפשרות לעבור על הפריטים בלולאה.
        
        שימוש: for item in menu: ...
        """
        return iter(self.items)

    def __getitem__(self, name: str) -> MenuItem:
        """
        גישה לפריט לפי שם.
        
        שימוש: menu["Hummus"]
        
        דרישות:
        - אם לא נמצא, להעלות KeyError עם הודעה "Item 'name' not found in menu"
        """
        for item in self:
            if item.name == name:
                return item
        raise KeyError(f"Item '{name}' not found in menu")

