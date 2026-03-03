import json
import os
import time

class InventoryManager:
    # 加载文件，这就静态方法吗？无上下文但和这个类强逻辑相关
    @staticmethod
    def load_content():
        if not os.path.exists("Book_Inventory.json"):
            return []
        try:
            with open("Book_Inventory.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            # 防止文件json格式出错，文件损坏等故障
            return []

    # 检测图书是否重复
    def is_book_exist(self,isbn):
        data = self.load_content()
        for item in data:
            if item["Book"]["ISBN"] == isbn:
                print("找到相同编号的图书,请确认编号输入无误和功能选择无误")
                return item
        return None

    # 保存数据
    @staticmethod
    def save_data(data):
        os.makedirs("Book_Inventory.json", exist_ok=True)
        with open("Book_Inventory.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    # 增加库存模块思路；调用load_content函数打开文件，让用户输入信息，调用stock_in()。在stock_in()中调用is_book_exist函数后添加
    # 上面是旧的想法，现在看应该是先处理好数据并打包好再打开文件保存数据
    # 录入图书信息
    def add_book(self):
        while True:
            isbn = input("请输入图书的编号(输入0回退):")
            if isbn == "0":
                break
            elif self.is_book_exist(isbn):
                print("此编号已录入系统，请确认输入无误")
                time.sleep(2)
                os.system("cls||clear") # 兼顾多个平台
                continue
            name = input("请输入书名:")
            author = input("请输入本书作者:")
            while True:
                quantity = input("请输入新增的该图书库存(没有请写0)")
                # 输入进去的是字符串，要转换为数字最后进入到json文件中
                try:
                    quantity = int(quantity)
                    if quantity >= 0:
                        break
                    else:
                        print("数字小于0，自动回退至上一步")
                        time.sleep(2)
                        os.system("cls||clear")
                except ValueError:
                    print("请输入数字，自动回退至上一步")
                    time.sleep(2)
                    os.system("cls||clear")
            location = input("请输入该库存位置(没有请写U)")
            data = {"Book": {"ISBN": isbn,"name": name,"author": author},"Inventory": {"quantity": quantity,"location": location}}
            self.save_data(data)
            break

    # 增加库存
    def stock_in(self):
        while True:
            isbn = input("请输入图书的编号(输入0回退):")
            data = self.load_content()
            inventory_item = None
            for item in data:
                if item["Book"]["ISBN"] == isbn:
                    inventory_item = item
            if isbn == "0":
                break
            elif inventory_item:
                # 有编号，后面部分代码从add_book那边改编过来
                while True:
                    quantity = input("请输入新增的该图书库存")
                    # 输入进去的是字符串，要转换为数字最后进入到json文件中
                    try:
                        quantity = int(quantity)
                        if quantity > 0:
                            break
                        else:
                            print("数字小于等于0，请选择“释放库存”\n自动回退至上一步")
                            time.sleep(2)
                            os.system("cls||clear")
                    except ValueError:
                        print("请输入数字，自动回退至上一步")
                        time.sleep(2)
                        os.system("cls||clear")
                while True:
                    location = input("请输入该库存位置")
                    if location in ["U", " ", "\t", "\n", ""]:
                        # 本来是想用and列举空字符串的，但是ai有更好的方法
                        print("库存地址不可为空，请重新输入地址")
                        time.sleep(2)
                        os.system("cls||clear")
                    else:
                        break

                # json原则上不能取小段的进行替换，所以要重写逻辑去替换文件
                for item in inventory_item["Inventory"]:
                    # 是没有库存的图书
                    if item["location"] == "U":
                        item["quantity"] = quantity
                        item["location"] = location
                        with open("Book_Inventory.json", "w", encoding="utf-8") as f:
                            json.dump(data, f, ensure_ascii=False, indent=4)
                        return
                # 看看到底是有已存的还是未存
                target_item = None
                for item in inventory_item["Inventory"]:
                    if item["location"] == location:
                        target_item = item
                        break
                # 是增加已存位置的信息
                if target_item:
                    target_item["quantity"] += quantity
                    with open("Book_Inventory.json", "w", encoding="utf-8") as f:
                        json.dump(data, f, ensure_ascii=False, indent=4)
                    break
                # 是增加未存位置的信息
                else:
                    plus = {"quantity": quantity, "location": location}
                    inventory_item.append(plus)
                    with open("Book_Inventory.json", "w", encoding="utf-8") as f:
                        json.dump(data, f, ensure_ascii=False, indent=4)
                    break
            else:
                # 编号未录入系统
                print("此编号未录入系统，请核对输入正确与否，5s后自动回退")
                time.sleep(5)
                os.system("cls||clear")

    # 减少库存
    def stock_out(self):
        # 代码从stock_in那边改编过来
        while True:
            isbn = input("请输入图书的编号(输入0回退):")
            data = self.load_content()
            inventory_item = None
            for item in data:
                if item["Book"]["ISBN"] == isbn and item["Inventory"][0]["quantity"] > 0:
                    inventory_item = item
            if isbn == "0":
                break
            elif inventory_item:
                # 有编号
                while True:
                    quantity = input("请输入释放的该图书库存")
                    # 输入进去的是字符串，要转换为数字最后进入到json文件中
                    try:
                        quantity = int(quantity)
                        if quantity > 0:
                            break
                        else:
                            print("数字小于等于0，请选择“增加库存”\n自动回退至上一步")
                            time.sleep(2)
                            os.system("cls||clear")
                    except ValueError:
                        print("请输入数字，自动回退至上一步")
                        time.sleep(2)
                        os.system("cls||clear")
                while True:
                    location = input("请输入该库存位置")
                    if location in ["U", " ", "\t", "\n", ""]:
                        # 本来是想用and列举空字符串的，但是ai有更好的方法
                        print("库存地址不可为空，请重新输入地址")
                        time.sleep(2)
                        os.system("cls||clear")
                    else:
                        break

                while True:
                    # 看看到底是有已存的还是未存
                    target_item = None
                    for item in inventory_item["Inventory"]:
                        if item["location"] == location:
                            target_item = item
                            break
                    # 是增加已存位置的信息
                    if target_item:
                        target_item["quantity"] -= quantity
                        if target_item["quantity"] < 0:
                            print("释放的库存超过仓库本身的库存，请重新安排\n5s后自动退回")
                            time.sleep(5)
                            os.system("cls||clear")
                        else:
                            with open("Book_Inventory.json", "w", encoding="utf-8") as f:
                                json.dump(data, f, ensure_ascii=False, indent=4)
                            break
                    # 是增加未存位置的信息
                    else:
                        print("未找到该仓库，请确认信息输入正确，将自动退回")
                        time.sleep(2)
                        os.system("cls||clear")
            else:
                # 编号未录入系统
                print("此编号未录入系统或当前库存为0，请核对输入正确与否，5s后自动回退")
                time.sleep(5)
                os.system("cls||clear")