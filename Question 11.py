class Node(object):
      def __init__(self, value):
          self.value=value
          self.next=None
          self.prev=None

class List(object):
      def __init__(self):
          self.head=None
          self.tail=None
      def insert(self,n,x):
          #Not actually perfect: how do we prepend to an existing list?
          if n!=None:
              x.next=n.next
              n.next=x
              x.prev=n
              if x.next!=None:
                  x.next.prev=x              
          if self.head==None:
              self.head=self.tail=x
              x.prev=x.next=None
          elif self.tail==n:
              self.tail=x
      def display(self):
          values=[]
          
          n=self.head
          while n!=None:
              values.append(str(n.value))
              n=n.next
          print ("List: ",",".join(values))

      def delete(self,N):
          if N.prev != None: 
              N.prev.next = N.next  
          else:
              l.head = N.next
          if N.next != None:
              N.next.prev = N.prev
          else:
              l.tail = N.prev
            
          
if __name__ == '__main__':
      l=List()
      l.insert(None, Node(4))
      l.insert(l.head,Node(6))
      #n = Node(6)
      #l.insert(l.head,n)
      l.insert(l.head,Node(5))
      l.delete(l.head)

      #l.delete( n )
      
      l.display()
