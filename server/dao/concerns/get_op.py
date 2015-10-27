class GetOp:
    def get_by_id(id):
        with self._s.begin():
            return self._s.query(self._m).filter_by(id=id).first()

    def get_list(offset=0, limit=100):
        with self._s.begin():
            return self._s.query(self._m).offset(offset).limit(limit).all()
