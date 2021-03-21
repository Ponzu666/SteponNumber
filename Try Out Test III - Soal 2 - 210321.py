def steponNumber(x, y):  #paham pattern dari gambar soal nomor 2, tapi kurang mampu menerjemahkan ke dalam kode
    if x < y: 
        return x + y + 2 * ((y - x) // 2)  
       
    else: 
        return x + y + 2 * (((x - y) + 1) // 2)  
  
if __name__ == "__main__":  
   
    x = int(input('masukkan : '))
    y = int(input('masukkan : '))
    print(steponNumber(x, y))  