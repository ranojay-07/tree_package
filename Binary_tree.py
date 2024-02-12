from pointer import Pointer
from node import Node

class Binary_Tree ( ) :

    # def create_Tree ( self , values ) :
    #     root = Pointer ( )
    #     for i in values :
    #         n = Node ( i )

    
    def bst ( self , values ) :
        first = True
        root = Node ( values )
        r = Pointer ( )
        r.next = root
        first = True
        for v in range ( 1 , len ( values ) ) :
            n = Node ( v )
            print ( n.data )
            while True :
                if n.data > r.next.data and r.next.right == None :
                    r.next.right = n
                    break

                elif n.data < r.next.data and r.next.left == None :
                    r.next.left = n
                    break

                elif n.data > r.next.data and r.next.right != None :
                    r = r.next.right

                elif n.data < r.next.data and r.next.left != None :
                    r = r.next.left

                else :
                    print ( "Binary Tree Cannot contain any duplicates" )
                    break
            
            r.next = root


    # def bst ( self , values ) :
    #     root = Node ( values [ 0 ] )

masti = [ 1,2,3,4,5,6,7,8,9,10 ]
mast = Binary_Tree ( )
mast.bst ( masti )