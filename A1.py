class LRU:
    def __init__(self,cache,cap):
        print("Init method declaration ")
        self.cache=[]
        self.cache.append(cache)
        self.cap=cap
        print(self.cap)
        
    def get(self):
        if(len(self.cache)==0):
            print("Apologies, Cache is empty!")
        else:
            c=self.cache.pop(0)
            return c
        
        
    def set(self,URL):
        if(len(self.cache)==self.cap):
            print("Cache size exceeded, removal of recent URL is being done to accept new URL's")
            self.cache.pop(0)
            self.cache.append(URL)
            return(f"URL Added: {URL}")
        
        else:
            self.cache.append(URL)
            return(f"Added the URL: {URL}")
        
    def display(self):
        return self.cache
    

class LRUtest(LRU):
    
    def __init__(self, URL,capacity):
        self.URL=URL
        self.capacity=capacity
        
    def testSet(self):
        k = f"URL Added {self.URL}"
        d=LRU("www.google.com",self.capacity)
        assert k == d.set("www.facebook.com"), "SET method succesfully tested"
        
    def testGet(self):
        j=self.URL
        a=LRU(j,self.capacity)
        i=a.get()
        assert j != i, "GET method succesfully tested"
        

def main():
    print("Enter a URL and LRUtest Capacity")
    v = str(input())
    c=int(input())
    g=LRUtest(v,c)
    z=True
    print("Enter your choice: ")
    y=int(input())
    print("Enter 1 for testing of SET Method")
    print("Enter 2 for testing of GET Method")
    while(z):
        if(y==1):
            g.testSet()
            break
        elif(y==2):
            g.testGet()
        else:
            print("Please enter a valid input!")
            z=False
    
 
if __name__ == "__main__":
    main()