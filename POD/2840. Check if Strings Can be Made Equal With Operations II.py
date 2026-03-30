class Solution(object):
    def checkStrings(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        hashh1o = {}
        hashh1e = {}
        hashh2o = {}
        hashh2e = {}
        for i in range(0,len(s1)):
            if i % 2 == 0:
                try: 
                    hashh1o[s1[i]] += 1
                except:
                    hashh1o[s1[i]] = 1
            else:
                try: 
                    hashh1e[s1[i]] += 1
                except:
                    hashh1e[s1[i]] = 1
        
        for i in range(0,len(s2)):
            if i % 2 == 0:
                try: 
                    hashh2o[s2[i]] += 1
                except:
                    hashh2o[s2[i]] = 1
            else:
                try: 
                    hashh2e[s2[i]] += 1
                except:
                    hashh2e[s2[i]] = 1
        
        return hashh2e == hashh1e and hashh2o == hashh1o
