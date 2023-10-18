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
wastage_prcnt=[0,0,0,0,0]
wastage_grams=[0,0,0,0,0]
gst_amount=[0,0,0,0,0]
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
    
def wastage_prc(prc):
    global wastage_prcnt
    wastage_prcnt[counter]=float(prc)
       
def cash_amount(cash):
    global paid_amount
    paid_amount=float(cash)
        
def pur_item():
    global counter
    counter+=1
    
def draw(canvas): 
    global counter,y_component,grand_total,total_amount,paid_amount
    #plain bill design
    #landline='Landline: 08545-231138'
    #canvas.draw_text(landline, [WIDTH-240,50], 20, "Black")
    cell='Mobile: +91-9393881515'
    canvas.draw_text(cell, [WIDTH-250,50], 18, "Black")
    #bank account details
    #bnk_details='Bank Account Details:'
    #canvas.draw_text(bnk_details, [WIDTH-250,70], 18, "Black")
    accnt_num='Account No: 622 415 833 82'
    canvas.draw_text(accnt_num, [WIDTH-250,90], 18, "Black")
    if_code='IFSC Code: sbin0020187'
    canvas.draw_text(if_code, [WIDTH-250,110], 18, "Black")
    brnch='Branch: Wanaparthy'
    canvas.draw_text(brnch, [WIDTH-250,130], 18, "Black")
    
    #gst number
    gst_num='GST No: 36ACEF1052Q1ZS'
    canvas.draw_text(gst_num, [WIDTH-250,170], 18, "Black")
    
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
    #canvas.draw_text('Estimation only', [WIDTH/2-60,200], 18, "Black")
    canvas.draw_text('Date: '+date, [WIDTH-170,230], 20, "Black")
    canvas.draw_text('Customer Details: '+c_details, [25,255], 20, "Black")
    
    
    
    canvas.draw_polygon([(10, 290), (WIDTH-30, 290), (WIDTH-30, 640),(10, 640)],1, 'Black')
    canvas.draw_polyline([(10, 330), (WIDTH-30, 330)], 1, 'Black')
    
    canvas.draw_text('Item Details', [62,315], 14, "Black")
    canvas.draw_polyline([(180, 290), (180, 640)], 1, 'Black')
    
    canvas.draw_text('Price/Ten grams', [192,315], 14, "Black")
    canvas.draw_polyline([(300, 290), (300, 640)], 1, 'Black')
    
    canvas.draw_text('Weight (grams)', [322,315], 14, "Black")
    canvas.draw_polyline([(420, 290), (420, 640)], 1, 'Black')
    
    canvas.draw_text('Wastage (grams)', [432,315], 14, "Black")
    canvas.draw_polyline([(540, 290), (540, 640)], 1, 'Black')
    
    canvas.draw_text('Making Charges', [552,315], 14, "Black")
    canvas.draw_polyline([(660, 290), (660, 640)], 1, 'Black')
    
    canvas.draw_text('GST (3%)', [682,315], 14, "Black")
    canvas.draw_polyline([(780, 290), (780, 640)], 1, 'Black')
    
    canvas.draw_text('Total Amount', [820,315], 14, "Black")
      
    canvas.draw_text('Chavalla Nagaraju', [30,715], 15, "Black")
    
    
    
    #billed item design
    a=counter+1
    for i in range(a):
        y_component=415-60+i*70
        #convert wastage as a percent of weight to gms
        wastage_grams[i]=(wastage_prcnt[i]/100.0)*weight_grams[i]
        
        canvas.draw_text(i_details[i], [15,y_component], 20, "Black")
        canvas.draw_text( str(price_ten_grams[i]), [192,y_component], 20, "Black")
        canvas.draw_text(str(weight_grams[i]), [322,y_component], 20, "Black")
        canvas.draw_text(str(wastage_grams[i]), [432,y_component], 20, "Black")
        canvas.draw_text(str(making_charges[i]), [552,y_component], 20, "Black")
        
        r=(price_ten_grams[i]*0.1)*weight_grams[i]
        w=(price_ten_grams[i]*0.1)*wastage_grams[i]
        
        
        if wastage_grams[i]>=0:
            
            gst_amount[i]=(r+w+making_charges[i])*0.03
            canvas.draw_text(str(gst_amount[i]), [682,y_component], 20, "Black")
            
            total_amount[i]=(r+w+making_charges[i]+gst_amount[i])
            canvas.draw_text(str(total_amount[i]), [810,y_component], 20, "Black")

        else:
            
            gst_amount[i]=0
            canvas.draw_text(str(gst_amount[i]), [682,y_component], 20, "Black")
            
            total_amount[i]=-1*(r+w+making_charges[i])
            canvas.draw_text(str(total_amount[i]), [810,y_component], 20, "Red")
        
        #calculating grandtotal
        grand_total=total_amount[0]+total_amount[1]+total_amount[2]+total_amount[3]+total_amount[4]
        canvas.draw_text('Grand Total: '+str(grand_total), [750,680], 20, "Black")
        #canvas.draw_text('Paid Amount: '+str(paid_amount), [625,740-60], 15, "Black")
        #balance=grand_total-paid_amount
        #canvas.draw_text('Balance '+str(balance), [625,755-60], 15, "Black")

        
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Bill", WIDTH, HEIGHT)
frame.set_canvas_background('White')
frame.add_input("Date", day_date, 100)
frame.add_input("Customer Details:", cust_details, 200)
frame.add_input("Item Details:", item_details, 200)
frame.add_input("Price/Ten grams", price_tengms, 100)
frame.add_input("Weight in grams", weight_gms, 100)
frame.add_input("Wastage: % of weight", wastage_prc, 100)
frame.add_input("Making Charges", labour_ch, 100)
#frame.add_input("Paid Amount", cash_amount, 100)
frame.add_button("Add item", pur_item)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
