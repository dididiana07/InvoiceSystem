from tkinter import *
import random
import datetime

background = "bisque1"
technical_background = "azure2"
black_color = "black"

# window initialization
window = Tk()
window.title("Invoice system")
window.resizable(False, False)
# window.geometry("1020x630+0+0")
window.config(background=background)

# create panels
top_panel = Frame(window)
top_panel.pack(side=TOP)

invoice_title = Label(top_panel, font=("Dosis", 50, "bold"), text="Invoice System",
                      bd=1, background=background, fg=black_color)
invoice_title.grid(row=0, column=0)

# left panel
left_panel = Frame(window)
left_panel.pack(side=LEFT)

# menus panel
menus_panel = Frame(left_panel)
menus_panel.grid(row=0, column=0)

food_panel = LabelFrame(menus_panel, font=("Dosis", 10, "bold"), bd=1, text="Food")
food_panel.grid(row=0, column=0)

drink_panel = LabelFrame(menus_panel, font=("Dosis", 10, "bold"), bd=1, text="Drink")
drink_panel.grid(row=0, column=1)

dessert_panel = LabelFrame(menus_panel, font=("Dosis", 10, "bold"), bd=1, text="Dessert")
dessert_panel.grid(row=0, column=2)

cost_panel = Frame(menus_panel)
cost_panel.grid(row=1, column=0)
# right panel
right_panel = Frame(window)
right_panel.pack(side=RIGHT)

calculation_entry_panel = Frame(right_panel)
calculation_entry_panel.grid(row=0, column=0)

calculator_panel = Frame(right_panel)
calculator_panel.grid(row=1, column=0)

printed_check_panel = Frame(right_panel)
printed_check_panel.grid(row=2, column=0)

buttons_panel = Frame(right_panel)
buttons_panel.grid(row=3, column=0)

# lists of foods, drinks and desserts
foods = ["chicken", "pizza ham", "pizza vegan", "cheese hamburger", "double hamburger", "tuna salad", "fish & chips"]
drinks = ["water", "juice", "cola", "apple juice", "cacao", "beer", "wine"]
desserts = ["chocolate pudding", "ice cream", "yogurt", "fruits", "cake", "apple pie", "banana triple ice cream"]

food_price = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
drink_price = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
dessert_price = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


# function to check all the checkbutton

def review_all():
    index = 0
    for b in food_boxes:
        if food_variables[index].get() == 1:
            food_boxes[index].config(state=NORMAL)
        else:
            food_boxes[index].delete(0, END)
            food_boxes[index].insert(0, "0")
            food_boxes[index].config(state=DISABLED)
        index += 1

    index = 0
    for b in drink_boxes:
        if drink_variables[index].get() == 1:
            drink_boxes[index].config(state=NORMAL)
        else:
            drink_boxes[index].delete(0, END)
            drink_boxes[index].insert(0, "0")
            drink_boxes[index].config(state=DISABLED)
        index += 1

    index = 0
    for b in dessert_boxes:
        if dessert_variables[index].get() == 1:
            dessert_boxes[index].config(state=NORMAL)
        else:
            dessert_boxes[index].delete(0, END)
            dessert_boxes[index].insert(0, "0")
            dessert_boxes[index].config(state=DISABLED)
        index += 1


# create checkbutton, boxes, and text

food_variables = []
food_boxes = []
food_text = []
row = 0
for food in foods:
    # checkbutton
    food_variables.append("")
    food_variables[row] = IntVar()
    food = Checkbutton(food_panel,
                       text=food.title(),
                       bd=1,
                       font=("Dosis", 14, "bold"),
                       variable=food_variables[row],
                       onvalue=1,
                       offvalue=0,
                       command=review_all)
    food.grid(row=row,
              column=0,
              sticky=W)

    # entries
    food_boxes.append("")
    food_text.append("")
    food_text[row] = StringVar()
    food_text[row].set("0")
    food_boxes[row] = Entry(food_panel,
                            textvariable=food_text[row],
                            font=("Dosis", 14, "bold"),
                            state=DISABLED,
                            width=3)
    food_boxes[row].grid(row=row,
                         column=1,
                         sticky=W)
    row += 1

drink_variables = []
drink_boxes = []
drink_text = []
row = 0
for drink in drinks:
    # checkbutton
    drink_variables.append("")
    drink_variables[row] = IntVar()
    drink = Checkbutton(drink_panel,
                        text=drink.title(),
                        bd=1,
                        font=("Dosis", 14, "bold"),
                        variable=drink_variables[row],
                        onvalue=1,
                        offvalue=0,
                        command=review_all)
    drink.grid(row=row,
               column=0,
               sticky=W)

    # entries
    drink_boxes.append("")
    drink_text.append("")
    drink_text[row] = StringVar()
    drink_text[row].set("0")
    drink_boxes[row] = Entry(drink_panel,
                             textvariable=drink_text[row],
                             font=("Dosis", 14, "bold"),
                             state=DISABLED,
                             width=3)
    drink_boxes[row].grid(row=row,
                          column=1,
                          sticky=W)
    row += 1

