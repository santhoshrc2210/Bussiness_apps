
#https://py2.codeskulptor.org/#user48_erwq0cY3bw_5.py
#simple bill generator app for calculating price of jewellery item
import simplegui
import random

#intialising global variables
dropbox_url='https://www.dropbox.com/s/p5lcba61cbxvejm/santhoshi_mata.png?raw=1'
image = simplegui.load_image(dropbox_url)
i_details=['','','','','','']
price_ten_grams=[0,0,0,0,0]
weight_grams=[0,0,0,0,0]
making_charges=[0,0,0,0,0]
wastage_grams=[0,0,0,0,0]
total_amount=[0,0,0,0,0]
grand_total=0
paid_amount=0
y_component=355
date=''
c_details=''
counter=0
HEIGHT=800
WIDTH=1000
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
       
def cash_amount(cash):
    global paid_amount
    paid_amount=float(cash)
        
def pur_item():
    global counter
    counter+=1
    
def draw(canvas): 
    global counter,y_component,grand_total,total_amount,paid_amount
    #plain bill design
    landline='Landline: 08545-231138'
    cell='Mobile: +91-9393881515'
    canvas.draw_text(landline, [WIDTH-240,50], 20, "Black")
    canvas.draw_text(cell, [WIDTH-240,70], 20, "Black")
    
    center_source = (204 / 2, 282 / 2) 
    width_height_source = (204, 282)
    center_dest = (60,75)
    width_height_dest = (100, 150)
    rotation = 0
    canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest, rotation)

    
    canvas.draw_text('Kurnool Subbaiah', [(WIDTH/2)-160,65], 40, "Blue")
    canvas.draw_text('Santhosh Jewellers', [(WIDTH/2)-130,90], 30, "Red")
    canvas.draw_text('Shankar Gunj,Wanaparthy-509103', [(WIDTH/2)-140,110], 20, "Black")
    canvas.draw_text('Jai Santhoshi Ma!', [10,170], 20, "black")


    canvas.draw_polyline([(10, 180), (WIDTH-10, 180)], 1, 'Black')
    canvas.draw_text('Estimation only', [WIDTH/2-60,200], 18, "Black")


    canvas.draw_text('Date: '+date, [WIDTH-170,230], 20, "Black")
    
    canvas.draw_text('Customer Details: '+c_details, [25,255], 20, "Black")
    
    canvas.draw_polygon([(10, 290), (WIDTH-30, 290), (WIDTH-30, 640),(10, 640)],1, 'Black')
    canvas.draw_polyline([(10, 330), (WIDTH-30, 330)], 1, 'Black')
    
    canvas.draw_text('Item Details', [65,315], 20, "Black")
    canvas.draw_polyline([(200, 290), (200, 640)], 1, 'Black')
    
    canvas.draw_text('Price/Ten grams', [215,315], 20, "Black")
    canvas.draw_polyline([(350, 290), (350, 640)], 1, 'Black')
    
    canvas.draw_text('Weight (grams)', [360,315], 20, "Black")
    canvas.draw_polyline([(500, 290), (500, 640)], 1, 'Black')
    
    canvas.draw_text('Wastage (grams)', [510,315], 20, "Black")
    canvas.draw_polyline([(650, 290), (650, 640)], 1, 'Black')
    
    canvas.draw_text('Making Charges', [660,315], 20, "Black")
    canvas.draw_polyline([(800, 290), (800, 640)], 1, 'Black')
    
    canvas.draw_text('Total Amount', [810,315], 20, "Black")
      
    canvas.draw_text('Chavalla Nagaraju', [30,715], 20, "Black")
    
    #billed item design
    a=counter+1
    for i in range(a):
        y_component=415-60+i*70
        canvas.draw_text(i_details[i], [15,y_component], 20, "Black")
        canvas.draw_text( str(price_ten_grams[i]), [215,y_component], 20, "Black")
        canvas.draw_text(str(weight_grams[i]), [360,y_component], 20, "Black")
        canvas.draw_text(str(wastage_grams[i]), [510,y_component], 20, "Black")
        canvas.draw_text(str(making_charges[i]), [660,y_component], 20, "Black")
        r=(price_ten_grams[i]*0.1)*weight_grams[i]
        w=(price_ten_grams[i]*0.1)*wastage_grams[i]
        if wastage_grams[i]>=0:
            total_amount[i]=(r+w+making_charges[i])
            canvas.draw_text(str(total_amount[i]), [810,y_component], 20, "Black")

        else:
            total_amount[i]=-1*(r+w+making_charges[i])
            canvas.draw_text(str(total_amount[i]), [810,y_component], 20, "Red")
        #calculating grandtotal
        grand_total=total_amount[0]+total_amount[1]+total_amount[2]+total_amount[3]+total_amount[4]
        canvas.draw_text('Grand Total: '+str(grand_total), [625,665], 20, "Black")
        #canvas.draw_text('Paid Amount: '+str(paid_amount), [625,740-60], 15, "Black")
        #balance=grand_total-paid_amount
        #canvas.draw_text('Balance '+str(balance), [625,755-60], 15, "Black")

        
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
#frame.add_input("Paid Amount", cash_amount, 100)
frame.add_button("Add item", pur_item)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
