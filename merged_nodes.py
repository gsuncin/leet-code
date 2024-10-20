
class Linked:
  def __init__(self, h1, h2):
    self.h1 = h1
    self.h2 = h2
    self.merged = []
  

  def merge_nodes(self, head_list):
    while True:
      tmpHead = head_list
      if self.h1 == None:
        return False
    
      self.merged.append(tmpHead.data)
      

  def get_merged_list(self):
    self.merge_nodes(self.h1)
    self.merge_nodes(self.h2)
    return self.merged.sort()

def merge_sorted(head1, head2):
  l = Linked(head1, head2)
  return l.get_merged_list()

merge_sorted([1, 2, 3], [4, 5, 6])