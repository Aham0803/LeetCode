class Solution:
    def secondHighest(self, s: str) -> int:
        val  = set()
        for v in s:
            if v.isdigit():
                val.add(int(v))
        maxV , smax = -1 , -1

        # for v in val:
        #     if v > maxV:
        #         smax = maxV
        #         maxV = v
        #     else:
        #         smax = v
        for v in val:
            if v > maxV:
                maxV = v
        for v in val:
            if v < maxV and v > smax:
                smax= v
        return smax

