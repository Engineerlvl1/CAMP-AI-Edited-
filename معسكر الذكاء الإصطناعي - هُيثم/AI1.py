#استيراد مكتبة OpenCV
import cv2

#just edited to test fork

#قراءة الصورة من ملف img.jpg وتخزينها في متغير image
image = cv2.imread("img.jpg")

#عرض الصورة على الشاشة في إطار يحمل اسم "Photo"
cv2.imshow('Photo' , image)

#انتظار الضغط على أي مفتاح على لوحة المفاتيح وتخزين القيمة المرتبطة به في المتغير I
I = cv2.waitKey(0)

#إذا تم الضغط على مفتاح الـ escape (الرمز 27 في لوحة المفاتيح) أو الحرف s في لوحة المفاتيح
#فإن جميع النوافذ المفتوحة في البرنامج ستتم إغلاقها
if I == 27 or I == ord('s'):
    cv2.destroyAllWindows()
