// Last updated: 2/9/2026, 9:54:38 PM
class MyHashMap {

    LinkedList<Entry>[] list;
    final int SIZE = 1000;
    public MyHashMap() {
        list = new LinkedList[SIZE];  
    }
    
    public void put(int key, int value) {
        int placement = key%SIZE;
        if(list[placement] == null) {
            list[placement] = new LinkedList<Entry>();
            list[placement].add(new Entry(value, key));
        }
        else {
            for(int i = 0; i < list[placement].size(); i++) {
                if(list[placement].get(i).key == key) {
                    list[placement].get(i).val = value;
                    return;
                }
            }
            list[placement].add(new Entry(value, key));
        }
        
    }
    
    public int get(int key) {
        int placement = key%SIZE;
        if(list[placement] == null) return -1;
        else {
            for(int i = 0; i < list[placement].size(); i++) {
                if(list[placement].get(i).key == key) {
                    return list[placement].get(i).val;
                }
            }
            return -1;
        }
    }
    
    public void remove(int key) {
        int placement = key%SIZE;
        Entry toRemove = null;
        
        if(list[placement] == null) return;
         else {
            for(int i = 0; i < list[placement].size(); i++) {
                if(list[placement].get(i).key == key) {
                    toRemove = list[placement].get(i);
                }
            }
            if(toRemove != null) list[placement].remove(toRemove);
        }

    }
}

class Entry {
    int val;
    int key;

    public Entry(int val, int key) {
        this.key = key;
        this.val = val;
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */