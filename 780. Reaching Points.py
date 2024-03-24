class Solution:
    '''
    APPROACH-3: work backwards (Modulo Variant)
    start from tx, ty and try to reach sx, sy
    notice any value can't be negative
    TIME: O(max(tx, ty))
    '''
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy: return True     # reached target
            
            if tx > ty:
                tx %= ty            # this is similar to doing tx -= ty multiple times
            elif tx <= ty:
                ty %= tx            # this is similar to doing ty -= tx multiple times

            if tx == sx:            # if x values are same, isolate the y values, check if the difference btw these y values is divisble by (tx or sx, both are same) value or not
                if (ty - sy) % tx == 0: return True
                else: return False
            
            if ty == sy:            # if y values are same, isolate the x values, check if the difference btw x values is divisible by this y value or not
                if (tx - sx) % ty == 0: return True
                else: return False

        return False


    '''
    APPROACH-2: work backwards (Naive Variant)
    start from tx, ty and try to reach sx, sy
    notice any value can't be negative
    TIME: O(max(tx, ty))
    '''
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy: return True
            
            if tx > ty:
                tx = tx - ty
            elif tx <= ty:
                ty = ty - tx

        return False

    '''
    APPROACH-1: brute force recursion
    '''
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if sx > tx or sy > ty: 
            return False
        if sx == tx and sy == ty: 
            return True
        
        return (self.reachingPoints(sx + sy, sy, tx, ty) or 
                self.reachingPoints(sx, sx + sy, tx, ty))