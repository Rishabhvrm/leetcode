package leetcode_java;

import java.util.Stack;
import java.util.Deque;
import java.util.ArrayDeque;

/**
 * Class: MinStackTest
 * Description: This class contains unit tests for the MinStack and MinStack2 classes.
 */
class MinStackTest {

    /**
     * Method: testMinStack
     * Description: Tests the MinStack class.
     */
    public void testMinStack() {
        MinStack minStack = new MinStack();
        minStack.push(-2);
        minStack.push(0);
        minStack.push(-3);
        assert minStack.getMin() == -3; // Expected minimum is -3
        minStack.pop();
        assert minStack.top() == 0; // Top element should be 0
        assert minStack.getMin() == -2; // Minimum should be -2
    }

    /**
     * Method: testMinStack2
     * Description: Tests the MinStack2 class.
     */
    public void testMinStack2() {
        MinStack2 minStack2 = new MinStack2();
        minStack2.push(-2);
        minStack2.push(0);
        minStack2.push(-3);
        assert minStack2.getMin() == -3; // Expected minimum is -3
        minStack2.pop();
        assert minStack2.top() == 0; // Top element should be 0
        assert minStack2.getMin() == -2; // Minimum should be -2
    }

    /**
     * Method: main
     * Description: Main method to run the unit tests.
     * @param args Command-line arguments (not used)
     */
    public static void main(String[] args) {
        MinStackTest minStackTest = new MinStackTest();
        minStackTest.testMinStack();
        minStackTest.testMinStack2();
    }
}


/**
 * APPROACH-1
 * Class: MinStack
 * Description: This class implements a stack that supports push, pop, top, and retrieving the minimum element in constant time.
 * Approach: Using another stack (minStack) to keep track of the minimum element so far.
 */
class MinStack {
    Stack<Integer> stack; // Stack to store elements
    Stack<Integer> minStack; // Stack to keep track of minimum element

    /**
     * Constructor: MinStack
     * Description: Initializes the main stack and the minStack with a single element of Integer.MAX_VALUE.
     */
    public MinStack() {
        stack = new Stack<>();
        minStack = new Stack<>();
        minStack.push(Integer.MAX_VALUE);
    }
    
    /**
     * Method: push
     * Description: Pushes the element onto the stack and updates the minStack if the pushed element is smaller than or equal to the current minimum.
     * @param val The value to be pushed onto the stack
     */
    public void push(int val) {
        stack.push(val);
        if (val <= minStack.peek()) {
            minStack.push(val);
        }
    }
    
    /**
     * Method: pop
     * Description: Pops the top element from the stack and updates the minStack if the popped element is equal to the current minimum.
     */
    public void pop() {
        int ele = stack.pop();
        if (ele == minStack.peek()){
            minStack.pop();
        }
    }
    
    /**
     * Method: top
     * Description: Returns the top element of the stack without removing it.
     * @return The top element of the stack
     */
    public int top() {
        return stack.peek();
    }
    
    /**
     * Method: getMin
     * Description: Returns the current minimum element in the stack.
     * @return The current minimum element in the stack
     */
    public int getMin() {
        return minStack.peek();
    }
}

/**
 * APPROACH-2
 * Class: MinStack2
 * Description: This class implements a stack that supports push, pop, top, and retrieving the minimum element in constant time.
 * Approach: Using only 1 stack and storing an Integer array in its stack frame.
 */
class MinStack2 {
    Deque<Integer[]> stack; // Deque to store elements and their corresponding minimums

    /**
     * Constructor: MinStack2
     * Description: Initializes the stack with a single element containing null and Integer.MAX_VALUE.
     */
    public MinStack2() {
        stack = new ArrayDeque<>();
        Integer[] initialVal = {null, Integer.MAX_VALUE};
        stack.push(initialVal);
    }
    
    /**
     * Method: push
     * Description: Pushes the element onto the stack along with its corresponding minimum value.
     * @param val The value to be pushed onto the stack
     */
    public void push(int val) {
        stack.push(new Integer[] {val, Math.min(val, stack.peek()[1])});
    }
    
    /**
     * Method: pop
     * Description: Pops the top element from the stack.
     */
    public void pop() {
        stack.pop();
    }
    
    /**
     * Method: top
     * Description: Returns the top element of the stack without removing it.
     * @return The top element of the stack
     */
    public int top() {
        return stack.peek()[0];
    }
    
    /**
     * Method: getMin
     * Description: Returns the current minimum element in the stack.
     * @return The current minimum element in the stack
     */
    public int getMin() {
        return stack.peek()[1];
    }
}

