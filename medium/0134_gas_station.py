class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        start = 0
        total_gas = 0
        available_gas = 0

        for i in range(n):
            balance = gas[i] - cost[i]
            total_gas += balance
            available_gas += balance

            if available_gas <0:
                start = i+1
                available_gas = 0
        
        return start if total_gas >= 0 else -1
        
        return start
