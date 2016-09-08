
class MailingList:
    '''Manage groups of e-mail addresses for sending e-mails.'''

    def __init__(self):
        self.email_map = defaultdict(set)

    def add_to_group(self, email, group):
        self.email_map[email].add(group)
