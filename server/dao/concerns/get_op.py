class GetOp:
    def get_by_id(self, id):
        return self._s.query(self._m).filter_by(id=id).first()

    def get_list(self, offset=0, limit=100):
        return self._s.query(self._m).offset(offset).limit(limit).all()
