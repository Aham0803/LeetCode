class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        freq = {}

        for item in cpdomains:
            count, domain = item.split()
            count = int(count)

            parts = domain.split('.')

            for i in range(len(parts)):
                subdomain = '.'.join(parts[i:])

                freq[subdomain] = freq.get(subdomain, 0) + count

        result = []

        for domain, count in freq.items():
            result.append(str(count) + " " + domain)

        return result