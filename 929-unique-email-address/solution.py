class Solution:
    def num_unique_emails(self, emails):
        pairs = set()

        for email in emails:
            local, domain = email.split('@')

            local = local.split('+')[0]

            local = local.replace('.', '')

            pairs.add((local, domain))

        return len(pairs)
