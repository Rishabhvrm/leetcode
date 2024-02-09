package leetcode_java.fundamentals_java;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

class DesignHashMap {
    public static void main(String[] args) {
        MyHashMap map = new MyHashMap();
        map.put(1,10);
        map.put(2,20);
        map.put(3,30);

        System.out.println(map.get(2));        // 20
        map.remove(2);
        System.out.println(map.get(2));        // -1


    }
}

class Tuple<U,V> {
    public U first;
    public V second;

    public Tuple(U first, V second) {
        this.first = first;
        this.second = second;
    }
}

class Bucket {
    private List<Tuple<Integer,Integer>> bucket;

    public Bucket() {
        this.bucket = new LinkedList<Tuple<Integer, Integer>>();
    }

    public void update(Integer key, Integer value) {
        boolean found = false;

        // if key is present, update the value
        for (Tuple<Integer, Integer> pair : this.bucket) {
            if (pair.first.equals(key)) {
                pair.second = value;
                found = true;
            }
        }
        
        // if key not present, add a tuple value to this bucket
        if (!found)
            this.bucket.add(new Tuple<Integer, Integer>(key, value));
    }

    public Integer get(Integer key) {
        for (Tuple<Integer, Integer> pair : this.bucket) {
            if (pair.first.equals(key))
                return pair.second;
        }
        return -1;
    }

    public void remove(Integer key) {
        for (Tuple<Integer, Integer> pair : this.bucket) {
            // if key found in bucket, del it
            if (pair.first.equals(key)) {
                this.bucket.remove(pair);                        // remove method of LinkedList
                break;
            }
        } 
    }
}

class MyHashMap {
    // hash function design
    // collision handeling
    private int keySpace;                                       // number of buckets
    private List<Bucket> hashTable; 

    public MyHashMap() {
        /* Initialize your data structure here */
        this.keySpace = 2069;                                   // a large prime number
        this.hashTable = new ArrayList<>();
        for (int i = 0; i < this.keySpace; ++i) {
            this.hashTable.add(new Bucket());
        }
    }

    // update value if key already present
    // else: add key value
    /* valid for only non-negative values */
    public void put(int key, int value) {
        int hash_key = key % this.keySpace;                     // calculate hash
        this.hashTable.get(hash_key).update(key, value);        // call update method on bucket
    }

    // if key present return value
    // else return -1
    public int get(int key) {
        int hash_key = key % this.keySpace;                     // calculate hash
        return this.hashTable.get(hash_key).get(key);           // call get method on bucket
    }

    // if key in map: remove key and value
    public void remove(int key) {
        int hash_key = key % this.keySpace;                     // calculate hash
        this.hashTable.get(hash_key).remove(key);               // call remove method on bucket
    }
}
