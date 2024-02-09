package leetcode_java.fundamentals_java;

/*
 * 'super' keyword allows for accessing 
 * a) superclass members,
 * b) invoking superclass constructors,
 * c) invoking overridden superclass methods 
 */

class Test {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.display();
        d.eat();
    }
}

class Animal {
    String color = "white";

    Animal() {
        System.out.println("Animal Constructor");
    }
    
    void display() {
        System.out.println("I am an Animal");
    }

    void eat() {
        System.out.println("Animal is eating");
    }
}

class Dog extends Animal {
    String color = "black";

    Dog() {
        super(); // java is going to call it by default as well even if we don't call it here
        System.out.println("Dog Constructor");
    }

    void display() {
        System.out.println("I am a Dog");
        System.out.println("Color: " + color);   // accessing subclass field
        System.out.println("Superclass color: " + super.color);   // accessing superclass field
        super.display();  // invoking superclass method
    }

    void eat(){
        // Accessing Superclass Methods Overridden by the Subclass:
        super.eat();  // Invoking superclass method
        System.out.println("Dog is eating");
    }
}