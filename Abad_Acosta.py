# The succeeding lines are Mekyla Abad's contribution to this Assignment
#This is the code for the Cellphone Class (Parent Class)
class Cellphone:
# Attributes of the Cellphone Class
    def __init__(self, on, o, l, b, u):
	    self.on = on
	    self.off = o
	    self.locked = l
	    self.battery = b
	    self.unit = u

# Methods for Cellphone Class
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

# This is the code for the Samsung Class (Child Class)
class Samsung(Cellphone):
# Attributes of the Samsung Class
    def __init__(self, c, n, a, br, on, o, l, b, u):
        super().__init__(on, o, l, b, u)
        self.connection = c
        self.notification = n
        self.__application = a
        self.brightness = br
        
# Methods for the Samsung Class
    def fix_connection(self):
        print ("Connection: ", self.connection)
    def manage_notification(self):
        print ("Notification: ", self.notification)
    def adjust_brightness(self):
        print ("Brightness: ", self.brightness)
    
# Getter and Setter methods for the private variable application
    def set_application(self, a):
        self.__application = a
        
    def get_application(self):
        print(self.__application)

"""
I set the attribute application into private because in reality, there are applications
in our phones that we don't want anyone to access immediately, especially those that
involves personal information and important stuff. As much as possible, we want privacy 
and would not like others to know things that they shouldn't know about.
"""  

# Main Program
#Created an object named 'cp' for the Parent Class, which is Cellphone	
cp = Cellphone("on", "off", "love", "low battery", "Samsung A50s")

print (cp.on)
print (cp.off)
print (cp.locked)
print (cp.battery)
print (cp.unit)

"""
After running the code above, it will show the on and off status of the phone, the password love
to unlock the attribute 'locked,' notify that it is 'low battery' already, and that the phone's unit is 
Samsung A50s.
"""

# Created an object named 'kyla' for the Child Class, which is Samsung
kyla = Samsung("Sky Fiber", "Detailed", "Insert private application", "600 nits", "on", "off", "kylavers", "Fully charged","Samsung Galaxy Z Flip 5")

print (kyla.connection)
print (kyla.notification)
print (kyla.brightness)
print (kyla.on)
print (kyla.off)
print (kyla.locked)
print (kyla.battery)
print (kyla.unit)

# Code to make the private attribute application publicly visible 
kyla.get_application()
kyla.set_application("GCash")
kyla.get_application()

"""
The object 'cp' for the parent class Cellphone is only an example of common 
characteristics of a phone. It can be turn on and off, has a password, 
display the battery status, and sample unit of a phone. On the other hand,
the object 'kyla'for the child class Samsung is somehow more specific. Aside
from the fact that it can also be turn on and off, type a password to unlock,
show the battery level, and the phone's unit, it also reveals the cellphone's
WiFi connection, notification setting, brightness level, and an application 
that requires privacy.
"""

"""
Indeed, inheritance allows code reusability and encapsulation allows us to
restrict access from information we want to be protected. This activity 
allowed us to practice the lessons and principles discussed from the previous
weeks. It is hard, especially for a beginner like me, but if there's the will
to learn, then anything can be possible.
"""

# The succeeding lines are Misaki Acosta's contribution to this Assignment
# This is the code for the K-Pop Album Class (Parent Class)
class KPopAlbum:
# Attributes of the K-Pop Album Class
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

# This is the code for the Pre-Order Benefits (POB) Class (Child Class)
class POB(KPopAlbum):
# Attributes of the POB Class
    def __init__(self, e, b, f, s, v, p, pc, pb, c):
        super().__init__(v, p, pc, pb, c)
        self.exclusive_photocard = e
        self.__videocall_benefit = b
        self.folder = f
        self.sticker = s
        
# Methods for the POB Class
    def pull_random_exclusive_photocard(self):
        print ("Exclusive Photocard: ", self.exclusive_photocard)
    def get_random_a4_folder(self):
        print ("A4 Folder: ", self.folder)
    def obtain_random_sticker_set(self):
        print ("Sticker: ", self.sticker)
    
# Getter and Setter methods for the private variable videocall_benefit
    def set_videocall_benefit(self, b):
        self.__videocall_benefit = b
        
    def get_videocall_benefit(self):
        print(self.__videocall_benefit)

"""
The attribute videocall_benefit is private since, in a real-life context, 
the information on who the winners are in the raffled video call benefit is not publicly disclosed. 
Only the winners of the video call benefit know if they won the prize. 
"""  
# Main Program
# Created Different Regular K-Pop Album Variations
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

# Created a Special/Limited Edition K-Pop Album which includes the POB
specialalbum = POB("Charisma Hao (Cat Ver.)", "Insert Winner's Name Here", "Dear Dream A4 Clear Folder", "S-Class Sticker Set", "mixtape", "flat displaying a group yearbook layout", "Shen Quan Rui","Page 27", "Track 3")

print (specialalbum.exclusive_photocard)
print (specialalbum.folder)
print (specialalbum.sticker)
print (specialalbum.version)
print (specialalbum.poster)
print (specialalbum.photocard)
print (specialalbum.photobook)
print (specialalbum.cd)

# Code to make the private attribute videocall_benefit publicly visible 
specialalbum.get_videocall_benefit()
specialalbum.set_videocall_benefit("Akiara Acosta-Kim")
specialalbum.get_videocall_benefit()

"""
Regular Albums and Special Albums share attributes such as the album version, poster image, photocard version (which shows the name of the K-Pop Idol), photobook page, and track played on the album CD.
However, unlike the other Regular K-Pop Albums above, the Special Album has Pre-Order Benefits (POB). These Pre-Order benefits are rare; only those fans who ordered the album early or its limited version can have them. 
The most common POBs are exclusive photocards and the video call benefit. The exclusive photocards contain a rare selfie taken by the K-Pop Idol. As for the video call benefit, fans who win this can interact with their K-Pop idol through a video call. 
As for the folder and sticker, it is usually a "limited edition" benefit for the K-Pop Album's Japan release. 
Fans can only get these benefits if they purchase the album from a specific shop (like Makestar, Withmuu, etc.) or a CD store in Japan. 
However, the POB from one store differs from that from another store.
No POBs are the same from various stores.
"""

"""
For this final assignment, I combined my interest in K-Pop with the concepts of OOP we learned this trimester, which made the coding process fun. 
At first, I coded my setters and getters wrong since I realized I missed an underscore in one line of code. 
Upon coming to this realization, I added the missing underscore. 
Adding this helped display my private attribute. 
Overall, I had fun learning more about coding and Python this trimester! 
I also hope that through my code, you can learn more about the different variations of K-Pop albums. 
"""
