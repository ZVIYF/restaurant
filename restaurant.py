# restaurant.py - מחלקת המסעדה הראשית

from menu import Menu
from table import Table
from order import Order
from menu_item import MenuItem


class Restaurant:
    """
    המחלקה הראשית - מנהלת את כל המסעדה.
    
    שדות מופע:
        _name (str): שם המסעדה
        _menu (Menu): אובייקט התפריט
        _tables (list): רשימת השולחנות
        _active_orders (list): רשימת הזמנות פעילות
        _closed_orders (list): רשימת הזמנות שנסגרו
        _total_revenue (float): סה"כ הכנסות
    """
    
    def __init__(self, name: str):
        """
        אתחול מסעדה.
        
        דרישות:
        - לשמור את name ב-_name
        - ליצור Menu חדש ולשמור ב-_menu
        - לאתחל _tables, _active_orders, _closed_orders לרשימות ריקות
        - לאתחל _total_revenue ל-0.0
        
        Args:
            name: שם המסעדה
        """
        self.__name = name
        self.__menu = Menu()
        self.__tables = []
        self.__active_orders = []
        self.__closed_orders = []
        self.__total_revenue = 0.0

    # --- Properties ---
    
    @property
    def name(self) -> str:
        """מחזיר את שם המסעדה"""
        return self.__name

    @property
    def menu(self) -> Menu:
        """מחזיר את אובייקט התפריט"""
        return self.__menu

    # --- Table Management ---
    
    def add_table(self, table: Table):
        """הוספת שולחן למסעדה"""
        self.__tables.append(table)

    def get_table(self, number: int) -> Table|None:
        """
        שליפת שולחן לפי מספר.
        
        Returns:
            השולחן אם נמצא, None אחרת
        """
        for t in self.__tables:
            if t.number == number:
                return t
        return None

    def get_all_tables(self) -> list:
        """מחזיר עותק של רשימת כל השולחנות"""
        return self.__tables.copy()

    def get_free_tables(self) -> list:
        """מחזיר רשימת שולחנות פנויים"""
        free_tables = []
        for t in self.__tables:
            if not t.is_occupied:
                free_tables.append(t)
        return free_tables

    def get_occupied_tables(self) -> list:
        """מחזיר רשימת שולחנות תפוסים"""
        occupied_tables = []
        for t in self.__tables:
            if t.is_occupied():
                occupied_tables.append(t)
        return occupied_tables

    # --- Order Management ---
    
    def open_order(self, table_number: int) -> Order:
        """
        פתיחת הזמנה חדשה לשולחן.
        
        דרישות:
        - לבדוק שהשולחן קיים (אם לא, ValueError עם "Table X does not exist")
        - לבדוק שהשולחן פנוי (אם תפוס, ValueError עם "Table X is already occupied")
        - לסמן את השולחן כתפוס
        - ליצור Order חדש ולהוסיף לרשימת ההזמנות הפעילות
        
        Args:
            table_number: מספר השולחן
            
        Returns:
            ההזמנה החדשה
            
        Raises:
            ValueError: אם השולחן לא קיים או תפוס
        """
        for t in self.get_free_tables():
            if table_number == t.number:
                t.occupy()
                new_order =  Order(t)
                self.__active_orders.append(new_order)
                return new_order
        raise ValueError(f"Table #{table_number} does not exist or occupied")

    def get_active_orders(self) -> list:
        """מחזיר עותק של רשימת הזמנות פעילות"""
        return self.__active_orders.copy()

    def get_order_by_table(self, table_number: int) -> Order|None:
        """
        מחזיר הזמנה פעילה לפי מספר שולחן.
        
        Returns:
            ההזמנה אם נמצאה, None אחרת
        """
        for o in self.get_active_orders():
            if o.table.number == table_number:
                return o
        return None

    def close_order(self, order: Order, tip_percent: float = None) -> float:
        """
        סגירת הזמנה וחישוב סכום לתשלום.
        
        דרישות:
        - לבדוק שההזמנה ברשימת ההזמנות הפעילות (אם לא, ValueError עם "Order not found in active orders")
        - לחשב את הסכום הסופי
        - לקרוא ל-close של ההזמנה
        - להעביר מרשימת הפעילות לסגורות
        - להוסיף את הסכום ל-_total_revenue
        
        Args:
            order: ההזמנה לסגירה
            tip_percent: אחוז טיפ (ברירת מחדל: None)
            
        Returns:
            הסכום הסופי לתשלום
        """
        if order in self.get_active_orders():
            order_total = order.get_subtotal()
            self.__active_orders.remove(order)
            self.__total_revenue += order_total
            order.close()
            self.__closed_orders.append(order)
            return order_total
        raise ValueError("Order not found in active orders")



    # --- Statistics (Bonus) ---
    
    def get_total_revenue(self) -> float:
        """מחזיר סה"כ הכנסות"""
        return self.__total_revenue

    def get_orders_count(self) -> int:
        """מחזיר כמות הזמנות שנסגרו"""
        return len(self.__closed_orders)

    def get_average_order_value(self) -> float:
        """
        מחזיר ממוצע סכום הזמנה.
        
        Returns:
            ממוצע, או 0.0 אם אין הזמנות
        """
        return self.get_total_revenue() / self.get_orders_count()

    def get_most_popular_item(self) -> tuple:
        """
        מחזיר את הפריט שהוזמן הכי הרבה.
        
        דרישות:
        - לעבור על כל ההזמנות הסגורות
        - לספור כמה פעמים כל פריט הוזמן
        - להחזיר את הפריט עם הספירה הגבוהה ביותר
        
        Returns:
            (item_name, count) או (None, 0) אם אין נתונים
        """
        items_count = {}
        for o in self.get_orders_count():
            for item in o.items:
                if item.name not in items_count:
                    items_count[item.name] = 0
                items_count[item.name] += item.quantity
        most_ordered = None
        if len(items_count) == 0:
            return None, 0
        for key, value in items_count.items():
            if most_ordered is None:
                most_ordered = key, value
            if value > most_ordered[1]:
                most_ordered = (key, value)
        return self.menu.__getitem__(most_ordered[0]), most_ordered[1]

    def get_revenue_by_category(self) -> dict:
        """
        מחזיר הכנסות מחולקות לפי קטגוריה.
        
        Returns:
            מילון {category: amount}
        """
        category_revenue = {}
        for o in self.get_orders_count():
            for item in o.items:
                if item.menu_item.category not in category_revenue:
                    category_revenue[item.menu_item.category] = 0
                category_revenue[item.menu_item.category] += item.subtotal()
        return category_revenue

    # --- Magic Methods ---
    
    def __str__(self) -> str:
        """
        ייצוג מחרוזת.
        
        Returns:
            "Restaurant 'name' - X tables, Y menu items"
        """
        return f"Restaurant {self.name} - {len(self.__tables)} tables, {len(self.menu)} menu items"
