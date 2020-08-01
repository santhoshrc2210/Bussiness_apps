#simple bill generator app for calculating price of jewellery item
#https://www.dropbox.com/s/ze58mms20xkk2ke/bill_header.jpg?dl=0
#http://www.codeskulptor.org/#user47_r55bhigAAe_23.py
import simplegui
import random

#intialising global variables
dropbox_url='https://www.dropbox.com/s/ze58mms20xkk2ke/bill_header.jpg?raw=1'
image = simplegui.load_image(dropbox_url)
i_details=['','','','','','']
price_ten_grams=[0,0,0,0,0]
weight_grams=[0,0,0,0,0]
making_charges=[0,0,0,0,0]
wastage_grams=[0,0,0,0,0]
total_amount=[0,0,0,0,0]
grand_total=0
y_component=415
date=''
c_details=''
counter=0
HEIGHT=800
WIDTH=900
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
    global counter
    counter+=1

def ret_item():
    global counter
    counter+=1

for t in total_amount:
        grand_total+=t
# Handler to draw on canvas
def draw(canvas):
    global counter,y_component,grand_total,total_amount
    #plain bill design
    landline='Landline: 08545-231138'
    cell='Mobile: +91-9393881515'
    canvas.draw_text(landline, [WIDTH-170,50], 15, "Black")
    canvas.draw_text(cell, [WIDTH-170,70], 15, "Black")

    canvas.draw_text('Kurnool Subbaiah', [(WIDTH/2)-150,70], 30, "Blue")
    canvas.draw_text('Santhosh Jewellers', [(WIDTH/2)-120,90], 20, "Red")
    canvas.draw_text('Shankar Gunj,Wanaparthy-509103', [(WIDTH/2)-140,110], 15, "Black")
    canvas.draw_text('Jai Santhoshi Ma!', [40,50], 15, "Black")



    #drawing header
    #center_source = (1057 / 2, 2470 / 2)
    #width_height_source = (1057, 2470)
    #center_dest = (450, 115)
    #width_height_dest = (900, 230)
    #rotation = 1.5*3.14
    #canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest, rotation)

    canvas.draw_polyline([(10, 200), (WIDTH-10, 200)], 1, 'Black')
    canvas.draw_text('Estimation only', [25,220], 15, "Black")


    canvas.draw_text('Date: '+date, [WIDTH-170,250], 15, "Black")

    canvas.draw_text('Customer Details: '+c_details, [25,275], 15, "Black")

    canvas.draw_polygon([(10, 350), (WIDTH-10, 350), (WIDTH-10, 700),(10, 700)], 1, 'Black')
    canvas.draw_polyline([(10, 390), (WIDTH-10, 390)], 1, 'Black')

    canvas.draw_text('Item Details', [65,375], 15, "Black")
    canvas.draw_polyline([(200, 350), (200, 700)], 1, 'Black')

    canvas.draw_text('Price/Ten grams', [215,375], 15, "Black")
    canvas.draw_polyline([(320, 350), (320, 700)], 1, 'Black')

    canvas.draw_text('Weight (grams)', [335,375], 15, "Black")
    canvas.draw_polyline([(440, 350), (440, 700)], 1, 'Black')

    canvas.draw_text('Wastage (grams)', [455,375], 15, "Black")
    canvas.draw_polyline([(570, 350), (570, 700)], 1, 'Black')

    canvas.draw_text('Making Charges', [585,375], 15, "Black")
    canvas.draw_polyline([(700, 350), (700, 700)], 1, 'Black')

    canvas.draw_text('Total Amount', [745,375], 15, "Black")

    canvas.draw_text('Chavalla Nagaraju', [30,775], 15, "Black")

    #billed item design
    a=counter+1
    for i in range(a):
        y_component=415+i*70
        canvas.draw_text(i_details[i], [15,y_component], 15, "Black")
        canvas.draw_text( str(price_ten_grams[i]), [215,y_component], 15, "Black")
        canvas.draw_text(str(weight_grams[i]), [335,y_component], 15, "Black")
        canvas.draw_text(str(wastage_grams[i]), [455,y_component], 15, "Black")
        canvas.draw_text(str(making_charges[i]), [585,y_component], 15, "Black")
        r=(price_ten_grams[i]*0.1)*weight_grams[i]
        w=(price_ten_grams[i]*0.1)*wastage_grams[i]
        if wastage_grams[i]>=0:
            total_amount[i]=(r+w+making_charges[i])
            canvas.draw_text(str(total_amount[i]), [745,y_component], 15, "Black")

        else:
            total_amount[i]=-1*(r+w+making_charges[i])
            canvas.draw_text(str(total_amount[i]), [745,y_component], 15, "Red")
        #calculating grandtotal
        grand_total=total_amount[0]+total_amount[1]+total_amount[2]+total_amount[3]+total_amount[4]
        canvas.draw_text('Grand Total: '+str(grand_total), [625,725], 15, "Black")


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
frame.add_button("Add item", pur_item)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
