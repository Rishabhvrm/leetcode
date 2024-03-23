package leetcode_java;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.Stack;
import java.util.HashMap;

class SolutionTest {

    /**
     * Method: isValid
     * Description: Checks whether a given string containing parentheses, brackets,
     *              and curly braces is valid or not.
     * @param s String to be checked
     * @return boolean indicating whether the string is valid or not
     */
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>(); // Stack to keep track of open brackets

        // HashMap to store mappings of closing brackets to their corresponding open brackets
        HashMap<Character, Character> parenthesis = new HashMap<>();
        parenthesis.put(')', '(');
        parenthesis.put('}', '{');
        parenthesis.put(']', '[');

        // Iterating through each character in the string
        for (char c : s.toCharArray()) {
            // If the character is an open bracket, push it onto the stack
            if (!parenthesis.containsKey(c)) {
                stack.push(c);
            } else {
                // If the character is a closing bracket
                // and the stack is empty or the top of the stack doesn't match
                // the corresponding open bracket, return false
                if (stack.isEmpty() || stack.peek() != parenthesis.get(c)) {
                    return false;
                }
                stack.pop(); // Pop the corresponding open bracket from the stack
            }
        }
        // If the stack is empty at the end, return true indicating the string is valid
        return stack.isEmpty();
    }

    @Test
    void testValidStrings() {
        assertTrue(isValid(""));
        assertTrue(isValid("()"));
        assertTrue(isValid("()[]{}"));
        assertTrue(isValid("{[]}"));
        assertTrue(isValid("[[[]]]"));
        assertTrue(isValid("(((((())))))"));
    }

    @Test
    void testInvalidStrings() {
        assertFalse(isValid("("));
        assertFalse(isValid(")"));
        assertFalse(isValid("([)]"));
        assertFalse(isValid("((("));
        assertFalse(isValid("(()))"));
    }

    public static void main(String[] args) {
        SolutionTest solutionTest = new SolutionTest();

        // Testing valid strings
        System.out.println("Testing valid strings:");
        System.out.println("isValid(\"\") -> " + solutionTest.isValid(""));
        System.out.println("isValid(\"()\") -> " + solutionTest.isValid("()"));
        System.out.println("isValid(\"()[]{}\") -> " + solutionTest.isValid("()[]{}"));
        System.out.println("isValid(\"{[]}\") -> " + solutionTest.isValid("{[]}"));
        System.out.println("isValid(\"[[[]]]\") -> " + solutionTest.isValid("[[[]]]"));
        System.out.println("isValid(\"(((((())))))\") -> " + solutionTest.isValid("(((((())))))"));

        // Testing invalid strings
        System.out.println("\nTesting invalid strings:");
        System.out.println("isValid(\"(\") -> " + solutionTest.isValid("("));
        System.out.println("isValid(\")\") -> " + solutionTest.isValid(")"));
        System.out.println("isValid(\"([)]\") -> " + solutionTest.isValid("([)]"));
        System.out.println("isValid(\"(((\") -> " + solutionTest.isValid("(((("));
        System.out.println("isValid(\"(()))\") -> " + solutionTest.isValid("(()))"));
    }
}
