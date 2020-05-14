import classtest01.class_ahntaewoong as cal
import pickle

cal1 = cal.test1()
cal2 = cal.test2()
cal3 = cal.test3()
cal4 = cal.test4()

pickle.dump(cal1, open("./cal1.pkl", "wb"))
pickle.dump(cal2, open("./cal2.pkl", "wb"))
pickle.dump(cal3, open("./cal3.pkl", "wb"))
pickle.dump(cal4, open("./cal4.pkl", "wb"))


emp_pkl1 = pickle.load(open("./cal1.pkl", "rb"))
emp_pkl2 = pickle.load(open("./cal2.pkl", "rb"))
emp_pkl3 = pickle.load(open("./cal3.pkl", "rb"))
emp_pkl4 = pickle.load(open("./cal4.pkl", "rb"))

emp_pkl1.getTest(3)
emp_pkl2.getTest(3)
emp_pkl3.getTest(0,1)
emp_pkl4.getTest(0,2)
