# Last updated: 2/9/2026, 9:54:37 PM
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = Counter()
        for domain in cpdomains:
            num_str, d_str = domain.split()
            num = int(num_str)
            counts[d_str] += num
            while '.' in d_str:
                index = d_str.index('.')
                d_str = d_str[index+1 : ]
                counts[d_str] += num
        return [f"{num} {domain}" for domain, num in counts.items()]
