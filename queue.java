class Queue {
    private int arr[];
    private int first; 
   
    public int size(int arr[]) {
        return sizeof.arr;
    }
    
    public boolean isEmpty() {
        if (size(arr) == 0) {
            return true;
        } else {
            return false;
        }
    }
   
    public boolean push(int x) {
        // Size of the array
        int index = size();
        if (index > -1) {
           arr.append(x);
           return true;
        }
        
        return false;
    }
    
    public int pop() {
        if (!isEmpty()) {
            int temp = arr[0];
            // pop first element
            arr = arr.slice(1, size(arr));
            
            return temp;
        } 
       
        return -1;
       
    }
  
    
    

}

