package leetcode_java;

import java.util.HashMap;

// LC 1507. Reformat Date (https://leetcode.com/problems/reformat-date/)
class Solution {
    private static final HashMap<String, String> months = getMonth();
    
    public static void main(String[] args) {
        System.out.println(reformatDate("20th Oct 2052"));
    }

    public static String reformatDate(String date) {
        // [0]: day, [1]: month, [2]: year
        String [] dateArr = date.split("\\s+");

        String day = dateArr[0];                // get day
        String month = dateArr[1];              // get month
        String year = dateArr[2];               // get year
        
        int day_len = day.length();
        day = day.substring(0, day_len - 2);    // remove 'th', 'nd', 'st', 'rd'
            
        if (Integer.parseInt(day) < 10) {       // add a 0 if day is single digit
            day = "0" + day;
        }

        return year + "-" + months.get(month) + "-" + day;
    }

    private static HashMap<String, String> getMonth() {
        HashMap<String, String> month_map = new HashMap<>();
        month_map.put("Jan", "01");
        month_map.put("Feb", "02");
        month_map.put("Mar", "03");
        month_map.put("Apr", "04");
        month_map.put("May", "05");
        month_map.put("Jun", "06");
        month_map.put("Jul", "07");
        month_map.put("Aug", "08");
        month_map.put("Sep", "09");
        month_map.put("Oct", "10");
        month_map.put("Nov", "11");
        month_map.put("Dec", "12");
        return month_map;
    }
}