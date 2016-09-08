        for link in unvisited_links:
            if not link.startswith(self.url):
                continue
            self.collect_links(urlparse(link).path)
