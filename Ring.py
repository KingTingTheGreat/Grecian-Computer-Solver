COLUMNS = 12


class Ring:
    def __init__(self, rows):
        # all rows must have the same number of columns
        for inner in rows:
            assert len(inner) == COLUMNS
        self.rows = rows

    def __repr__(self):
        return repr(self.rows)

    def __iter__(self):
        return iter(self.rows)

    def __getitem__(self, i):
        return self.rows[i]

    def __len__(self):
        return len(self.rows)

    def rotate(self):
        for i, row in enumerate(self.rows):
            self.rows[i] = row[1:] + row[:1]
