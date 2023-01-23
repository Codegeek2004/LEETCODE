class Solution(object):
    def detectCapitalUse(self, w):
        if(w==w.upper()):
            return True
        elif(w==w.capitalize()):
            return True
        elif(w==w.lower()):
            return True
        else:
            return False