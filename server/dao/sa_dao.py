class SADao:
    """
    SqlAclchemy DAO
    """
    def _refresh(self, obj):
        self._s.add(obj)
        self._s.flush()
        self._s.refresh(obj)
