 
# I didn't read and made this work for 2d matrices that have
# variable columns so it's a little inefficient. Im too lazy
# to fix
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    m_l, m_r, = 0, len(matrix) - 1

    while m_l <= m_r:
        middle = (m_l + m_r) // 2
        if matrix[middle][0] == target:
            return True
        
        elif matrix[middle][0] > target:
            m_r = middle - 1
            
        elif matrix[middle][0] < target <= matrix[middle][len(matrix[middle]) -1]: 
            arr = matrix[middle]
            l, r = 0, len(arr)-1
            while l <= r:
                mid = (r+l) // 2
                if arr[mid] == target:
                    return True
                
                elif arr[mid] > target:
                    r = mid - 1

                else:
                    l = mid + 1

            return False 
            
        else:
            m_l = middle + 1 
    
    return False 

searchMatrix([[1],[3]],3)