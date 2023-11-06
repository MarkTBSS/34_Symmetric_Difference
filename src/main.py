print("===== Creat =====")
mySet = {1, 2, 1} # ประกาศชนิดตัวแปรเป็น set
print(mySet) # ค่าไม่ซ้ำไม่เรียงเพราะมันเป็น set
mySet = set()  # ประกาศชนิดตัวแปรเป็น set แบบว่างๆ 
mySet = set(['a', 'b', 'a']) # ใส่ค่าใน set
print(mySet) # ค่าไม่ซ้ำไม่เรียงเพราะมันเป็น set
print("===== Modify (Add) =====")
mySet.add('c') # เติม c เข้าไป
print(mySet) # มี c เพิ่มมาอีก
mySet.add('a') # บรรทัดนี้ไม่มีอะไรเกิดขึ้นเพราะ a มีอยู่แล้ว
mySet.add((5, 4)) # เติม dict(5,4) เข้าไป
print(mySet) # {(5, 4), 'b', 'c', 'a'} 
print("===== Modify (Update) =====")
#mySet.add([1, 2, 3, 4]) # error เพราะ add เพิ่มได้ทีละ 1 element
mySet.update([1, 2, 3, 4]) # ต้องใช้ update แทน
print(mySet) # ไม่เรียงและไม่ซ้ำ
mySet.update({1, 7, 8, 'a'}) # แบบนี้ก็ได้
print(mySet) # ไม่เรียงและไม่ซ้ำ
mySet.update(('x', 'y')) # ต้องเน้นว่า update จะใส่แยก ไม่ได้ใส่เหมือน add
print(mySet) # x ตัว y ตัว
mySet.add(('x', 'y'))
print(mySet) # เติม ('x', 'y')
print("===== Remove =====")
mySet.discard('x') # เอา x ออก ถ้าไม่มี 'x' ก็ไม่ error
print(mySet) 
#mySet.remove('x') # ถ้าหาไม่พบจะแสดง error

a = {2, 4, 5, 9}
b = {2, 4, 11, 12}
print("===== Union ======")
c = a.union(b) # รวมกัน
print(c)
print("===== Intersection ======")
c = a.intersection(b) # ซ้ำกัน
print(c)
print("===== Difference ======")
c = a.difference(b) # แสดงในสิ่งที่ a ต่างจาก b
print(c)
c = b.difference(a) # แสดงในสิ่งที่ b ต่างจาก a
print(c)