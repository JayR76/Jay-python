# #hybrid inheritance:combination of two inheritance. 
 
# class a:
#     pass 
# class b(a): 
#     pass 
# class c(a): 
#     pass 
# class d(b,c:)
#     pass 
 
class Read: 
     pass 
class books(Read): 
    def students(self):
        print("Chadavara")  
class pdfs(Read): 
     def students(self): 
         print("anukoni chadivey") 
class study(books,pdfs):  
     pass            
obj=study() 
obj.students()    