dessert_variables = []
dessert_boxes = []
dessert_text = []
row = 0
for dessert in desserts:
    # checkbutton
    dessert_variables.append("")
    dessert_variables[row] = IntVar()
    dessert = Checkbutton(dessert_panel,
                          text=dessert.title(),
                          bd=1,
                          font=("Dosis", 14, "bold"),
                          variable=dessert_variables[row],
                          onvalue=1,
                          offvalue=0,
                          command=review_all)
    dessert.grid(row=row,
                 column=0,
                 sticky=W)

    # entries
    dessert_boxes.append("")
    dessert_text.append("")
    dessert_text[row] = StringVar()
    dessert_text[row].set("0")
    dessert_boxes[row] = Entry(dessert_panel,
                               textvariable=dessert_text[row],
                               font=("Dosis", 14, "bold"),
                               state=DISABLED,
                               width=3)
    dessert_boxes[row].grid(row=row,
                            column=1,
                            sticky=W)
    row += 1


food_cost_label = Label(cost_panel, text="Food Cost")
food_cost_label.grid(row=0, column=0, sticky=W)

food_cost_entry = Entry(cost_panel, width=6)
food_cost_entry.grid(row=0, column=1, sticky=W)

drink_cost_label = Label(cost_panel, text="Drink Cost")
drink_cost_label.grid(row=1, column=0)

drink_cost_entry = Entry(cost_panel, width=6)
drink_cost_entry.grid(row=1, column=1, sticky=W)

dessert_cost_label = Label(cost_panel, text="Dessert Cost")
dessert_cost_label.grid(row=2, column=0)

dessert_cost_entry = Entry(cost_panel, width=6)
dessert_cost_entry.grid(row=2, column=1)

subtotal_label = Label(cost_panel, text="Subtotal")
subtotal_label.grid(row=0, column=2)

subtotal_entry = Entry(cost_panel, width=6)
subtotal_entry.grid(row=0, column=3)

taxes_label = Label(cost_panel, text="Taxes")
taxes_label.grid(row=1, column=2)

taxes_entry = Entry(cost_panel, width=6)
taxes_entry.grid(row=1, column=3)

total_label = Label(cost_panel, text="Subtotal")
total_label.grid(row=2, column=2)

total_entry = Entry(cost_panel, width=6)
total_entry.grid(row=2, column=3)


ordered = []
total = ""
subtotal = ""
taxes = ""


def get_total():
    global total, subtotal, taxes, ordered
    total_food = 0
    for i in range(len(foods)):
        if food_boxes[i].get() != "0":
            new_enter = {"item": foods[i],
                         "price": food_price[i],
                         "quantity": food_boxes[i].get()}
            ordered.append(new_enter)
            price = food_price[i] * int(food_boxes[i].get())
            total_food += price

    total_drink = 0
    for i in range(len(drinks)):
        if drink_boxes[i].get() != "0":
            new_enter = {"item": drinks[i],
                         "price": drink_price[i],
                         "quantity": drink_boxes[i].get()}
            ordered.append(new_enter)
            price = drink_price[i] * int(drink_boxes[i].get())
            total_drink += price

    total_dessert = 0
    for i in range(len(desserts)):
        if dessert_boxes[i].get() != "0":
            new_enter = {"item": desserts[i],
                         "price": dessert_price[i],
                         "quantity": dessert_boxes[i].get()}
            ordered.append(new_enter)
            price = dessert_price[i] * int(dessert_boxes[i].get())
            total_dessert += price

    subtotal = round(total_food + total_drink + total_dessert, 2)
    taxes = round(subtotal * 0.11, 2)
    total = round(subtotal + taxes, 2)

    food_cost_entry.delete(0, END)
    drink_cost_entry.delete(0, END)
    dessert_cost_entry.delete(0, END)
    subtotal_entry.delete(0, END)
    taxes_entry.delete(0, END)
    total_entry.delete(0, END)

    food_cost_entry.insert(0, f"${round(total_food, 2)}")
    drink_cost_entry.insert(0, f"${round(total_drink, 2)}")
    dessert_cost_entry.insert(0, f"${round(total_dessert, 2)}")
    subtotal_entry.insert(0, f"${subtotal}")
    taxes_entry.insert(0, f"${taxes}")
    total_entry.insert(0, f"${total}")


calculator_entry = Entry(calculation_entry_panel, font=("Dosis", 14, "bold"), width=30)
calculator_entry.grid(row=0, column=0)

