#simple bill generator app for calculating price of jewellery item
#http://www.codeskulptor.org/#user47_r55bhigAAe_18.py

import simplegui
import random

#intialising global variables
i_details=['','','','','','']
price_ten_grams=[0,0,0,0,0]
weight_grams=[0,0,0,0,0]
making_charges=[0,0,0,0,0]
wastage_grams=[0,0,0,0,0]
total_amount=[0,0,0,0,0]
y_component=415
date=''
c_details=''
counter=0
HEIGHT=800
WIDTH=800
calc_multiple=False
#event handlers for control panel
def day_date(today_date):
    global date
    date=today_date

def cust_details(details):
    global c_details
    c_details=details

def price_tengms(price):
    global price_ten_grams
    price_ten_grams[counter]=float(price)


def item_details(detail):
    global i_details
    i_details[counter]=detail

def weight_gms(weight):
    global weight_grams
    weight_grams[counter]=float(weight)

def labour_ch(rate):
    global making_charges
    making_charges[counter]=float(rate)


def wastage_gms(wt):
    global wastage_grams
    wastage_grams[counter]=float(wt)


def pur_item():
    global counter,y_component
    counter+=1

def ret_item():
    pass

# Handler to draw on canvas
def draw(canvas):
    global counter,y_component
    #plain bill design
    landline='Landline: 08545-231138'
    cell='Mobile: +91-9393881515'
    canvas.draw_text(landline, [WIDTH-170,50], 15, "Black")
    canvas.draw_text(cell, [WIDTH-170,70], 15, "Black")

    canvas.draw_polyline([(10, 230), (WIDTH-10, 230)], 1, 'Black')

    canvas.draw_text('Date: '+date, [WIDTH-170,250], 15, "Black")

    canvas.draw_text('Customer Details: '+c_details, [25,275], 15, "Black")

    canvas.draw_polygon([(10, 350), (WIDTH-10, 350), (WIDTH-10, 700),(10, 700)], 1, 'Black')
    canvas.draw_polyline([(10, 390), (WIDTH-10, 390)], 1, 'Black')
    canvas.draw_text('Item Details', [15,375], 15, "Black")
    canvas.draw_polyline([(100, 350), (100, 700)], 1, 'Black')
    canvas.draw_text('Price/Ten grams', [115,375], 15, "Black")
    canvas.draw_polyline([(220, 350), (220, 700)], 1, 'Black')
    canvas.draw_text('Weight (grams)', [235,375], 15, "Black")
    canvas.draw_polyline([(340, 350), (340, 700)], 1, 'Black')
    canvas.draw_text('Wastage (grams)', [355,375], 15, "Black")
    canvas.draw_polyline([(470, 350), (470, 700)], 1, 'Black')
    canvas.draw_text('Making Charges', [485,375], 15, "Black")
    canvas.draw_polyline([(600, 350), (600, 700)], 1, 'Black')
    canvas.draw_text('Total Amount', [645,375], 15, "Black")

    canvas.draw_text('Chavalla Nagaraju', [WIDTH-170,750], 15, "Black")

    #billed item design
    a=counter+1
    for i in range(a):
        y_component=415+i*70
        canvas.draw_text(i_details[i], [15,y_component], 15, "Black")
        canvas.draw_text( str(price_ten_grams[i]), [115,y_component], 15, "Black")
        canvas.draw_text(str(weight_grams[i]), [235,y_component], 15, "Black")
        canvas.draw_text(str(wastage_grams[i]), [355,y_component], 15, "Black")
        canvas.draw_text(str(making_charges[i]), [485,y_component], 15, "Black")
        r=(price_ten_grams[i]*0.1)*weight_grams[i]
        w=(price_ten_grams[i]*0.1)*wastage_grams[i]
        total_amount[i]=(r+w+making_charges[i])
        canvas.draw_text(str(total_amount[i]), [645,y_component], 15, "Black")


# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Bill", WIDTH, HEIGHT)
frame.set_canvas_background('White')
frame.add_input("Date", day_date, 100)
frame.add_input("Customer Details:", cust_details, 200)
frame.add_input("Price/Ten grams", price_tengms, 100)
frame.add_input("Item Details:", item_details, 200)
frame.add_input("Weight in grams", weight_gms, 100)
frame.add_input("Wastage in grams", wastage_gms, 100)
frame.add_input("Making Charges", labour_ch, 100)
frame.add_button("Add Purchase item", pur_item)
frame.add_button("Add Return item", ret_item)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
