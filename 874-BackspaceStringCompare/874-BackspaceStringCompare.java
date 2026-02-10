// Last updated: 2/9/2026, 9:54:31 PM
class Solution {
    public boolean backspaceCompare(String s, String t) {
        int pointers = s.length() - 1;
        int pointert = t.length() - 1;
        int countt = 0;
        int counts = 0;

        while (pointers >= 0 || pointert >= 0) {
            while (pointers >= 0 && (s.charAt(pointers) == '#' || counts > 0)){
                if (s.charAt(pointers) == '#') {
                    counts++;
                    pointers--;
                }
                else {
                    pointers--;
                    counts--;
                }
            }

            while (pointert >= 0 && (t.charAt(pointert) == '#' || countt > 0)){
                if (t.charAt(pointert) == '#') {
                    countt++;
                    pointert--;
                }
                else {
                    pointert--;
                    countt--;
                }
            }

            if ((pointert >= 0 && pointers >= 0) && s.charAt(pointers) != t.charAt(pointert)) {
                return false;
            }
            if ((pointert >= 0 && pointers < 0) || (pointert < 0 && pointers >= 0)) {
                return false;
            }

            pointert--;
            pointers--;

        }
        return true;

    }
}