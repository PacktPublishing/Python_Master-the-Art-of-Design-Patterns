
    def send_mailing(self, subject, message, from_addr,
                     *groups, headers=None):
        emails = self.emails_in_groups(*groups)
        send_email(subject, message, from_addr,
                   *emails, headers=headers)
