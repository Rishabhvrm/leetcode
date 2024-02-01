package leetcode_java;

import java.util.Collections;
import java.util.ArrayList;
import java.util.Arrays;

class Test {
    public static void main(String[] args) {
        
        Dog d = new Dog();
        System.out.println(d.getName());
        d.setName("jake");
        System.out.println(d.getName());
        arrayList.arrayMethod();
    }
}

// 'this' keyword
class Dog {
    private String name;
    private int age;

    public Dog() {
        this("defaultName", 0);

        // above line is similar to following
        // this.name = "defaultName";
        // this.age = 0;
    }
    
    public Dog(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void setName(String n) {
        name = n;
        // this.name = n;
        String name = "John";
        System.out.println(this.name + " and " + name);
    }

    public String getName() {
        return name;
    }
}

// ArrayList
class arrayList {
    public static void arrayMethod() {
        ArrayList<String> cars = new ArrayList<>();
        cars.add("Bugati");
        cars.add("Volvo");
        cars.add("BMW");
        cars.add("Ford");
        cars.add("Mazda");

        System.out.println(cars);
        Collections.sort(cars);
        System.out.println(cars);

        int[] arr1 = {30,20,10,50,40};
        int[] arr2 = {3,2,1,5,4};
        System.out.println(Arrays.toString(arr1));
        System.out.println(Arrays.toString(arr2));
        System.out.println(Arrays.compare(arr1, arr2));
        System.out.println(Arrays.toString(arr1));
        System.out.println(Arrays.toString(arr2));
    }
}