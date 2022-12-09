from laptrinhdoituong.student import SinhVien

def main():
    sv = [SinhVien("Tran Thinh", 2006, 5),
          SinhVien("Tran Hoang", 2004, 5),
          SinhVien("Tran Thanh", 2006, 9),
          SinhVien("Tran Dy", 2009, 10),
          SinhVien("Tran Huy", 2009, 7),
          SinhVien("Tran Long", 2008, 2),
          SinhVien("Tran Duc", 2009, 4),
          SinhVien("Tran Kien", 2006, 1)]
    sv = sorted(sv, reverse=False)
    for i in (sv):
        print('Phan tu  la', i)
if __name__=='__main__':
  main()
