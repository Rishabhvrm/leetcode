package leetcode_java.fundamentals_java.threads;

// you can use threads by extending 'Thread' class or by implementing 'Runnable' interface

class MyThread extends Thread {
    public void run() {
        for (int i = 0; i < 5; i++) {
            System.out.println("Thread running: " + i + " for: " + this.threadId());
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

class MyRunnable implements Runnable {
    public void run() {
        for (int i = 0; i < 5; i++) {
            System.out.println("Thread running: " + i);
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

class Main {
    public static void main(String[] args) throws InterruptedException {
        
        // by extending thread class
        MyThread t1 = new MyThread();
        MyThread t2 = new MyThread();
        t1.start();
        t2.start();


        // by implement Runnable interface
        MyRunnable myRunnable = new MyRunnable();
        Thread th1 = new Thread(myRunnable);
        Thread th2 = new Thread(myRunnable);
        th1.start();
        th2.start();
    }
}