"""
Good day Prof! Here is our output. Since there are 8 classes,
me and my partner divided it into two in accordance with what
we did in Assignment 1. Thanks!
"""

# The succeeding lines are Mekyla Abad's contribution to this assignment.
# This is the code for Class 1: Volleyball Ball
class Volleyball_Ball:
# Attributes of the Volleyball Ball class
	def __init__(self, b, c, co, w, t):
		self.brand = b
		self.circumference = c
		self.color = co
		self.weight = w
		self.type = t
		
# Methods of the Volleyball Ball class
	def identify_brand(self):
		self.brand = self.brand
		
	def measure(self):
		self.measure = self.measure
		
	def distinguish_color(self):
		self.color = self.color
		
	def weigh(self):
		self.weigh = self.weigh
		
	def determine_type(self):
		self.type = self.type

#Created an object named 'vball'		
vball = Volleyball_Ball("Mikasa", 65, "white", 270, "indoor")

"""
After running the code, it will show the brand, circumference,
color, weight, and type of the Volleyball Ball. No change or 
increase is needed since we are only describing the ball itself.
"""

print (vball.brand)
print (vball.circumference)
print (vball.color)
print (vball.weight)
print (vball.type)

# This is the code for Class 2: Cellphone
class Cellphone:
# Attributes of the Cellphone class
	def __init__(self, on, o, l, b, u):
		self.on = on
		self.off = o
		self.locked = l
		self.battery = b
		self.unit = u
	
# Methods of the Cellphone class	
	def turn_on(self):
		self.on = self.on
	
	def turn_off(self):
		self.off = self.off
		
	def typepassword_locked(self):
		self.locked = self.locked
		
	def charge_battery(self):
		self.battery = self.battery
		
	def identify_unit(self):
		self.unit = self.unit
	
#Created an object named 'cp'	
cp = Cellphone("on", "off", "love", "low battery", "Samsung A50s")

"""
The attributes shows the class' status and what type it is
while the methods show what to do to achieve the attributes.
"""

print (cp.on)
print (cp.off)
print (cp.locked)
print (cp.battery)
print (cp.unit)

# This is the code for Class 3: Television
class Television:
# Attributes of the Television class
	def __init__(self, v, c, i, p, m):
		self.volume = v
		self.channel = c
		self.input = i
		self.power = p
		self.menu = m
	
# Methods of the Television class
	def increase_volume(self):
	 self.volume = self.volume + 7
 
	def change_channel(self):
		self.channel = self.channel + 3
		
	def choose_input(self):
		self.input = self.input
	
	def on_power(self):
	 self.power = self.power
	 
	def brightnessfix_menu(self):
		self.menu = self.menu -5
	
#Created an object named 'tv'	
tv = Television(31, 2, "HDMI", "on", 25)

"""
For this class, this is where we can do some modifications
because the methods use verbs such as increase, change, and 
fix. It is applicable since the example we have is a
television that requires operation.
"""

print ("Before increase volume:", tv.volume)
tv.increase_volume()
print ("After increase volume:", tv.volume)

print ("Before change channel:", tv.channel)
tv.change_channel()
print ("After change channel:", tv.channel)

print (tv.input)
print (tv.power)

print ("Before brightnessfix_menu:", tv.menu)
tv.brightnessfix_menu()
print ("After brightnessfix_menu:", tv.menu)

# This is the code for Class 4: Shirt
class Shirt:
# Attributes of the Shirt class
	def __init__(self, s, c, b, d, p):
		self.size = s
		self.color = c
		self.brand = b
		self.design = d
		self.price = p
	
# MEthods of the Shirt class
	def determine_size(self):
		self.size = self.size
		
	def recognize_color(self):
	 self.color = self.color
		
	def identify_brand(self):
		self.brand = self.brand
		
	def know_design(self):
		self.design = self.design
		
	def check_price(self):
		self.price = self.price +249

#Created an object named 'sh'	
sh = Shirt("small", "purple", "Adidas", "floral", 750)

"""
The first four attributes describe the look of the shirt.
On the other hand, the last attribute refers to its price.
There is an additional 249 pesos because upon checking in
the physical store, the buyer discovers it is more expensive
than the one being sold online.
"""

print (sh.size)
print (sh.color)
print (sh.brand)
print (sh.design)

print ("Before check price:", sh.price)
sh.check_price()
print ("After check price:", sh.price)

"""
Hello Prof!
Doing this activity is really hard and overwhelming
for me (since I'm only a beginner). It may seem very 
very simple, but I did it on my own and I did my best 
to accomplish it. Hope you appreciate my work.
-Mekyla Patrice G. Abad
"""

# The succeeding lines are Misaki Acosta's contribution to this assignment.
# This is the code for Class 5: K-Pop Album
class KPopAlbum:
# Attributes of K-Pop Album Class
    def __init__(self, v, p, pc, pb, c):
        self.version = v
        self.poster = p
        self.photocard = pc 
        self.photobook = pb 
        self.cd = c 

# Methods for K-Pop Album Class
    def identify_variation(self):
        self.version = self.version
    
    def unroll_poster(self):
        self.poster = self.poster
    
    def draw_random_photocard(self):
        self.photocard = self.photocard
        
    def browse_photobook(self):
        self.photobook = self.photobook
        
    def play_cd(self):
        self.cd = self.cd 

