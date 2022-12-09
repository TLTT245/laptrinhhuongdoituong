from laptrinhdoituong.student import SinhVien
def main():
    sv = [SinhVien("Tran Thinh", 2003, 10),
        SinhVien("Tran Hoang", 2004, 8),
        SinhVien("Tran Thanh", 2006, 9),
        SinhVien("Tran Dy", 2009, 10),
        SinhVien("Tran Huy", 2009, 7),
        SinhVien("Tran Long", 2008, 2),
        SinhVien("Tran Duc", 2009, 4),
        SinhVien("Tran Kien", 2006, 1)]
    for i in range (-1,len(sv)-1,1):
        i = i+1
        print('Phan tu thu',i,'la',sv[i])
if __name__=='__main__':
    main()
