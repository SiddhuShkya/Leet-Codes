class SnapshotArray(object):

    def __init__(self, length):
        self.data = [{0: 0} for _ in range(length)]
        self.snap_id = 0

    def set(self, index, val):
        self.data[index][self.snap_id] = val

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        if snap_id in self.data[index]:
            return self.data[index][snap_id]
        else:
            snap_ids = sorted(self.data[index].keys())
            closest_snap_id = max([sid for sid in snap_ids if sid <= snap_id])
            return self.data[index][closest_snap_id]
         

snapshotArr = SnapshotArray(3)
snapshotArr.set(0,5)
print(snapshotArr.snap())
snapshotArr.set(0,6)
print(snapshotArr.get(0,0))