class Solution {
    public boolean isValid(String s) {
        Scanner sc=new Scanner(System.in);
        Stack<Character> st=new Stack<>();
        if(s.length()==1){
            return false;
        }
        for(int i=0;i<s.length();i++){
            char ch=s.charAt(i);
            if(ch=='(' || ch=='{' || ch=='['){
                st.push(ch);
            }else{
                if(st.isEmpty()){
                    return false;
                }
                else{
                    char top=st.pop();
                    if((top!='(' && ch==')') ||
                        (top!='{' && ch=='}')||
                        (top!='[' && ch==']')){
                            return false;
                        }
                }
            }
        }
        if(st.isEmpty()){
            return true;
        }
        else{
            return false;
        }
        
    }
}
