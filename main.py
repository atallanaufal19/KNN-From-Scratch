import pandas as pd

#Hitung Jarak dengan Manhattan Distance lalu menentukan kelasnya
def predict(x1,x2,x3,Y,y1,y2,y3, k):
    kelas = []
    for i in range(len(y1)):
        dump = []
        for j in range(len(x1)):
            #Ngitung Manhattan Distance
            dump.append(abs(y1[i]-x1[j])+abs(y2[i]-x2[j])+abs(y3[i]-x3[j]))
        #Sorting untuk menentukan kelas
        Kelas = [x for _,x in sorted(zip(dump,Y))]
        Kelas_hasil = Kelas[0:k]
        kelas.append(max(set(Kelas_hasil), key = Kelas_hasil.count))
    return kelas


#Evaluasi dengan membanding 1/2 data latihan dengan 1/2 data latihan lagi
def evaluasi(x1,x2,x3,Y, k):
    tX1 = x1[148:296]
    tX2 = x2[148:296]
    tX3 = x3[148:296]
    tXY = Y[148:296]
    tY1 = x1[0:148]
    tY2 = x2[0:148]
    tY3 = x2[0:148]
    tYY = Y[0:148]
    
    output = predict(tX1,tX2,tX3,tXY,tY1,tY2,tY3,k)
    count = 0
    for i in range(len(output)):
        if output[i] == tYY[i]:
            count += 1
    print("akurasi dengan K =",k,": ",((count/len(output))) * 100,"%")

#Running
#Baca Data
data = pd.ExcelFile('traintest.xlsx')
datatrain = pd.read_excel(data, 'train')
datatest = pd.read_excel(data, 'test')
x1 = datatrain['x1'].tolist()
x2 = datatrain['x2'].tolist()
x3 = datatrain['x3'].tolist()
Y = datatrain['y'].tolist()

id = datatest['id'].tolist()
y1 = datatest['x1'].tolist()
y2 = datatest['x2'].tolist()
y3 = datatest['x3'].tolist()

#Custom K di sini
k = int(input("masukkan K : ", ))
output = predict(x1, x2, x3, Y, y1,y2,y3,k)
evaluasi(x1,x2,x3,Y,k)

#Tulis Data
df = pd.DataFrame({'id': id, 'x1': y1, 'x2': y2, 'x3': y3, 'y': output})
df.to_excel('hasilKNN.xlsx', index= False)

