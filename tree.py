import numpy as np
from node import Node
from pointer import Pointer

class Tree ( ) :

    def __init__ ( self ) :
        self.number_of_nodes = None
        self.root = None
        self.array = None

    def factorial ( self , number ) :
        '''Returns the factorial of a number'''
        f = 1
        for i in range ( 1 , number + 1 ) :
            f *= i

        return f

    def combination ( self , n , r ) :
        '''Returns the combination 
        Generalised Formula =           n!
                                  ---------------
                                  ( n - r )! * r!'''
        return self.factorial ( n ) / ( self.factorial ( n - r ) * self.factorial ( r ) )
        

    def get_catalan_Number ( self , number_of_nodes ) :
        '''Returns the number of trees possible for a given set of nodes.'''
        return self.combination ( 2 * number_of_nodes , number_of_nodes ) / ( number_of_nodes + 1 )

    def get_minimum_Nodes ( self , height ) :
        return height + 1

    def get_maximum_Nodes ( self , height ) :
        return ( ( 2 ** ( height + 1 ) ) - 1 )

    def get_minimum_Height ( self , number_of_nodes ) :
        return ( np.log2 ( number_of_nodes + 1 ) - 1 )

    def get_maximum_Height ( self , number_of_nodes ) :
        return number_of_nodes - 1

    def get_Index ( self , element ) :
        '''Returns the index of a specific element'''
        c = 1
        for i in self.array :
            if i == element :
                return c
            c += 1

    def get_LeftChild ( self , element ) :
        '''Retruns the Left Child of a node'''
        index = self.get_Index ( element )
        return self.array [ ( index * 2 ) - 1 ]

    def get_RightChild ( self , element ) :
        '''Retruns the Right Child of a node'''
        index = self.get_Index ( element )
        return self.array [ ( index * 2 ) ]

    def get_Parent ( self , element) :
        '''Retruns the Parent of a node'''
        index = self.get_Index ( element )
        return self.array [ ( index // 2 - 1 ) ]

    def input_Tree ( self ) :
        no_of_nodes = int ( input ( "Enter how many nodes you want?: " ) )
        lst = [ ]
        print ( f"Enter {no_of_nodes} values of nodes: " )
        for i in range ( no_of_nodes ) :
            lst.append ( int ( input ( ) ) )
        
        return self.create_Tree ( np.array ( lst ) )

    def create_Tree ( self , array ) :
        l = []
        l.append ( 0 )
        for i in range ( len ( array ) ) :
            n = Node ( array [ i ] )
            l.append ( n )
        
        for i in range (  1, len ( l ) ) :
            if i * 2 < len ( l ) :
                l [i].left = l [ i * 2 ]
                print ( f"{l[i].data} left {l[i*2].data} ")
            if ((i * 2) + 1) < len ( l ) :
                l [i].right = l [ (i * 2) + 1  ]
                print ( f"{l[i].data} right {l[(i*2)+1].data} ")
                
        return l[1]

    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res