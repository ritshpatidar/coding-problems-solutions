#Complicated Solutions
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        p1 = len(s)-1
        p2 = len(t)-1
        
        while p2>=0 or p1>=0:
            hashCnt = 0
            while p1 >= 0:
                if s[p1] == "#":
                    hashCnt += 1
                    p1 -= 1
                elif hashCnt > 0:
                    hashCnt -= 1
                    p1 -= 1
                else:
                    break
            
            hashCnt2 = 0
            while p2 >= 0:
                if t[p2] == "#":
                    hashCnt2 += 1
                    p2 -= 1
                elif hashCnt2 > 0:
                    hashCnt2 -= 1
                    p2 -= 1
                else:
                    break
            
            if p1>=0 and p2>=0:
                if s[p1] != t[p2]:
                    return False
            elif (p1 < 0 and p2>=0) or (p2 < 0 and p1>=0):
                return False
            
            p1 -= 1
            p2 -= 1
            
        return True

class Solution2:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sp = len(s) - 1
        tp = len(t) - 1
        shc = 0 #s hash count
        thc = 0 #t hash count
        
        while sp >= 0 or tp >= 0:
            
            if sp >= 0:
                if s[sp] == '#':
                    shc += 1
                    sp -= 1
                    continue
            
            if tp >= 0:
                if t[tp] == '#':
                    thc += 1
                    tp -= 1
                    continue
            
            if shc > 0 or thc > 0:
                if shc > 0:
                    shc -= 1
                    sp -= 1
                if thc > 0:
                    thc -= 1
                    tp -= 1
            else:
                if sp<0 or tp<0:
                    return False
                if s[sp] != t[tp]:
                    return False
                else:
                    sp -= 1
                    tp -= 1
        return True
        
