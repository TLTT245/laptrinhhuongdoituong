class SinhVien:
    def __init__(self,fullname,birth,score):
        self.hoten = fullname
        self.namsinh = birth
        self.dtb = score
    def __str__(self):
        message ='[hoten:'+self.hoten+';namsinh:'+str(self.namsinh)+';dtb:'+str(self.dtb)+']'
        return message
def main():
    sv1 = SinhVien("Tran Thinh",2004,10)
    sv2 = SinhVien("Nguyen Long",2005,12)
    print(sv1)
if __name__=='__main__':
    main()