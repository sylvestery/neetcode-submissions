class DynamicArray {

    private int[] arr;
    private int length;
    private int capacity;
    public DynamicArray(int capacity) {
        this.capacity = capacity;
        this.length = 0;
        this.arr = new int[capacity];

    }
    private void throwIfOutofBounds(int i) {
        if  (i < 0  || i >= capacity)  {
            //throw IllegalArgumentException("Array out of bounds.");
        }
    }

    public int get(int i) {
        //this.throwIfOutOfBounds(i);
        return arr[i];

    }

    public void set(int i, int n) {
        //throw exception if i not in bounds.
        //throwIfOutOfBounds(i);
        arr[i] = n;

    }

    public void pushback(int n) {
        if (this.length == this.capacity) {
            resize();
        }
        this.arr[this.length] = n;
        length+=1;

    }

    public int popback() {
        if (length == 0) {
            //throw Exception("No elements in array");
            

        }
        return arr[--length];



    }

    private void resize() {
        //double capacity otherwise every operation will cause resize.
        int newCapacity = this.capacity *2;
        int[]  newArray =  new int[newCapacity];
        for (int i = 0; i < length; i++) {
            newArray[i] = this.arr[i];

        }

        this.arr = newArray;
        this.capacity = newCapacity;
    }

    public int getSize() {
        return length;

    }

    public int getCapacity() {
        return capacity;

    }
}
