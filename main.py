#Radhe Radhe
import pyscreenshot as ps

image=ps.grab(bbox=(10, 10, 500, 500))

image.show()

path=input("Enter the Path to save the image:")

filename=input("Enter the filename:")

extension=input("Enter the extension of the file:")
# image.save(r"C:\Users\lenovo\Desktop\1.png", "png") 
#"r" is for raw string, it is used to ignore the escape sequences in the string.
image.save(f"{path}/{filename}.{extension}", extension)