# Created Different K-Pop Album Variations
albumone = KPopAlbum("artbook","flat displaying a group photo", "Andy Park", "Page 3", "Track 11")
albumtwo = KPopAlbum("vending machine", "flat displaying a photo of Donghyuck and Injun", "Taeraesa Kim", "Page 23", "Track 1")
albumthree = KPopAlbum("limited", "flat displaying a photo of Haobin", "Sky Kim", "Page 14", "Track 5")
albumfour = KPopAlbum("digipack", "flat displaying a photo of Jiwoon", "Seok Woohyun", "Page 28", "Track 10")
albumfive = KPopAlbum("jewel case", "flat displaying a photo of Shun, Kyo, and Ken", "Hannah Bhang", "Page 8", "Track 8")
print (albumone.version)
print (albumtwo.poster)
print (albumthree.photocard)
print (albumfour.photobook)
print (albumfive.cd)

"""
After running the code above, it will display the album version, poster image, photocard version (which shows the name of the K-Pop Idol), photobook page, and track played on the album CD.
I made five album variations to show the randomness of the inclusions that come with every K-Pop Album.
I am only describing the inclusions; hence, there is no numerical change or increase in value.
"""

# This is the code for Class 6: Digital Camera
class DigiCam:
# Attributes of Digital Camera Class
    def __init__(self, l, f, vf, s, mc):
        self.lens = l
        self.flash = f
        self.viewfinder = vf 
        self.shutter = s
        self.memorycard = mc 

# Methods for Digital Camera Class
    def change_lens(self):
        self.lens = self.lens + 10
    
    def adjust_flash(self):
        self.flash = self.flash + 0.5
        
    def peek_through_viewfinder(self):
        self.viewfinder = self.viewfinder
    
    def press_shutter(self):
        self.shutter = self.shutter
        
    def insert_memorycard(self):
        self.memorycard = self.memorycard + 256

# Created a Camera Object
camera = DigiCam(360, 9, "You saw the white sandy beach through the viewfinder", "The shutter was pressed", 0)
print ("Before change lens:", camera.lens)
camera.change_lens()
print ("After change lens:", camera.lens)
print ("Before adjust flash:", camera.flash)
camera.adjust_flash()
print ("After adjust flash:", camera.flash)
print (camera.viewfinder)
print (camera.shutter)
print ("Before insert memory card:", camera.memorycard)
camera.insert_memorycard()
print ("After insert memory card:", camera.memorycard)

"""
After running the code above, it will display the change in the numerical value of the lens millimeter (which affects the focal length of the camera), flash value, and memory card storage value. It also describes what a person can see through their viewfinder and if the camera's shutter is pressed.
I tried simulating the way a person uses a camera through code.
"""

# This is the code for Class 7: Guitar
class Guitar:
# Attributes of Guitar Class
    def __init__(self, st, fb, t, b, n):
        self.strings = st
        self.fretboard = fb
        self.type = t 
        self.body = b
        self.neck = n

# Methods for Guitar Class
    def tune_strings(self):
        self.strings = self.strings + 1
    
    def strum_chord(self):
        self.fretboard = self.fretboard
    
    def determine_type(self):
        self.type = self.type
        
    def knock_on_body(self):
        self.body = self.body
        
    def hold_neck(self):
        self.neck = self.neck

# Created a Guitar Object
guitarnitaerae = Guitar(0, "You strummed the G Chord", "Yamada Acoustic Guitar", "You knocked on your guitar's body", "You are holding your guitar by its neck")
print ("Before tune strings:", guitarnitaerae.strings)
guitarnitaerae.tune_strings()
print ("After tune strings:", guitarnitaerae.strings)
print(guitarnitaerae.fretboard)
print(guitarnitaerae.type)
print(guitarnitaerae.body)
print(guitarnitaerae.neck)

"""
After running the code above, it will display the increase in the numerical value of the tuned chord. This change simulates the increase in the chord's pitch once you twist the tuning peg for that chord.
The code also describes the different actions a person does with their guitar. It also notes the guitar type. I had to modify one of the methods so that all of the attributes have a corresponding method.
"""

# This is the code for Class 8: Computer Mouse
class CompMouse:
# Attributes of Computer Mouse Class
    def __init__(self, c, w, wh, bt, tp):
        self.color = c
        self.weight = w
        self.wheel = wh 
        self.button = bt
        self.type = tp

# Methods for Computer Mouse Class
    def see_color(self):
        self.color = self.color 
    
    def discover_weight(self):
        self.weight = self.weight + 4.23

    def scroll_up(self):
        self.wheel = self.wheel
    
    def click_left_button(self):
        self.button = self.button
        
    def determine_type(self):
        self.type = self.type

# Created a Mouse Object
desktopmouse = CompMouse("black", 0, "You scrolled up", "You left-clicked", "wireless mouse")
print(desktopmouse.color)
print ("Before discover weight:", desktopmouse.weight)
desktopmouse.discover_weight()
print ("After discover weight:", desktopmouse.weight)
print(desktopmouse.wheel)
print(desktopmouse.button)
print(desktopmouse.type)

""" 
After running the code above, it will display the color, weight, and type of the Computer Mouse. The code also describes the actions taken by the person if they use the mouse wheel to scroll and click its button.
I had to modify one of the methods so that all of the attributes have a corresponding method.
"""
