inventory = [
    {"id": "G01", "name": "Gạo tẻ", "quantity": 50},
    {"id": "G02", "name": "Mì tôm", "quantity": 120}
]


def show_inventory(inventory_list):
    if len(inventory_list) == 0:
        print("Kho hàng hiện đang trống!")
        return

    print("\n" + "=" * 50)
    print(f"{'ID':<10}{'Tên hàng hóa':<25}{'Số lượng'}")
    print("=" * 50)

    for item in inventory_list:
        print(f"{item['id']:<10}{item['name']:<25}{item['quantity']}")

    print("=" * 50)


def add_item(inventory_list):
    while True:
        item_id = input("Nhập ID hàng hóa: ").strip()
        if item_id != "":
            break
        print("ID không được để trống!")

    while True:
        item_name = input("Nhập tên hàng hóa: ").strip()
        if item_name != "":
            break
        print("Tên hàng hóa không được để trống!")

    while True:
        try:
            quantity = int(input("Nhập số lượng: "))
            if quantity > 0:
                break
            print("Số lượng phải lớn hơn 0!")
        except:
            print("Vui lòng nhập số nguyên hợp lệ!")

    inventory_list.append({
        "id": item_id,
        "name": item_name,
        "quantity": quantity
    })

    print("Thêm hàng hóa vào kho thành công!")


def update_quantity(inventory_list):
    item_id = input("Nhập ID hàng hóa cần cập nhật: ").strip()

    for item in inventory_list:
        if item["id"] == item_id:
            while True:
                try:
                    new_quantity = int(input("Nhập số lượng mới: "))
                    if new_quantity > 0:
                        item["quantity"] = new_quantity
                        print("Cập nhật số lượng thành công!")
                        return
                    print("Số lượng phải lớn hơn 0!")
                except:
                    print("Vui lòng nhập số nguyên hợp lệ!")

    print(f"Không tìm thấy hàng hóa có mã {item_id}!")


while True:
    print("\n" + "=" * 50)
    print("       QUẢN LÝ KHO HÀNG - GROCERY STORE ")
    print("=" * 50)
    print("1. Xem danh sách hàng tồn kho")
    print("2. Nhập thêm hàng hóa mới")
    print("3. Cập nhật số lượng tồn kho")
    print("4. Thoát chương trình")
    print("=" * 50)

    choice = input("Nhập lựa chọn của bạn: ")

    match choice:
        case "1":
            show_inventory(inventory)
        case "2":
            add_item(inventory)
        case "3":
            update_quantity(inventory)
        case "4":
            print("Đã thoát chương trình!")
            break
        case _:
            print("Lựa chọn không hợp lệ!")