class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1=len(num1)
        l2=len(num2)

        if (l2>l1):   # taking smaller string as nums2
            num1,num2=num2,num1

        l1=len(num1)
        l2=len(num2)

        res=[0]*(l1+l2)
        res_pointer=len(res)-1
        res_pointer_count=0

        carry=0

        j=l2-1

        while j>-1:
            res_pointer=len(res)-1-res_pointer_count
            for i in range((l1)-1,-1,-1):
                temp1 = int(num1[i])
                temp2 = int(num2[j])

                inplace = (temp1*temp2)%10
                carry= (temp1*temp2)//10

                res[res_pointer]+=inplace
                res[res_pointer-1]+=carry

                if res[res_pointer]>9:
                    inplace = res[res_pointer]%10
                    carry= res[res_pointer]//10
                    res[res_pointer]=inplace
                    res[res_pointer-1]+=carry

                res_pointer-=1

            res_pointer_count+=1
            j-=1

        ans=""
        for i in res:
            ans=ans+str(i)
        return str(int(ans))