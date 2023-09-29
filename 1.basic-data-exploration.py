#Nadhifi Qurrunul B F H
#1103204156
#Tugas ke-1

# Impor pustaka yang diperlukan
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Membaca data dari file CSV 
data = pd.read_csv('melb_data.csv')

# Menampilkan 5 baris pertama data
print("5 Baris Pertama Data:")
print(data.head())

# Informasi tentang dataset
print("\nInformasi Data:")
print(data.info())

# Statistik deskriptif dasar
print("\nStatistik Deskriptif:")
print(data.describe())

# Menghitung jumlah data yang hilang per kolom
print("\nJumlah Data yang Hilang per Kolom:")
print(data.isnull().sum())

# Visualisasi sederhana
plt.hist(data['Suburb'], bins=20)
plt.xlabel('Label sumbu X')
plt.ylabel('Label sumbu Y')
plt.title('Judul Histogram')
plt.show()


Statistik Deskriptif:
              Rooms         Price      Distance      Postcode  ...    YearBuilt     Lattitude    Longtitude  Propertycount
count  13580.000000  1.358000e+04  13580.000000  13580.000000  ...  8205.000000  13580.000000  13580.000000   13580.000000      
mean       2.937997  1.075684e+06     10.137776   3105.301915  ...  1964.684217    -37.809203    144.995216    7454.417378      
std        0.955748  6.393107e+05      5.868725     90.676964  ...    37.273762      0.079260      0.103916    4378.581772      
min        1.000000  8.500000e+04      0.000000   3000.000000  ...  1196.000000    -38.182550    144.431810     249.000000      
25%        2.000000  6.500000e+05      6.100000   3044.000000  ...  1940.000000    -37.856822    144.929600    4380.000000      
50%        3.000000  9.030000e+05      9.200000   3084.000000  ...  1970.000000    -37.802355    145.000100    6555.000000      
75%        3.000000  1.330000e+06     13.000000   3148.000000  ...  1999.000000    -37.756400    145.058305   10331.000000      
max       10.000000  9.000000e+06     48.100000   3977.000000  ...  2018.000000    -37.408530    145.526350   21650.000000 

Jumlah Data yang Hilang per Kolom:
Suburb              0
Address             0
Rooms               0
Type                0
Price               0
Method              0
SellerG             0
Date                0
Distance            0
Postcode            0
Bedroom2            0
Bathroom            0
Car                62
Landsize            0
BuildingArea     6450
YearBuilt        5375
CouncilArea      1369
Lattitude           0
Longtitude          0
Regionname          0
Propertycount       0
dtype: int64
