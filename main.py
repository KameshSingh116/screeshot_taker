#Radhe Radhe
import pyscreenshot as ps

image=ps.grab(bbox=(10, 10, 500, 500))

image.show()

# image.save(r"C:\Users\lenovo\Desktop\1.png", "png") 
#"r" is for raw string, it is used to ignore the escape sequences in the string.
image.save("C:\\Users\\lenovo\\Desktop\\2.png", "png")

