class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = [0]*len(gas)
        for i in range(len(gas)) :
            l[i] = gas[i]-cost[i]
        
        if sum(l) < 0 :
            return -1
        
        cum, answer = 0, 0
        for i in range(len(gas)) :
            cum += l[i]
            if cum < 0 :
                answer = i+1
                cum=0

        return answer