calculator_buttons = ["7", "8", "9", "+",
                      "4", "5", "6", "-",
                      "1", "2", "3", "*",
                      "CE", "Delete", "0", "/"]

calculator_buttons_lst = []

row = 1
column = 0
for button in calculator_buttons:
    button = Button(calculator_panel, text=button.title())
    button.grid(row=row, column=column)
    calculator_buttons_lst.append(button)
    column += 1
    if column > 3:
        row += 1
    if column == 4:
        column = 0


# add commands to the calculator buttons

def click_button(value):
    text = ""
    text += value
    calculator_entry.insert(END, text)


# function that calculates the total of the calculator entry

def calculate():
    try:
        result = eval(calculator_entry.get())
        calculator_entry.delete(0, END)
        calculator_entry.insert(0, result)
        calculator_entry.config(state=DISABLED)
    except SyntaxError:
        pass


def delete_calculation():
    calculator_entry.config(state=NORMAL)
    calculator_entry.delete(0, END)


calculator_buttons_lst[0].config(command=lambda: click_button("7"))
calculator_buttons_lst[1].config(command=lambda: click_button("8"))
calculator_buttons_lst[2].config(command=lambda: click_button("9"))
calculator_buttons_lst[3].config(command=lambda: click_button("+"))
calculator_buttons_lst[4].config(command=lambda: click_button("4"))
calculator_buttons_lst[5].config(command=lambda: click_button("5"))
calculator_buttons_lst[6].config(command=lambda: click_button("6"))
calculator_buttons_lst[7].config(command=lambda: click_button("-"))
calculator_buttons_lst[8].config(command=lambda: click_button("1"))
calculator_buttons_lst[9].config(command=lambda: click_button("2"))
calculator_buttons_lst[10].config(command=lambda: click_button("3"))
calculator_buttons_lst[11].config(command=lambda: click_button("*"))
calculator_buttons_lst[12].config(command=calculate)
calculator_buttons_lst[13].config(command=delete_calculation)
calculator_buttons_lst[14].config(command=lambda: click_button("/"))

printed_check_entry = Text(printed_check_panel, width=40, height=7, bd=1, background="white",
                           fg="black", font=("Dosis", 14))
printed_check_entry.grid(row=0, column=0)


def invoice():
    global ordered, total, taxes, subtotal
    printed_check_entry.delete("1.0", END)
    text = f"{'*' * 55}\n" \
           f"Welcome to Celeste's Kitchen\t\t\t{datetime.datetime.today().date()}" \
           f"\nOrder Nª{random.randint(0, 9999)}\n" \
           f"{'*' * 55}\n" \
           f"Item\t\tQuantity\t\tPrice" \
           f"\n{'-' * 55}"
    for i in range(len(ordered)):
        new_line = f"\n{ordered[i]['item'].title()}\t\t{ordered[i]['quantity']}\t\t${ordered[i]['price']}"
        text += new_line
    text = text + f"\n{'-' * 55}" + f"\nTAXES:\t${taxes}\nSUBTOTAL:\t${subtotal}\nTOTAL:\t${total}"
    printed_check_entry.insert(INSERT, text)


def save_invoice():
    text = printed_check_entry.get("1.0", "end-1c")
    with open("receipt.txt", "w") as file_open:
        file_open.write(text)


def reset_invoice():
    global ordered, total, taxes, subtotal
    total = ""
    taxes = ""
    subtotal = ""
    ordered = []
    printed_check_entry.delete("1.0", END)
    for var in food_variables:
        var.set(0)
    for var in drink_variables:
        var.set(0)
    for var in dessert_variables:
        var.set(0)

    for b in food_boxes:
        b.delete(0, END)
        b.insert(0, "0")
        b.config(state=DISABLED)

    for b in drink_boxes:
        b.delete(0, END)
        b.insert(0, "0")
        b.config(state=DISABLED)

    for b in dessert_boxes:
        b.delete(0, END)
        b.insert(0, "0")
        b.config(state=DISABLED)

    calculator_entry.delete(0, END)
    food_cost_entry.delete(0, END)
    drink_cost_entry.delete(0, END)
    dessert_cost_entry.delete(0, END)
    subtotal_entry.delete(0, END)
    taxes_entry.delete(0, END)
    total_entry.delete(0, END)


control_buttons = ["total", "invoice", "save", "reset"]
control_buttons_buttons = []

column = 0

for button in control_buttons:
    button = Button(buttons_panel, text=button.title())
    button.grid(row=0, column=column)
    control_buttons_buttons.append(button)
    column += 1

control_buttons_buttons[0].config(command=get_total)
control_buttons_buttons[1].config(command=invoice)
control_buttons_buttons[2].config(command=save_invoice)
control_buttons_buttons[3].config(command=reset_invoice)

window.mainloop()
