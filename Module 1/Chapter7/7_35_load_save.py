def save(self):
    with open(self.data_file, 'w') as file:
        for email, groups in self.email_map.items():
            file.write(
                '{} {}\n'.format(email, ','.join(groups))
            )

def load(self):
    self.email_map = defaultdict(set)
    try:
        with open(self.data_file) as file:
            for line in file:
                email, groups = line.strip().split(' ')
                groups = set(groups.split(','))
                self.email_map[email] = groups
    except IOError:
        pass
