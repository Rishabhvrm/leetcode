package leetcode_java;

class ParkingSystem {
    private int arr [];

    public ParkingSystem(int big, int medium, int small) {
        arr = new int[] {0, big, medium, small};
    }
    
    public boolean addCar(int carType) {
        // check if there's space
        //      if there's not, return false
        //      if there is, decrement space and return true
        if (arr[carType] == 0) {
            return false;
        }
        else {
            arr[carType] -= 1;                   // decrement availableSlots
            return true;
        }




    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 ParkingSystem obj = new ParkingSystem(big, medium, small);
 boolean param_1 = obj.addCar(carType);
 */