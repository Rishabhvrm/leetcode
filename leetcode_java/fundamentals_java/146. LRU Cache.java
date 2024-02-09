package leetcode_java.fundamentals_java;

import java.util.HashMap;

class ListNode {
    int key;
    int val;
    ListNode prev;
    ListNode next;

    public ListNode(int key, int val) {
        this.key = key;
        this.val = val;
    }
}
// back  ~ MRU, if val is added/updated, move its node here
// front ~ LRU, will be removed from here
class LRUCache {

    HashMap<Integer, ListNode> dic;
    int capacity;
    ListNode head;
    ListNode tail;

    /* Initialize your data structure here */
    public LRUCache(int capacity) {
        this.capacity = capacity;
        dic = new HashMap<>();
        head = new ListNode(-1, -1);
        tail = new ListNode(-1, -1);
        head.next = tail;
        tail.prev = head;
    }
    
    // get the value associated with the key
    public int get(int key) {
        // if key not in hashmap
        if (!dic.containsKey(key))
            return -1;
        
        ListNode node = dic.get(key);           // get the node for the key
        remove(node);                           // remove the node from its current position
        add(node);                              // add the node to the end of the doubly LL (MRU)
        return node.val;
    }

    // add a key value pair to cache
    public void put(int key, int value) {
        // if key already exists, update the key value(node) pair in dic
        // first remove the node from queue
        if (dic.containsKey(key)) {
            ListNode oldNode = dic.get(key);
            remove(oldNode);
        }

        // if key doesn't already exist, add it
        ListNode node = new ListNode(key, value);
        dic.put(key, node);
        add(node);                              // add the node to the end of the doubly LL (MRU)

        // check if size goes beyond capacity
        // if yes then remove the LRU node ~ first ~ head
        if (capacity < dic.size()) {
            ListNode nodeToDelete = head.next;
            remove(nodeToDelete);
            dic.remove(nodeToDelete.key);       // remove the LRU key from dic as well
        }

    }

    // add node to tail ~ back ~ MRU
    public void add(ListNode node) {
        ListNode previousEnd = tail.prev;
        previousEnd.next = node;
        node.prev = previousEnd;
        node.next = tail;
        tail.prev = node;
    }

    // remove a node from LL
    public void remove(ListNode node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
    
}
