from datetime import datetime,timedelta
class Warehouse:
    def __init__(self):
        self.product = {
            "oil":[20,5],
            "steel":[35,2],
            "glass":[15,7],
            "ghee":[10,3],
            "aluminium":[23,1]
        }
        self.transacion_log = []

    @staticmethod
    def get_current_date_time():
        now = datetime.now()
        return now.strftime("%d-%m-%Y %H:%M %p")



    def add_stock(self,name,qty):
        name = name.casefold()
        if not name in self.product and qty > 0:
            print("Wrong product name")
            return
        self.product[name][1] += qty
        cost_price = qty * self.product[name][0]
        print(f"{name} has been added with new stock {self.product[name][1]}")
        self.transacion_log.append(f"{name} has been added with new stock {self.product[name][1]} at {cost_price} value {self.get_current_date_time()}")


    def remove_stock(self,name,qty):
        name = name.casefold()
        if not name in self.product:
           print("Wrong product name")
           return
        stock = self.product[name][1]
        if stock > qty:
            stock -= qty
            selling_price = qty * self.product[name][0]
            self.product[name][1] = stock
            print(f"{name} has been deduced with remaining stock {stock}")
            self.transacion_log.append(f"{name} has been sold with remaining stock {stock} at {selling_price}  value {self.get_current_date_time()}")
        else:
            print(f"Insufficient stock")


    def get_transaction_log(self):
        if not self.transacion_log:
            print("No logs present")
            return
        for index,log in enumerate(self.transacion_log,start=1):
            print(index,' : ',log)

    def inventory_report(self):
        print("\n------INVENTORY REPORT-------")
        total_value = 0
        for name,detail in self.product.items():
            stock = detail[1]
            if not stock > 1:
                print(f"LOW STOCK ALERT : {name} has stock {stock}")
            total_value += stock * detail[0]
            print(f"{name} has stock {stock} with value {detail[0]}")
        print("Total Inventory value : ",total_value)

    
    def demand_forecast(self):
        items_sold=items_purchased=0
        for log in self.transacion_log:
            if "sold".casefold() in log:
                items_sold += 1
            elif "added".casefold()in log:
                items_purchased += 1
        print(f"Items sold : {items_sold} and Purchased : {items_purchased}")

available_choices = ["Add product","Add stock","Remove stock","View report","Forecast demand"]
if __name__ == '__main__':
    wh = Warehouse()

    # wh.add_stock('oil',2)
    # wh.add_stock('ghee',3)
    # wh.remove_stock('ghee',3)
    # wh.get_current_date_time()
    # wh.get_transaction_log()
    # wh.inventory_report()
    # wh.demand_forecast()

    while True:
        for index,choice in enumerate(available_choices,start=1):
            print(index," : ",choice)
        print("0 : Exit")

        choice = input("Enter your choice [0-6] ")
        if choice == '0':
            print("Exit")
            break

        elif choice == '4':
            wh.get_transaction_log()

        elif choice == '5':
            wh.demand_forecast()


        
