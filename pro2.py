  def slove(A):
  
        n = len(A)
        l = [A[0]]
        cnt = 0
        for i in range(n):
            if l[cnt][0] <= A[i][0] and l[cnt][1] >= A[i][1]:
                continue
            if l[cnt][1] >= A[i][0]:
                l[cnt][1] = A[i][1]
            else:
                l.append(A[i])
                cnt +=1
        return l
